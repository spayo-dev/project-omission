# Project Omission

A privacy-preserving PII scrubber for LLM prompts in FinTech and education applications.

# Problem
FinTech applications increasingly rely on LLMs for features like document summarization and grant application assistance. However, sending raw student data (Names, SINs, Financials) to third-party providers (OpenAI, Anthropic) creates significant compliance and privacy risks.

As per **OWASP Top 10 for LLM Applications 2025**, failing to sanitize this data results in *LLM02:2025 Sensitive Information Disclosure*. 

# The Solution: "Sanitize First, Inference Second"
Project Omission acts as a proxy layer between the frontend client and the LLM. It uses Natural Language Processing (NLP) to contextually identify PII and replace it with entity tags.

### Key Features
*   **Context-Aware Scrubbing:** Uses **Microsoft Presidio** (backed by `spaCy` en_core_web_lg) to distinguish between "Call me at 555-0199" (Phone) and "Ticket #5550199" (Non-PII).
*   **Stateless Architecture:** No data persistence. Processed in-memory.
*   **Strict Validation:** Uses **Pydantic** to enforce strict input/output contracts.
*   **Containerized:** Deploys as a Docker microservice.

**Note**: Omission reduces risks but does not replace a full security of your LLM. 
---

## OWASP 2025 Coverage
This project  mitigates the following risks from the [OWASP Top 10 for LLM Applications 2025 (Latest)](https://genai.owasp.org/):

| ID | Vulnerability | How Project Omission Mitigates |
| :--- | :--- | :--- |
| **LLM02** | **Sensitive Information Disclosure** | **Direct Mitigation.** By scrubbing PII *before* the prompt leaves the secure enclave, we prevent sensitive data from entering the model provider's logs or training data. |
| **LLM08** | **Vector and Embedding Weaknesses** | **preventative.** Ensures that PII is not embedded into Vector Databases (RAG), preventing cross-tenant data leakage or retrieval of secrets via semantic search. |
| **LLM10** | **Unbounded Consumption** | **Partial.** Enforces strict token/character limits (`max_length=5000`) on inputs to prevent DoS via massive payload injections. |

## Architecture

![Project Omission Architecture](docs/images/Omission%20Diagram.png)

1.  **Ingest:** API receives raw text payload via `POST /api/v1/scrub`.
2.  **Analyze:** Presidio Analyzer identifies entities (SSN, CREDIT_CARD, EMAIL).
3.  **Anonymize:** Entities are replaced with distinct tags `<ENTITY_TYPE>` to preserve grammatical context for the LLM.
4.  **Forward:** The sanitized string is returned to the application for safe inference.

## API Example

```bash 
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/scrub' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "My name is Sean and my email is sean@mru.ca."
}'

{
  "original_text_length": 44,
  "clean_text": "My name is <PERSON> and my email is <EMAIL_ADDRESS>.",
  "redacted_items": [
    "EMAIL_ADDRESS",
    "PERSON",
    "URL"
  ]
}
```

 # Quick Start (Docker)

Prerequisites: Docker Desktop.

```bash
# Quick Start (Production Mode)
To run the application as a standalone container (simulating a production deployment):

```bash
# 1. Build the image (bakes in the NLP model)
docker build -t project-omission .

# 2. Run the container
# Note: Ensure .env file exists or pass variables manually (API KEY)
docker run -p 8000:8000 --env-file .env project-omission

# Development (Hot Reload)
For active development with source code mounting and auto-reloading:

# Starts the service with volume mounts defined in docker-compose.yml
docker-compose up --build

```

# Roadmap
1. Canadian SIN Support: Implement a way to validate Canadian Social Insurance numbers using the Luhn Algorithm. 

# References
[Presidio](https://microsoft.github.io/presidio/)
[Ploomer](https://ploomber.io/blog/pii-openai/)

Testing to see if SSH still works
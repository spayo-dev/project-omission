# FastAPI Application Documentation

This document provides an overview of the FastAPI application structure, including key directories and files, as well as developer workflow instructions.

## Key Directories and Files
- **app/**: The main application directory.
  - **main.py**: The entry point for the FastAPI application.
  - **schemas/**: Contains Pydantic models for data validation and serialization.
  - **api/**: Contains the API route definitions.
  - **core/**: Contains core application logic, such as configuration and security.
  - **db/**: Contains database models and access functions.
  - **tests/**: Contains test cases for the application.

- **Payload Schemas**: Define input/output structures in `app/schemas/payload.py`.

## Developer Workflows
- **Running the App**: From the project root, run:
  ```bash
  uvicorn app.main:app --reload
  ```
  (Note: Do not run `uvicorn main:app` unless you are inside the `app` directory, but running from root is preferred to resolve imports correctly.)
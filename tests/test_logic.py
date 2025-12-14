from app.services.scrubber import scrubber_service

# Simulating a FinTech user input
# Presidio does not redact fake SSNs (like the one below) to ensure no false positives, but this is just for demonstration.
# Swap to a common SSN to see redaction in action
sample_text = """
Hi, my name is Sean Payomo. 
My email is sean@example.com and my SSN is 123-45-6789.
I am applying for a grant.
"""

print("--- ORIGINAL ---")
print(sample_text)

print("\n--- PROCESSING ---")
result = scrubber_service.scrub_text(sample_text)

print("\n--- CLEANED ---")
print(result["clean_text"])

print("\n--- REDACTED ENTITIES ---")
print(result["redacted_items"])


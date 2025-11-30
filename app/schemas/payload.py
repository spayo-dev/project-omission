from pydantic import BaseModel, Field
from typing import List

# Request and Response models for the PII Scrubber API
class ScrubberRequest(BaseModel):
    text: str = Field(
        ..., 
        min_length=1, 
        max_length=5000, 
        description="The raw text containing potential PII.",
        example="My name is Sean and my email is sean@mru.ca."
    )

# Response model for the PII Scrubber API
class ScrubberResponse(BaseModel):
    original_text_length: int = Field(..., description="Length of the original input.")
    clean_text: str = Field(..., description="Text with PII replaced by <ENTITY> tags.")
    redacted_items: List[str] = Field(..., description="List of entity types found and redacted.")
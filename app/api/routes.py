from fastapi import APIRouter, HTTPException
from app.schemas.payload import ScrubberRequest, ScrubberResponse
from app.services.scrubber import scrubber_service

router = APIRouter()

@router.post("/scrub", response_model=ScrubberResponse, summary ="Scrub PII from text")
async def scrub_text(payload: ScrubberRequest):
    """
    Scrub PII from the provided text using Microsoft Presidio.

    Input: Raw text containing potential PII.
    Output: Sanitized text with PII replaced by <ENTITY> tags and a list of redacted items.
    """
    try:
        # Call the service layer
        result = scrubber_service.scrub_text(payload.text)
        
        # Prepare and return the response
        return ScrubberResponse(
            original_text_length=len(payload.text),
            clean_text=result["clean_text"],
            redacted_items=result["redacted_items"]
        )
    # Handle exceptions and return appropriate HTTP errors
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error during PIU processing.") from e

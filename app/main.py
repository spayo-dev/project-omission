from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import api_router   

app = FastAPI(
    description="Middleware to prevent OWASP LLM02 (Sensitive Data Disclosure) by scrubbing PII from text using Microsoft Presidio.",
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    version="1.0.0"
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/health")
async def health_check():
    """
    Health check endpoint for Kubernetes/Docker orchestration.
    """
    ## Health check response
    return {"status": "healthy", "service": settings.PROJECT_NAME}
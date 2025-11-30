from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.get("/health")
async def health_check():
    """
    Health check endpoint for Kubernetes/Docker orchestration.
    """
    ## Health check response
    return {"status": "healthy", "service": settings.PROJECT_NAME}
from fastapi import FastAPI
from app.api.v1.routes import health, resume

app = FastAPI(
    title="Smart Resume Screener API",
    version="1.0.0"
)

app.include_router(health.router, prefix="/api/v1")
app.include_router(resume.router, prefix="/api/v1")

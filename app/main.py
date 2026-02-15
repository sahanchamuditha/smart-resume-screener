from fastapi import FastAPI
from app.api.v1.routes import health, resume, match
from app.api.v1.routes import rank
from app.api.v1.routes import job


app = FastAPI(
    title="Smart Resume Screener API",
    version="1.0.0"
)

app.include_router(health.router, prefix="/api/v1")
app.include_router(resume.router, prefix="/api/v1")
app.include_router(match.router, prefix="/api/v1")
app.include_router(rank.router, prefix="/api/v1")
app.include_router(job.router, prefix="/api/v1")


from fastapi import FastAPI
from app.api.v1 import health

app = FastAPI(
	title="Language Buddy API",
	description="API for Language Buddy: AI-powered language practice with buddy matching.",
	version="0.1.0",
	docs_url="/docs",
	redoc_url="/redoc",
	openapi_url="/openapi.json"
)

# Versioned API prefix
app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])
# app.include_router(chat.router, prefix="/api/v1/chat", tags=["chat"])
# app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

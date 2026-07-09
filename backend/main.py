from fastapi import FastAPI

from .routes import router


app = FastAPI(
    title="Cricket Performance Analyzer",
    description="API for cricket performance tracking and analytics",
    version="1.0.0"
)


app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Cricket Performance Analyzer API"
    }


@app.get("/health")
def health():
    return {
        "status": "Running"
    }

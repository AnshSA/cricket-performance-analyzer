from fastapi import FastAPI

app = FastAPI(
    title="Cricket Performance Analyzer",
    description="API for analyzing cricket player performance",
    version="1.0.0"
)


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

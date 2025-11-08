from fastapi import FastAPI
from app.backend.main.src.routers import router

app = FastAPI(
    title="main",
    description="API documentation for main-service",
    version="1.0.0",
    root_path="/api",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)
app.include_router(router)


@app.get("/", status_code=200)
async def test():
    return {"message": "Hi!"}

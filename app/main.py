from fastapi import FastAPI
from app.api.endpoints import router as api_router
from app.utils.logging import configure_logging

app = FastAPI(title="Protocol Upgrade Monitor")
app.include_router(api_router, prefix="/api/v1")

configure_logging()

@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
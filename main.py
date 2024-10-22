from fastapi import FastAPI
from app.routers import router as allocation_router

app = FastAPI() # Initialize FastAPI app


app.include_router(allocation_router)  # Include the allocation router


if __name__ == "__main__":   # Entry point to run the FastAPI app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Run the app on localhost:8000


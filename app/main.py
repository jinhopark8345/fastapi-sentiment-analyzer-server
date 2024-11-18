from fastapi import FastAPI
from app.db.base import Base, engine
from app.routers import feedback, predict
from fastapi.middleware.cors import CORSMiddleware

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # Change to specific origins for better security, e.g., ["http://127.0.0.1:7800"]
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.include_router(feedback.router)
app.include_router(predict.router)

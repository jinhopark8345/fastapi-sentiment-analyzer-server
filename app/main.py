from fastapi import FastAPI
from app.db.base import Base, engine
from app.routers import feedback, predict

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(feedback.router)
app.include_router(predict.router)

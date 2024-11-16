from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from .base import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Add a function to get a session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

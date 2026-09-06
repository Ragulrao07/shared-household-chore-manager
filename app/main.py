from fastapi import FastAPI
from app.models import Base
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Shared Household Chore Manager")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Chore Manager API"}

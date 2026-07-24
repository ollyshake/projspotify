from fastapi import FastAPI
from app.api import concerts

app = FastAPI()

app.include_router(concerts.router)


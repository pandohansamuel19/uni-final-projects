from fastapi import FastAPI
from dataclasses import dataclass
import os

# App Instances
app = FastAPI()


@app.get("/")
async def root() -> None:
    return {"message": "Hello World"}

from fastapi import FastAPI
from pydantic_settings import BaseSettings

app = FastAPI()


class Settings(BaseSettings): ...


settings = Settings()


@app.get("/")
def home():
    return {"message": "Hello world!"}

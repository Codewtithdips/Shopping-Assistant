# main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from routers import auth, chat

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
import os
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SESSION_SECRET"))
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth.router)
app.include_router(chat.router)

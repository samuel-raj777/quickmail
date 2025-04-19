# app.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from inbox_logic import generate_email, get_inbox, receive_email
import os

app = FastAPI()

# CORS settings (open to all for now; restrict in prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate")
def generate():
    return generate_email()

@app.get("/inbox/{email}")
def inbox(email: str):
    return get_inbox(email)

@app.post("/inbox/{email}/receive")
def receive(email: str, message: dict):
    return receive_email(email, message)

@app.get("/")
def read_root():
    return {"message": "QuickMail backend is working!"}
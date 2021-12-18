from fastapi import FastAPI, UploadFile, File, HTTPException
import httpx
import urllib.parse
import os
from httpx import ReadTimeout
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")  # set via environment / .env

@app.post("/submit")
async def submit_code(file: UploadFile = File(...)):
    code = (await file.read()).decode("utf-8")
    snippet = code[:50].strip()

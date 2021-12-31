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
    if not snippet:
        raise HTTPException(status_code=400, detail="Empty code snippet")

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    query = f"{snippet} in:file"
    encoded_query = urllib.parse.quote(query)
    url = f"https://api.github.com/search/code?q={encoded_query}&per_page=5"

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.get(url, headers=headers)
    except ReadTimeout:

# CodePatrol

CodePatrol is a plagiarism-detection web app. It accepts a code snippet,
normalizes it, and compares it against other submissions and public GitHub
code using a fingerprinting similarity engine.

## Features

- Submit a code snippet through a React + CodeMirror editor.
- FastAPI backend that queries GitHub code search for matches.
- Local plagiarism engine using tokenization, identifier normalization and
  winnowing fingerprints to score similarity against stored submissions.

## Project Structure

- `backend/` — FastAPI service, SQLAlchemy models, and the `plagiarism_engine`
  package (tokenizer, normalizer, winnowing, compare).
- `frontend/` — React + Vite + Tailwind UI for submitting code and viewing
  similarity results.

## Running Locally

Backend:

```
cd backend
source venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Frontend:

```
cd frontend
npm install
npm run dev
```

The frontend dev server proxies `/submit` to the backend on port 8000.

# CodePatrol

CodePatrol is a plagiarism-detection web app. It accepts a code snippet,
normalizes it, and compares it against other submissions and public GitHub
code using a fingerprinting similarity engine.

## Features

- Submit a code snippet through a React + CodeMirror editor.
- FastAPI backend that queries GitHub code search for matches.

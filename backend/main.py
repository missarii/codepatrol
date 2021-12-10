from fastapi import FastAPI, UploadFile, File, HTTPException
import httpx
import urllib.parse
import os
from httpx import ReadTimeout
from dotenv import load_dotenv


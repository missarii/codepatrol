import re

def tokenize(code: str):
    tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*|\d+|[^\s]", code)

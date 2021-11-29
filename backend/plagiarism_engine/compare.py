from .tokenizer import tokenize
from .normalizer import normalize
from .winnowing import get_hashes

def compare_all(new_code: str, others):
    new_tokens = normalize(tokenize(new_code))
    new_hashes = get_hashes(new_tokens)
    best_score = 0
    best_match = None
    for sub in others:
        tokens = normalize(tokenize(sub.code))
        hashes = get_hashes(tokens)

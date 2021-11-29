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
        similarity = len(new_hashes.intersection(hashes)) / max(len(new_hashes), 1)
        if similarity > best_score:
            best_score = similarity
            best_match = sub.username

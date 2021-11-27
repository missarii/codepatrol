from .tokenizer import tokenize
from .normalizer import normalize
from .winnowing import get_hashes

def compare_all(new_code: str, others):
    new_tokens = normalize(tokenize(new_code))

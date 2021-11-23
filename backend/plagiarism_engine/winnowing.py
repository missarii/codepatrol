def get_hashes(tokens, k=5, window=4):
    hashes = [hash(" ".join(tokens[i:i+k])) for i in range(len(tokens)-k+1)]
    fingerprints = set()
    for i in range(len(hashes) - window + 1):

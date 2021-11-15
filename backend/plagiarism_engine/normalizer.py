def normalize(tokens):
    var_map = {}
    count = 1
    normalized = []
    for token in tokens:
        if token.isidentifier() and not token in ["if", "for", "while", "return"]:

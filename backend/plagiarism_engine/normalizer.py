def normalize(tokens):
    var_map = {}
    count = 1
    normalized = []
    for token in tokens:
        if token.isidentifier() and not token in ["if", "for", "while", "return"]:
            if token not in var_map:
                var_map[token] = f"var{count}"
                count += 1
            normalized.append(var_map[token])
        else:
            normalized.append(token)
    return normalized

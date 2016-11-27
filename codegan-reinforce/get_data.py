

def get_data():
    token_stream = []
    with open("code.txt", 'r') as f:
        for line in f:
            toks = tokenize(line)
            for tok in toks:
                token_stream.append("".join(toks))
    return token_stream

print(get_data())

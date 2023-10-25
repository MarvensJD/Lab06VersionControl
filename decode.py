def decode(encoded):
    return "".join([str((int(x) - 3) % 10) for x in encoded])
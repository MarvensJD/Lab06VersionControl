# Quentin Wright

def encode(passcode):
    encoded_passcode = []
    for i in range(len(passcode)):
        encoded_passcode.append(str((int(passcode[i]) + 3) % 10))
    encoded_passcode = ''.join(encoded_passcode)
    return encoded_passcode
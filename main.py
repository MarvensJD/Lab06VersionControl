# Quentin Wright

from decode import decode

def encode(passcode):
    encoded_passcode = []
    for i in range(len(passcode)):
        encoded_passcode.append(str((int(passcode[i]) + 3) % 10))
    encoded_passcode = ''.join(encoded_passcode)
    return encoded_passcode

if __name__ == "__main__":
    password = ""
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        choice = int(input('Please enter an option: '))
        if choice == 1:
            password = input('Please enter your password to encode: ')
            password = encode(password)
            print('Your password has been encoded and stored!\n')
        elif choice == 3:
            break

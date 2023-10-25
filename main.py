from encode import encode

def decode(encoded):
    return "".join([str((int(x) - 3) % 10) for x in encoded])

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

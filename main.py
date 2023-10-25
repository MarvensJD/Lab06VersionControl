from encode import encode
from decode import decode

if __name__ == "__main__":
    password = ""
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        choice = int(input('Please enter an option: '))
        if choice == 1:
            password = input('Please enter your password to encode: ')
            password = encode(password)
            print('Your password has been encoded and stored!\n')
        elif choice == 2:
            decoded_password = decode(password)
            print(f"The encoded password is {password}, and the original password is {decoded_password}.")
        elif choice == 3:
            break

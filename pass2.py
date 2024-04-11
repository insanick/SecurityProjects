import string
import random

def lowers(chars):
    chars = chars

    for letter in string.ascii_lowercase:
        chars.append(letter)

    return chars

def uppers(chars):
    chars = chars

    for letter in string.ascii_uppercase:
        chars.append(letter)
    
    return chars

def nums(chars):
    chars = chars

    for num in string.digits:
        chars.append(num)

    return chars

def build_keyspace(mode):

    keyspace = []

    if mode == "pin".upper():
        nums(keyspace)
        return keyspace
    
    elif mode == "alphabet".upper():
        uppers(keyspace)
        lowers(keyspace)
        return keyspace
    elif mode == "mixed".upper():
        uppers(keyspace)
        lowers(keyspace)
        nums(keyspace)
        return keyspace
    
def get_keygen_mode():
    
    print("Select your password complexity!")
    print("1) Pin Code\n\tNumbers only!")
    print("2) Alphabet\n\tLower and Upper case letters!")
    print("3) Mixed [MOST SECURE]\n\tAlphabet and Numbers!")

    choice = input("Enter your selection(1, 2, or 3): ")

    choice = int(choice.strip())

    if choice == 1:
        return "pin".upper()
    elif choice == 2:
        return "alphabet".upper()
    elif choice == 3:
        return "mixed".upper()
    else:
        print("Not an option!")
        get_keygen_mode()

def get_key_length():
    key_length = input("Enter how long you want your password to be: ")
    key_length = int(key_length)

    return key_length


def build_password(keyspace, key_length):

    password = ""

    for spot in range(key_length):
        char = random.choice(keyspace)
        password = password + char
    
    print(password)



mode = get_keygen_mode()
keyspace = build_keyspace(mode)
key_length = get_key_length()


build_password(keyspace, key_length)





    

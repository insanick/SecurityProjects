import random
import string 

class Key():
    '''initialize the key class'''

    def __init__(self):
        '''initialize the class'''

    def lowers():
        '''Initiate the key and add lower case letters to it'''
        key = []
        for i in string.ascii_lowercase:
            key.append(i)
        return key


    def upper_lower():
        '''initialize the key and add all letter variants to it'''
        key = []
        for i in string.ascii_letters:
            key.append(i)
        return key

    def alph_num():
        '''initialize key and add alphanumeric numbers to it'''

        key = []
        chars = string.ascii_letters + string.digits
        for i in chars:
            key.append(i)
        return key

    def nums():
        '''Initiliaze the key and add only digits'''
        key = []
        chars = string.digits
        for i in chars:
            key.append(i)
        return key

    def complx():
        '''initialize key and add alphanumeric AND symbols'''

        key = []
        chars = string.ascii_letters + string.digits + '!@#$%^&?'
        for i in chars:
            key.append(i)
        return key

def gen_pass(key, length):
    '''generate a password using the key and input length'''
    key = key
    pw = ''
    for i in range(length):
        random.shuffle(key)
        pw += random.choice(key)
    
    print(f'Password:\n{pw}')


def get_complexity():
    '''Ask the user for password complexity'''


    print('A. Lowercase only')
    print('B. Lower and Upper')
    print('C. Alphanumeric')
    print('D. Numeric')
    print('E. Alpha + Symbols')
    cmp = input('Choose password complexity  ')
    if cmp.lower() == 'a':
        key = Key.lowers()
        return key
    
    if cmp.lower() == 'b':
        key = Key.upper_lower()
        return key

    if cmp.lower() == 'c':
        key = Key.alph_num()
        return key

    if cmp.lower() == 'd':
        key = Key.nums()
        return key

    if cmp.lower() == 'e':
        key = Key.complx()
        return key
    else:
        print('Not an option!')
        ans = input('Would you like to quit? y/n: ')
        if ans.lower() == 'y':
            print("Shutting down!")
            quit()
        else:
            get_complexity()


def get_length():
    '''Get the key length from the user'''

    len = int(input('Enter key length: '))
    return len



        

def main():

    gen_pass(get_complexity(), get_length())
    




if __name__ == '__main__':

    print('Welcome to P-Man!\nThe Password Generator!\n' + ('_' * 83) + '\n\n')
    main()

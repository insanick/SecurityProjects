def get_pass():
    '''Get the password to be checked'''
    pw = input('Enter password to check: ')
    return pw

def check_pass(pw):
    '''Check the password for complexity requirements'''
    low = False
    up = False
    num = False 
    symbs = False
    symb_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    if len(pw) < 8:
        print(f'Password too short!\nMinimum Length: 8\nPassword Length: {len(pw)}\n')

    for c in pw:
        if c.islower():
            low = True
        if c.isupper():
            up = True
        if c.isdigit():
            num = True
        if c in symb_list:
            symbs = True

    if low == False:
        print('There are no lowercase letters!\n')
    if up == False:
        print('There are no uppercase letters!\n')
    if num == False:
        print('There are no numbers!\n')
    if symbs == False:
        print('There are no symbols!\n')
    else:
        print('Strong password!')

if __name__ == '__main__':
    print('Test your (password) strength!\n')
    check_pass(get_pass())
        


import hashlib 



def target():
    tgt = input('Enter hash to crack: ')
    return tgt



def md(tgt):
    ## Cracking an MD5 hash
    res = ''
    h = hashlib.md5(tgt.encode()).hexdigest()
    try:
        #Opens the wordlist file
        with open('test.txt', 'r') as s:
            for line in s:
                comp = hashlib.md5(line.strip().encode()).hexdigest()
                print(f'Now testing {line}\n {h}:{comp}\n\n')
                if comp == h:
                    print(f'Password cracked!\nPassword: {line}')
                    res = line
                    break
                else:
                    continue
            if res == '':
                print('No Match Found!')
                quit()
                    
    except:
        print('File Not Found')
        quit()
    

            


if __name__ == '__main__':
    print('hello')
    tgt = target()

    md(tgt)



import string
import random


class Password:
    """Password generating engine"""

    def __init__ (self, mode='', key_length=0):
        """Initialize the password generator"""
        print("Intializing the password generator...\n")
        self.mode = mode
        self.key_length = key_length
        self.password = ''
        self.key_space = ''
        print("Generator initialized\n")

        if self.key_length == 0:
            self.get_key_length()

        
        if self.mode == '':
            self.get_mode()
            self.initialize_keyspace()

        

        self.generate_password()



        

    def get_key_length(self):
        """Get the desired password length"""
        try:
            key_length = int(input("Enter desired password length: ").strip())
        except TypeError:
            print("Enter a number please")
            self.get_key_length()

        finally:
            self.key_length = key_length
            print(f"Password will be {self.key_length} characters long\n\n")

    def get_mode(self):
        """Get desired password complexity"""
        self.mode_menu()
        choice = input("Mode: ")
        try:
            choice = int(choice.strip())
        except TypeError:
            print("Enter a number please")
            self.get_mode()
        finally: 
            if choice in range(1,5):
                self.mode = choice
        
            else:
                print("Not an option!\n\n\n")
                self.get_mode()

        
            
        
    def mode_menu(self):
        """Display different generation modes"""
        print("Select your desired password complexity")
        print("1) Numbers only")
        print("2) Alphabet only")
        print("3) Alphanumeric")
        print("4) Alpha + Symbols")

    def initialize_keyspace(self):
        """Initialize the desired complexity"""

        if self.mode == 1:
            self.key_space = self.key_space + string.digits
        elif self.mode == 2:
            self.key_space = self.key_space + string.ascii_letters
        elif self.mode == 3:
            self.key_space = self.key_space + string.ascii_letters + string.digits
        elif self.mode == 4:
            self.key_space = self.key_space + string.ascii_letters + string.digits + "/?.>,<!@#$%^&*()+ "
        

    def generate_password(self):
        print("Creating your password...\n")

        for num in range(self.key_length):
            char = random.choice(self.key_space)
            self.password = self.password + char
        
        print(f"Password:\n{self.password}")


        




def Create_Password(mode = '', key_length = 0):
    password = Password(mode, key_length)

def main():
    Create_Password()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Quitting...")
        quit()
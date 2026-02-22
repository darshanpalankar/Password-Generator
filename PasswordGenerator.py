from pyfiglet import Figlet
import random
import string

x = Figlet(font='slant', width = 550)
print(x.renderText('Password Generator'))

chars = string.ascii_letters + string.digits + "~!@#$%&*?"

# Class for Password generator
class PasswordGenerator:
    #Constructor
    def __init__(self,length):
        self.length = length
        
    #Display Method for displaying password
    def display(self):
        password = ''
        for i in range(self.length):
            password += random.choice(chars)
        
        print(f"\nYour Password : {password}")
    
#Main Function
def main():
    while True:
        try:
            length = int(input('Enter a length of password : '))
            if length >= 8:
                PG = PasswordGenerator(length)
                PG.display()
            else:
                print("Password must be at least 8 characters.")

        except ValueError:
            print('Error,Enter Number only ')
        
        #User Choice
        print('\n1. Next Password.')
        print('2. Exit.')

        choice = input('\nEnter Choice Number : ')

        if choice == '1':
            continue
        elif choice == '2':
            print('<<<<< Exiting Program >>>>>')
            break
        else:
            print('\nInvalid Choice.\n')
            
if __name__ == '__main__':

    main()

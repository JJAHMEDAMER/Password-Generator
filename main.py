import string
from random import shuffle, randint

uppercase = list(string.ascii_uppercase)
lowercase = (list(string.ascii_lowercase ))
numbers = (list(string.digits))
punc = (list(string.punctuation))

class Password:
    def __init__(self, len, show):
        password = ""
        for i in range(len):
            password += uppercase[randint(0,25)]
            password += lowercase[randint(0,25)]
            password += numbers[randint(0,9)]
            password += punc[randint(0,31)]
        password = list(password)
        shuffle(password)
        password = "".join(password[0:len])
        
        file = open("MyPasswords.txt", "a")
        file.write("Pass:: " + password + "\n")
        file.close
        
        if show == 'y': print(password)
        
        


len = input("How long?: ")
show = input("Show Password in Terminal(y/n)?: ")

x = Password(int(len), show.lower())
import string
import os
# thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]

# message = input('enter a message: ')
alphabet = string.printable + " "
key = 5

def encrypt(data):
    filename = 'userdata.txt'
    
    encrypt = ''

    for i in data:
        position = alphabet.find(i)
        newposition = (position+key)%len(alphabet)
        encrypt += alphabet[newposition]

    if os.path.exists(filename):
        append_write = 'a'
    else:
        append_write = 'w'
    f = open(filename, append_write)
    f.write(encrypt + "\n")
    f.close()

def decrypt(data):
    decrypt = ''

    for i in data:
        pos = alphabet.find(i)
        newpos = (pos-key)%len(alphabet)
        decrypt += alphabet[newpos]
    return decrypt


def decrypt_all(login1, login2):

    with open("userdata.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            # print(decrypt(stripped_line))
            li = decrypt(stripped_line).split(" ")
            if li[0] == login1 and li[1] == login2:
               return True
        return False

            
currentUser = ""
currentRole = ""
loginState = False

rootUsername = "RootUser1"
rootPassword = "RootPass1@"

while True:
    welcome = input("Do you have an acount? y/n: ")
    if welcome == "n":
        while True:
            username  = input("Enter a username:")
            password  = input("Enter a password:")
            password1 = input("Confirm password:")
            if password == password1:
                encrypt(username + " " + password)
                welcome == "y"
                break
            print("Passwords do NOT match!")
    
    elif welcome == "y":
        while True:
            login1 = input("Login:")
            login2 = input("Password:")
            if (login1 == "RootUser1" and login2 == "RootPass1@"):
                currentUser = login1
                currentRole = "Root"
                loginState = True
                print("Welcome: " + currentUser + " User Role: " + currentRole + " LoginState: " + str(loginState)) 
                action = input("What do you want to do?")
            result = decrypt_all(login1, login2)
            if result == True:
                print("Welcome")
                currentUser = login1
                loginState = True
                print("Login State: " + str(loginState))
                print("Username: " + currentUser)
            else:
                print("No User")
                break
            
            
                
                
            
    # if loginState == "Logged In":
    #         print("Yo " + currentUser)
    #         yo = input("what now: ")
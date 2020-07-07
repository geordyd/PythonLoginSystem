import string
import os

alphabet = string.printable + " "
key = 5

global currentUser 
currentUser = ""
global currentRole 
currentRole = ""
global loginState 
loginState = False

rootUsername = "1"
rootPassword = "1"


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
               global currentRole
               currentRole = li[2] 
               return True
        return False

def logout():
    global currentUser
    global currentRole
    global loginState
    currentUser = ""
    currentRole = ""
    loginState = False       

def loginAsRoot(user):
    global currentUser
    global currentRole
    global loginState
    currentUser = user
    currentRole = "root"
    loginState = True
    #print("Welcome: " + currentUser + " User Role: " + currentRole + " LoginState: " + str(loginState))

def createUser(role):
    encrypt(username + " " + password + " " + role)
    

while True:
    
    if loginState == False:
        while True:
            # print("Login to user")
            # username  = input("Enter a username:")
            # password  = input("Enter a password:")
            # password1 = input("Confirm password:")
            # if password == password1:
            #     encrypt(username + " " + password)
            #     loginState = True
            #     break
            # print("Passwords do NOT match!")
            login1 = input("Login:")
            login2 = input("Password:")
            #Login as hardcoded root user
            if (login1 == rootUsername and login2 == rootPassword):
                loginAsRoot(login1)
                loginState = True
                break
                
            #Log in as normal user
            #check if user exists
            result = decrypt_all(login1, login2)
            if result == True:
                currentUser = login1
                loginState = True
                break
            else:
                print("Wrong Login")
                break
        
    elif loginState == True:
        print("Welcome: " + currentUser + " User Role: " + currentRole + " LoginState: " + str(loginState)) 

        while True:
            if currentRole == "root":
                while True:
                    rootInput = input("Create System Admin or Logout (c/l): ")
                    if rootInput == "c":
                        username  = input("Enter a username:")
                        password  = input("Enter a password:")
                        password1 = input("Confirm password:")
                        if password == password1:
                            createUser("System-Administrator")
                            break
                        print("Passwords do NOT match!")
                    elif rootInput == "l":
                        logout()
                        break
                    else:
                        rootInput
                    
            elif currentRole == "System-Administrator":
                while True:
                    systemAdminInput = input("Create Advisor or Logout (c/l): ")
                    if systemAdminInput == "c":
                        username  = input("Enter a username:")
                        password  = input("Enter a password:")
                        password1 = input("Confirm password:")
                        if password == password1:
                            createUser("Advisor")
                            break
                        print("Passwords do NOT match!")
                    elif systemAdminInput == "l":
                        logout()
                        break
                    else: 
                        systemAdminInput

            elif currentRole == "Advisor":
                while True:
                    AdvisorInput = input("Logout (l)")
                    if AdvisorInput == ("l: "):
                        logout()
                        break
                    else:
                        AdvisorInput
                #     if systemAdminInput == "c":
                #         username  = input("Enter a username:")
                #         password  = input("Enter a password:")
                #         password1 = input("Confirm password:")
                #         if password == password1:
                #             createUser("Advisor")
                #             break
                #         print("Passwords do NOT match!")
                #     elif systemAdminInput == "l":
                #         logout()
                #         break
                #     else: 
                #         AdvisorInput
            
            else:
                break
            # login1 = input("Login:")
            # login2 = input("Password:")
            # if (login1 == "RootUser1" and login2 == "RootPass1@"):
            #     currentUser = login1
            #     currentRole = "Root"
            #     loginState = True
            # result = decrypt_all(login1, login2)
            # if result == True:
            #     print("Welcome")
            #     currentUser = login1
            #     loginState = True
            #     print("Login State: " + str(loginState))
            #     print("Username: " + currentUser)
            # else:
            #     print("No User")
            #     break
            # print("User is logged in.")
            
                
                
            
    # if loginState == "Logged In":
    #         print("Yo " + currentUser)
    #         yo = input("what now: ")
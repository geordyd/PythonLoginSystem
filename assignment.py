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

city = ["Amsterdam", "Rotterdam", "Utrecht", "Eindhoven", "Groningen", "Tilburg", "Almere", "Breda", "Nijmegen", "Apeldoorn"]

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

def encryptClient(data):
    filename = 'clientdata.txt'
    
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

def createUser(role):
    encrypt(username + " " + password + " " + role)

def createClient(firstName, lastName, streetName, houseNumber, zipcode, cityName, email, phoneNumber):
    encryptClient(firstName + " " + lastName + " " + streetName + " " + houseNumber + " " + zipcode + " " + cityName + " " + email + " " + phoneNumber)

def printCity():
    print("Choose street index")
    i = 0
    while i < len(city):
        
        print( str(i) + ": " + city[i])
        i += 1

def checkStreetIndex(name):
    i = 0
    while i < len(city):
        if name == str(i):
            return True
        i += 1
    return False



while True:
    
    if loginState == False:
        while True:
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
                        #Julia validation
                        # validation = userval(username)
                        # if validation == True:
                        #     password  = input("Enter a password:")
                        #     password1 = input("Confirm password:")
                        # else: 
                        #     print("Error")
                        #     username
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
                    systemAdminInput = input("Create Advisor or New Client or Logout (c/n/l): ")
                    if systemAdminInput == "c":
                        username  = input("Enter a username:")
                        password  = input("Enter a password:")
                        password1 = input("Confirm password:")
                        if password == password1:
                            createUser("Advisor")
                            break
                        print("Passwords do NOT match!")
                    elif systemAdminInput == "n":
                        firstName  = input("Enter a First Name:")
                        lastName = input("Enter a Last Name:")
                        printCity()
                        while True:
                            streetName = input("Enter a Street:")
                            checkIndex = checkStreetIndex(streetName)
                            try:
                                if checkIndex == True:
                                    break
                                else:
                                    raise  ValueError
                            except ValueError:
                                print("Error")
                        houseNumber  = input("Enter a House Number:")
                        zipcode = input("Enter a Zip Code:")
                        cityName = input("Enter a City:")
                        email  = input("Enter an Email:")
                        phoneNumber = input("Enter a Phone Number:")
                        createClient(firstName, lastName, streetName, houseNumber, zipcode, cityName, email, phoneNumber)
                        break                        

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
            
            else:
                break

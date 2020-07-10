import string
import os
from datetime import datetime

alphabet = string.printable + " "
key = 5

global currentUser
currentUser = ""
global currentRole
currentRole = ""
global loginState
loginState = False
global validation
validation = True
global validationPass
validationPass = True

rootUsername = "1"
rootPassword = "1"

city = ["Amsterdam", "Rotterdam", "Utrecht", "Eindhoven", "Groningen", "Tilburg", "Almere", "Breda", "Nijmegen",
        "Apeldoorn"]


def encrypt(data):
    filename = 'userdata.txt'

    encrypt = ''

    for i in data:
        position = alphabet.find(i)
        newposition = (position + key) % len(alphabet)
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
        newposition = (position + key) % len(alphabet)
        encrypt += alphabet[newposition]

    if os.path.exists(filename):
        append_write = 'a'
    else:
        append_write = 'w'
    f = open(filename, append_write)
    f.write(encrypt + "\n")
    f.close()

def encryptLog(data):
    filename = 'log.txt'

    encrypt = ''

    for i in data:
        position = alphabet.find(i)
        newposition = (position + key) % len(alphabet)
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
        newpos = (pos - key) % len(alphabet)
        decrypt += alphabet[newpos]
    return decrypt


def decrypt_all(login1, login2):

    filename = 'userdata.txt'

    if os.path.exists(filename):
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
    else:
        return False


def getUserInfo(user):

    with open("clientdata.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            # print(decrypt(stripped_line))
            li = decrypt(stripped_line).split(" ")
            if li[0] == user:
               return li[0] + " | " + li[1] + " | " + li[2] + " | " + li[3] + " | " + li[4] + " | " + li[5] + " | " + li[6] + " | " + li[7] + " | "
        return "No User"


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
    encryptClient(
        firstName + " " + lastName + " " + streetName + " " + houseNumber + " " + zipcode + " " + cityName + " " + email + " " + phoneNumber)


def printCity():
    print("Choose street index")
    i = 0
    while i < len(city):
        print(str(i) + ": " + city[i])
        i += 1


def checkCityIndex(name):
    i = 0
    while i < len(city):
        if name == str(i):
            return True
        i += 1
    return False


def checkNameIndex(firstName):
    SpecialSym = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '`', '|', '(', ')', '{', '}', '[',
                  ']', ':', ';', '<', '>', '.', '?', '/', '.', "'", "\\", ' ']
    if len(firstName) < 25 and len(firstName) > 1:
        if not any(char.isdigit() for char in firstName):
            if not any(char in SpecialSym for char in firstName):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def checkLastnameIndex(lastName):
    SpecialSym = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '`', '|', '(', ')', '{', '}', '[',
                  ']', ':', ';', '<', '>', '.', '?', '/', '.', "'", "\\", ' ']
    # null = None

    if len(lastName) < 25 and len(lastName) > 1:
        if not any(char.isdigit() for char in lastName):
            if not any(char in SpecialSym for char in lastName):
                if lastName != "":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def checkHouseNumberIndex(houseNumber):
    space = [' ']
    if len(houseNumber) <= 1000:
        if any(char.isdigit() for char in houseNumber):
            if not any(char in space for char in houseNumber):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def checkzipIndex(zipcode):
    splitstring = zipcode.split()
    space = [' ']
    if len(zipcode) == 6:
        if not any(char in space for char in zipcode):
            for input in splitstring:
                if input[4].isalpha() and input[5].isalpha():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def checkstreetNameIndex(streetName):
    space = [' ']
    if len(streetName)< 50 and len(streetName)>= 1:
        if any(char.isalpha() for char in streetName):
            if not any(char in space for char in streetName):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def CheckPhoneNumberIndex(phoneNumber):
    space = [' ']
    if len(phoneNumber) == 8:
        if any(char.isdigit() for char in phoneNumber):
            if not any(char in space for char in phoneNumber):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def checkEmailIndex(email):
    SpecialSym = ['~', '!', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '`', '|', '(', ')', '{', '}', '[',
                  ']', ':', ';', '<', '>', '?', '/', "'", "\\"]
    Apenstaart = ['@']
    Dot = ['.']
    space = [' ']
    if any(char in Apenstaart for char in email):
        if any(char in Dot for char in email):
            if not any(char in space for char in email):
                if not any(char in SpecialSym for char in email):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def pasval(password):
    SpecialSym = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '`', '|', '(', ')', '{', '}', '[',
                  ']', ':', ';', '<', '>', '?', '/', '.', "'", "\\"]
    spatie = [' ']
    if len(password) >= 8 and len(password) <= 30:
        if any(char in SpecialSym for char in password):
            if any(char.isupper() for char in password):
                if any(char.islower() for char in password):
                    if not any(char in spatie for char in password):
                        print("it works")
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        print("ERROR")
        return False


def checkPasswordIndex(password):
    SpecialSym = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '`', '|', '(', ')', '{', '}', '[',
                  ']', ':', ';', '<', '>', '?', '/', '.', "'", "\\"]
    spatie = [' ']
    if len(password) >= 8 and len(password) <= 30:
        if any(char in SpecialSym for char in password):
            if any(char.isupper() for char in password):
                if any(char.islower() for char in password):
                    if not any(char in spatie for char in password):
                        print("it works")
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        print("ERROR")
        return False


def checkuserAdmin(username):
    specialSym = ['-', '_', "'", '.']
    spatie = [' ']

    splitstring = username.split()

    for input in splitstring:
        if input[0].isalpha():
            if len(username) >= 5 and len(username) <= 20:
                if any(char.isdigit() for char in username):
                    if any(char in specialSym for char in username):
                        if not any(char in spatie for char in username):
                            print("User name it works")
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def userval(username):
    global rootUsername
    global validation

    specialSym = ['-', '_',"'",'.']
    spatie = [' ']

    filename = 'userdata.txt'

    splitstring = username.split()
    if os.path.exists(filename):
        with open("userdata.txt", "r") as a_file:
            for line in a_file:
                stripped_line = line.strip()
                # print(decrypt(stripped_line))
                li = decrypt(stripped_line).split(" ")
                if li[0] == username:
                    return False
    
    for input in splitstring:
        if input[0].isalpha():
            if len(username) >= 5 and len(username) <= 20:
                if any(char.isdigit() for char in username):
                    if any(char in specialSym for char in username):
                        if not any(char in spatie for char in username):
                            print("User name it works")
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
<<<<<<< master
        return False
        # return validation == False

def log(error):
    encryptLog("["+str(datetime.now())+"]: " + error)
       

def openLog():
    filename = 'log.txt'

    if os.path.exists(filename):
        with open("log.txt", "r") as a_file:
            for line in a_file:
                print(decrypt(line))
    else:
        print("No Log")

logincounter = 0

=======
       return False


def log(error):
    filename = 'log.txt'

    if os.path.exists(filename):
        append_write = 'a'
    else:
        append_write = 'w'
    f = open(filename, append_write)
    f.write("["+str(datetime.now())+"]: " + error + "\n")
    f.close()

>>>>>>> Allevalidaties van klant
while True:
    if loginState == False:
        while True:
            login1 = input("Login:")
            login2 = input("Password:")
            # Login as hardcoded root user
            if (login1 == rootUsername and login2 == rootPassword):
                loginAsRoot(login1)
                loginState = True
                logincounter = 0
                break

            # Log in as normal user
            # check if user exists
            result = decrypt_all(login1, login2)
            if result == True:
                currentUser = login1
                loginState = True
                logincounter = 0
                break
            else:
                print("Wrong Login")
<<<<<<< master
                logincounter += 1
                if logincounter >= 3:
                    log("Username:" + login1 + "::" + "Password:" + login2)
=======
                log(login1 + ":" + login2)
>>>>>>> Allevalidaties van klant
                break

    elif loginState == True:
        print("Welcome: " + currentUser + " User Role: " + currentRole + " LoginState: " + str(loginState))

        while True:
            if currentRole == "root":
                while True:
                    rootInput = input("Create System Admin | Open Logfile | Logout (c/o/l): ")
                    if rootInput == "c":
                        while True:
                            username = input("Enter a username:")
                            validation = userval(username)
                            try:
                                if validation == True:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Username wrong or already exists")
                        while True:
                            password = input("Enter a password:")
                            validationPass = pasval(password)
                            try:
                                if validationPass == True:
                                    password1 = input("Confirm password:")
                                    try:
                                        if password == password1:
                                            createUser("System-Administrator")
                                            print("User Created")
                                            break
                                        else:
                                            raise ValueError
                                    except ValueError:
                                        print("Password not the same")
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Password wrong")
                                log(password)
<<<<<<< master
                    elif rootInput == "o":
                        openLog()
                        rootInput
=======


>>>>>>> Allevalidaties van klant
                    elif rootInput == "l":
                        logout()
                        break
                    else:
                        rootInput

<<<<<<< master
=======

>>>>>>> Allevalidaties van klant
            elif currentRole == "System-Administrator":
                while True:
                    systemAdminInput = input("Create Advisor | New Client | Logout (c/n/l): ")
                    if systemAdminInput == "c":
                        while True:
                            username = input("Enter a username:")
                            checkUserNameAdmin = checkuserAdmin(username)
                            try:
                                if checkUserNameAdmin == True:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Error")

                        while True:
                            password = input("Enter a password:")
                            checkPassword = checkPasswordIndex(password)
                            try:
                                if checkPassword == True:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Error")

                        password1 = input("Confirm password:")
                        if password == password1:
                            createUser("Advisor")
                            break
                        print("Passwords do NOT match!")
                    elif systemAdminInput == "n":
                        while True:
                            firstName = input("Enter a First Name:")
                            checkName = checkNameIndex(firstName)
                            try:
                                if checkName == True:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Error")

                        while True:
                            lastName = input("Enter a Last Name:")
                            checkLastName = checkLastnameIndex(lastName)
                            try:
                                if checkLastName == True:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Error")

                        while True:
                            houseNumber = input("Enter a House Number:")
                            checkHouseNumber = checkHouseNumberIndex(houseNumber)
                            try:
                                if checkHouseNumber == True:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Error")

                        while True:
                            zipcode = input("Enter a Zip Code:")
                            checkZipCode = checkzipIndex(zipcode)
                            try:
                                if checkZipCode == True:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Error")


                        while True:
                            streetName = input("Enter a Street:")
                            checkStreetName= checkstreetNameIndex(streetName)
                            try:
                                if checkStreetName == True:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Error")

                        while True:
                            printCity()
                            cityName = input("Enter a City:")
                            checkIndex = checkCityIndex(cityName)
                            try:
                                if checkIndex == True:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Error")

                        while True:
                            email  = input("Enter an Email:")
                            checkEmail = checkEmailIndex(email)
                            try:
                                if checkEmail == True:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Error")

                        while True:
                            phoneNumber = input("Enter a Phone Number:")
                            checkPhoneNumber = CheckPhoneNumberIndex(phoneNumber)
                            try:
                                if checkPhoneNumber == True:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Error")
                        createClient(firstName, lastName, streetName, houseNumber, zipcode, city[int(cityName)],
                                     email, phoneNumber)
                        break
                    elif systemAdminInput == "l":
                        logout()
                        break
                    else:
                        systemAdminInput

            elif currentRole == "Advisor":
                while True:
                    AdvisorInput = input("Find user info | Logout (f/l)")
                    if AdvisorInput == ("l"):
                        logout()
                        break
                    elif AdvisorInput == ("f"):
                        while True:
                            user = input("From which user do you want the info?: ")
                            getUser = getUserInfo(user)
                            try:
                                if getUser == "No User":
                                    raise ValueError
                                else:
                                    break
                            except ValueError:
                                print("No User")
                        print(getUser)
                        AdvisorInput
                    else:
                        AdvisorInput

            else:
                break

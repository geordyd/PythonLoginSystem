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


def decrypt(data):
    decrypt = ''

    for i in data:
        pos = alphabet.find(i)
        newpos = (pos - key) % len(alphabet)
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


def pasval(password):
    global rootPassword
    global validationPass

    if len(password) >= 5 and len(password) <= 20:
        print("it works")
        return True
    else:
        print("ERROR")
        return False


def userval(username):
    global rootUsername
    global validation

    # SpecialSym = ['~','!','@','#','$','%','^', '&','*','_','-','+','=','`','|','(',')','{','}','[',']',':',';','<', '>','.','?','/','.', "'", "\\"]
    specialSym = ['-', '_',"'",'.']

    splitstring = username.split()

    for input in splitstring:
        if input[0].isalpha():
            if len(username) >= 5 and len(username) <= 20:
                if any(char.isdigit() for char in username):
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
        # return validation == False


while True:

    if loginState == False:
        while True:
            login1 = input("Login:")
            login2 = input("Password:")
            # Login as hardcoded root user
            if (login1 == rootUsername and login2 == rootPassword):
                loginAsRoot(login1)
                loginState = True
                break

            # Log in as normal user
            # check if user exists
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
                    rootInput = input("Create System Admin | Logout (c/l): ")
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
                                print("Username wrong")
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



                        #     username = input("Enter a username:")
                        # # Julia validation
                        #     validation = userval(username)
                        #     try:
                        #         if validation == True:
                        #             while True:
                        #                 password = input("Enter a password:")
                        #                 validationPass = pasval(password)
                        #                 try:
                        #                     if validationPass == True:
                        #                         print("Login Worked, Hello")
                        #                         try:
                        #                             password1 = input("Confirm password:")
                        #                             if password == password1:
                        #                                 createUser("System-Administrator")
                        #                                 break
                        #                             else:
                        #                                 print("Passwords do NOT match!")
                        #                                 raise ValueError
                        #                         except ValueError:
                        #                             print("Errrrrrooooooorrrrrrr")

                        #                     else:
                        #                         raise ValueError
                        #                 except ValueError:
                        #                     print("Error")
                        #             # else:
                        #         #     print("ERRORSERS")
                        #         #     password
                        #         else:
                        #             # print("Error at username")
                        #             raise ValueError
                        #     except ValueError:
                        #         print("error")

                    elif rootInput == "l":
                        logout()
                        break
                    else:
                        rootInput

                        # Julia validation
                        # validation = userval(username)
                        # if validation == True:
                        #     password  = input("Enter a password:")
                        #     password1 = input("Confirm password:")
                        # else:
                        #     print("Error")
                        #     username
                    #     password  = input("Enter a password:")
                    #     password1 = input("Confirm password:")
                    #     if password == password1:
                    #         createUser("System-Administrator")
                    #         break
                    #     print("Passwords do NOT match!")
                    # elif rootInput == "l":
                    #     logout()
                    #     break
                    # else:
                    #     rootInput

            elif currentRole == "System-Administrator":
                while True:
                    systemAdminInput = input("Create Advisor | New Client | Logout (c/n/l): ")
                    if systemAdminInput == "c":
                        username = input("Enter a username:")
                        password = input("Enter a password:")
                        password1 = input("Confirm password:")
                        if password == password1:
                            createUser("Advisor")
                            break
                        print("Passwords do NOT match!")
                    elif systemAdminInput == "n":
                        firstName = input("Enter a First Name:")
                        lastName = input("Enter a Last Name:")
                        houseNumber  = input("Enter a House Number:")
                        zipcode = input("Enter a Zip Code:")
                        streetName = input("Enter a Street:")
                        printCity()
                        while True:
                            cityName = input("Enter a City:")
                            checkIndex = checkCityIndex(cityName)
                            try:
                                if checkIndex == True:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Error")
                        email  = input("Enter an Email:")
                        phoneNumber = input("Enter a Phone Number:")
                        createClient(firstName, lastName, streetName, houseNumber, zipcode, city[int(cityName)], email, phoneNumber)
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

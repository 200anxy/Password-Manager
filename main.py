import pyinputplus as pyip
import hashlib

signedIn = False
signInAttempts = 0

def shahash(string):
    hash = hashlib.sha256(text.encode('UTF-8')).hexdigest()
    return hash



def signin():
    userpass = open("usernames_pass.txt","a+")
    print('Starting password check... ')
    print('You can either (C)reate a new account, (S)ign in with an existing account, or (Q)uit.')

    start_choice = pyip.inputChoice(["c","s","q"])

    if start_choice.lower().strip()  == "c":
        print("You have chose to: Create a new account.")
        NewUsername = pyip.inputStr("Please input your Username: ")
        #Creating new account
        passwordverSuccess = False
        while passwordverSuccess != True:
            NewPassword = shahash(pyip.inputPassword("Please input your Password: "))
            NewPasswordVer = shahash(pyip.inputPassword("Please input your Password again: "))
            if NewPassword == NewPasswordVer:
                print("Password verification success")
                print("Saving Now...")
                passwordverSuccess == True
                userpass.write(NewUsername +":"+NewPassword+ "\n")
                userpass.close()
                print("Closing the program now...")
                print("Please sign in with your new credentials on a new instance.\nThanks!")
                quit()

    elif start_choice.lower().strip() == "s":
        print("You have chosen to : Sign in with an existing account")
        while signedIn == False and signInAttempts > 3:
            signUser = pyip.inputStr("Please input your Username: ")
            signPass = shahash(pyip.inputPassword("Please input your Password: "))
            checksign = signUser + ":" + signPass
            file_fullread = userpass.read()
            if checksign in file_fullread:
                print("Signed In!")
                signedIn = True
                return signedIn
            
            else:
                print("Sorry, the credentials that you have put in do not work.")
                signInAttempts += 1
                continue
        print("You have logged in with incorrect credentials too many times. Please try again later.")
        userpass.close()
        exit()    


    elif start_choice.lower().strip() == "q":
        print("You have chose to: Quit")
        print("The program is exiting...")
        quit()
    userpass.close()

signin()


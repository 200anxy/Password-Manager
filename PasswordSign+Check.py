import pyinputplus as pyip
# import hashlib



def signin():# from cryptography.fernet import Fernet
    userpass = open("1DatabasePy23//usernames_pass.txt","a+")
    print("Welcome to DatabasePy23")
    print("Here you can create an account and store your contacts")
    print("Your credentials are then encrypted for safety")
    print("Please choose (c) for creating a new account")
    print("Please chooose (s) for signing in with an existing one")
    print("And if you want to quit, choose (q)")

    start_choice = pyip.inputChoice(["c","s","q"])

    if start_choice.lower().strip()  == "c":
        print("You have chose to : Create a new account")
        NewUsername = pyip.inputStr("Please input your Username: ")
        #Creating new account
        passwordverSuccess = False
        while passwordverSuccess != True:
            NewPassword = pyip.inputPassword("Please input your Password: ")
            NewPasswordVer = pyip.inputPassword("Please input your Password again: ")
            if NewPassword == NewPasswordVer:
                print("Password verification Success")
                print("Saving Now")
                passwordverSuccess == True
                userpass.write(NewUsername +":"+NewPassword+ "\n")
                userpass.close()
                print("Closing the program now")
                print("Please sign in with your new credentials on a new instance")
                quit()

    elif start_choice.lower().strip() == "s":
        print("You have chosen to : Sign in with an existing account")
        #Signing in with existing account
        signUser = pyip.inputStr("Please input your Username: ")
        signPass = pyip.inputPassword("Please input your Password: ")
        checksign = signUser + ":" + signPass
        # print(checksign)
        userpass.seek(0)
        file_fullread = userpass.read()
        # print(file_fullread)
        if checksign in file_fullread:
            print("Signed In!")
            print("What would you like to do today?")
            print("Please choose from:")
            print("(c)reate new contact", "(s)how all contacts, (d)elete a contact or s(e)arch for a contact")
            print("Or you can choose (q) for quit")
            
            # if cShow == "q":
            #     print("Thank You")
            #     print("Quitting Program Now!")
            #     quit()
            # elif cShow == "r":
        else:
            print("Sorry, the credentials that you have put in do not work")
            quit()


    elif start_choice.lower().strip() == "q":
        print("You have chose to : Quit")
        print("The program has been exited")
        #Quitting the program
        quit()
    # print("YAY")
    userpass.close()
signin()

import hashlib
import pyinputplus as pyip


signedIn = False
signInAttempts = 0
userpass = open("usernames_pass.txt","a+", encoding='UTF-8')

def shahash(string):
    digest = hashlib.sha256(string.encode('UTF-8')).hexdigest()
    return digest
def signIn():
    global signedIn,signInAttempts
    while signedIn == False and signInAttempts < 3:
        signUser = pyip.inputStr("Please input your username: ")
        signPass = shahash(pyip.inputPassword("Please input your Password: "))
        checksign = signUser + ":" + signPass
        userpass.seek(0)
        file_fullread = userpass.read()
        if checksign in file_fullread:
            print("Signed in!")
            signedIn = True
            return signedIn
        else:
            print("Sorry, the credentials that you have put in do not work.")
            signInAttempts += 1
            continue
    print('''You have logged in with incorrect credentials too many times. 
        Please try again later.''')   
    userpass.close()
    return signedIn
 
def createAccount():
    print("You have chose to: Create a new account.")
    NewUsername = pyip.inputStr("Please input your Username: ")
    passwordverSuccess = False
    while passwordverSuccess != True:
        NewPassword = shahash(pyip.inputPassword("Please input your Password: "))
        NewPasswordVer = shahash(pyip.inputPassword("Please input your Password again: "))
        if NewPassword == NewPasswordVer:
            print("Password verification success")
            print("Saving Now...")
            passwordverSuccess = True
            userpass.write(NewUsername +":"+NewPassword+ "\n")
            userpass.close()
            print("Closing the program now...")
            print("Please sign in with your new credentials on a new instance.\nThanks!")
            return True

if __name__ == '__main__':
    print('This program is meant to be imported as a module.')
    print('Please open a new program and import this.')
    print('Thanks!\nExiting...')
    exit()

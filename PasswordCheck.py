## This Program uses python to create a password verification system using SHA256
## The program accepts the password, hashes it, and compares it with the file passwords.txt
from getpass import getpass
from hashlib import sha256
line = 0
try:
  fileCheck = open("passwords.txt","r")
except:
  print("passwords.txt does not exist. Please check and/or rename the file.\nThanks!")
  exit()
print("Welcome to Password Check!")
name = input("Please enter your name: ")
print("Checking if name exists in database...")
with open("passwords.txt") as Passwords:
  linesList = Passwords.readlines()
  for i in range(1,len(linesList - 2)):
    checkStr = linesList[i+2]
    if name.lower() in checkStr:
      line = i
      break
    else:
      print("Your name does not exist in the database. Please try again later. \nThanks!")
      exit()
  print("Name verified!")
  Password = getpass("Please enter your password.")
  print("Verifing password...")
  passwordHash = sha256(Password.encode('utf-8')).hexdigest()
  passwordCheck = lineList[line]
  padLen = int(len(name)) + 3
  passwordCheck = passwordCheck[padLen:]
  passwordCheck = passwordCheck[:-1]
  if passwordHash == str(passwordCheck):
    print("Password verified!")
    exit()
  else:
    print("Wrong password, please try again. \nThanks!")
    exit()
  
    

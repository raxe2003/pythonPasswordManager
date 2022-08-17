from operator import truediv
import colorama
from colorama import Fore
import os
import time
import sys
from hash import hashPassword as hp
from addNewPasswords import addPasswords as addPass
from readAllPasswords import readAll as ra
from clearEverything import clearEverything as ca
from checkOs import getOs

os = getOs()


def clear():
    os.system("clear")

goodEnoughStr = "is this right (y/n): "

def mainMenu():
    os.system("clear")
    
    print(Fore.YELLOW+"PasswordManager")
    print(" ")
    print(" ")
    print(Fore.GREEN+"(1) "+Fore.RED+"add new password")
    print(Fore.GREEN+"(2) "+Fore.RED+"read all passwords")
    print(Fore.GREEN+"(3) "+Fore.RED+"clear everything")
    print(Fore.GREEN+"(4) "+Fore.RED+"exit program")
    mainMenuSelect = int(input("type menu number: "))
    goBack = mainMenu


    if mainMenuSelect == 1:
        passwords = open("passwords", 'a')
        addPass(passwords, goBack)
    elif mainMenuSelect == 2:
        passwords = open("passwords",'r')
        ra(passwords, goBack)
    elif mainMenuSelect == 3:
        ca(goBack)
    elif mainMenuSelect == 4:
        print(Fore.LIGHTGREEN_EX+"good byee! =)")
        sys.exit()
    else:
        sys.exit(Fore.RED+"LOL")


#addPasswrods
# def addPasswords():
#     clear()
#     passwrodsFile = open("passwords",'a')
#     nup(passwrodsFile,"userName")
#     clear()
#     newUsernamePasswrod(passwrodsFile, "password")
#     clear()
#     print(Fore.BLUE+"your new username/passwrd has been added")
#     time.sleep(0.9)
#     print("going to main menu")
#     time.sleep(3)
#     mainMenu()

def funcRedoName(userName1, redoName1,passwordsFile):
    print(Fore.BLUE+"Let's try it again")
    time.sleep(0.5)
    userName1 = input(Fore.CYAN+"what will your name be: ?")
    redoName1 = input(Fore.CYAN+"if you want to change your name press 'y' if you are fine with it press 'n': " )
    if redoName1 == "y":
        funcRedoName(userName1, redoName1)
    elif redoName1 == "n":
        passwordsFile.writelines("userName: "+userName1)
        passwordsFile.close()
        print("great let's keep on going")
        time.sleep(1)
        print("you are about to go to mainMenu")
        time.sleep(3)
        mainMenu()

    else:
        os.system("clear")
        sys.exit(Fore.RED+"Learn to press keys")
print(Fore.RED+"this is advanced password manager")
time.sleep(2)
print("let me check if you used this program before")
time.sleep(5)

if os.path.exists("passwords"):
    os.system("clear")
    print(Fore.GREEN + "I found your old passwords file")
    print("lets go to main menu")
    time.sleep(5)
    mainMenu()
else:
    print("I think you are new user")
    print("It might be that you moved or deleted your old passwords file")
    time.sleep(1)
    print("but as much as I'm conserned you are new user")
    time.sleep(0.5)
    print(Fore.GREEN+"welcome abroad =)")
    time.sleep(10)
    os.system("clear")
    passwords = open("passwords", 'x')
    print(Fore.GREEN+"Let's first start with your name")
    userName = input(Fore.CYAN + "what is your name? :  ")
    time.sleep(2)
    print("I like your name, are you sure you want it to be that")
    redoName = input(Fore.CYAN+"if you want to change your name press 'y' if you are fine with it press 'n': " )
    if redoName == "y":
        funcRedoName(userName,redoName,passwords)

    elif redoName == "n":
        passwords.write("userName: "+userName)
        passwords.close()
        print("that is fine by me, let's keep going")
        time.sleep(0.7)
        print("you are about to go to main menu")
        time.sleep(0.7)
        print(Fore.GREEN+"when you get there you will understand everything don't wory")
        time.sleep(3)
        mainMenu()
    else:
        os.system("clear")
        sys.exit(Fore.RED+"Learn to press keys")

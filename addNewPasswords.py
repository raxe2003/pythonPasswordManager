from base64 import encode
import bcrypt
from colorama import Fore
import os
import time
import sys
from hash import hashPassword as hp
goodEnoughStr = "is this right (y/n): "


def clear():
    os.system("clear")

def newUserNamePassword(passwordFile, type):
    if type == "userName":
        newName = input(Fore.CYAN+"what is your new userName: ")
        isGood = False
        while isGood == False:
            os.system("clear")
            isRight = input(Fore.CYAN+goodEnoughStr)
            if isRight == "y":
                isGood = True
                passwordFile.write("\n")
                passwordFile.write("userName: "+newName)
            elif isRight == "n":
                newUserNamePassword(passwordFile, "userName")
            else:
                sys.exit(Fore.RED+"LOL")
    elif type == "password":
        newPassword = input(Fore.CYAN+"and what is the passwrod: ")
        isGood = False
        while isGood == False:
            os.system("clear")
            isRight = input(Fore.CYAN+goodEnoughStr)
            if isRight == "y":
                isGood = True
                # passwordFile.write("     passwrod: "+str(hp(newPassword)))
                passwordFile.write("     password: "+str(newPassword))

            elif isRight == "n":
                newUserNamePassword(passwordFile, "password")
            else:
                sys.exit(Fore.RED+"LOL")





def addPasswords(passwrodsFile, mainMenu ):
    clear()
    passwrodsFile = open("passwords",'a')
    newUserNamePassword(passwrodsFile,"userName")
    clear()
    newUserNamePassword(passwrodsFile, "password")
    clear()
    print(Fore.BLUE+"your new username/passwrd has been added")
    time.sleep(0.9)
    print("going to main menu")
    time.sleep(3)
    mainMenu()
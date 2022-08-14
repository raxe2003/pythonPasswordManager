from base64 import encode
import sys
import bcrypt
from colorama import Fore
import os
import time

def readAll(passwordList,mm):
    os.system('clear')
    wholeList = passwordList.read()
    print(wholeList)
    goBack = input("(type \"q\" to go to main menu: ")
    if goBack == "q":
        os.system("clear")
        print("going back in")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        mm()
    else:
        os.system("clear")
        print("Im guessing you wanted to go back")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        mm()
    


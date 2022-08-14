from base64 import encode
import bcrypt
from colorama import Fore
import os
import time

def clearEverything(mm):
    os.system('clear')
    print("this will clear all of your passwrods")
    print("are you sure you wanna procede with this")
    answer = input("y/n: ")
    if answer == "y":
        print("are you realy sure?")
        answer = input("y/n: ")
        if answer == "y":
            passwordList = open("passwords",'w')
            passwordList.write(" ")
            mm()
        else:
            mm()
    else:
        mm()

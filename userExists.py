import os
from turtle import Turtle

def userAlreadyExists(file):
    if os.path.exists(file):
        return True
    else:
        return False
        
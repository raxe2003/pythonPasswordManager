import os

def userAlreadyExists(file):
    if os.path.exists(file):
        return True
    else:
        return False

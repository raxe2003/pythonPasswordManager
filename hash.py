from base64 import encode
import os


def hashPassword(password):
    salt = bcrypt.gensalt()
    hashPass = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashPass



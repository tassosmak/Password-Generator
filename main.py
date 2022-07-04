import string
from random import random, shuffle, choice

#characters = list(string.ascii_lowercase, string.ascii_uppercase, string.digits, + "!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def gen():

    length = int(input("How long do you want your password to be:"))



    shuffle(characters)

    password = []
    for i in range(length):
        password.append(choice(characters))

    print("".join(password))

gen()
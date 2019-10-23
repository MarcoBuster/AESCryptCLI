import string
import random


def random_letter():
    return random.choice(string.ascii_lowercase)


def random_ext():
    ext = str(".")
    for i in range(3):
        ext = ext + str(random_letter())
    return ext


def remove_ext(file):
    return file[:-4]


def add_ext(file):
    return file + random_ext()

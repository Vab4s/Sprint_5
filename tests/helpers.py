import string
import random

def login_generator():
    login = ''
    for symbol in range(random.randint(1, 15)):
        symbol = (string.ascii_letters + string.digits)[
            random.randint(0, len(string.ascii_letters + string.digits) - 1)]
        login = login + symbol
    login = login + '@ya.ru'
    return login


def password_generator():
    password = ''
    for symbol in range(random.randint(6, 30)):
        symbol = (string.ascii_letters + string.digits)[
            random.randint(0, len(string.ascii_letters + string.digits) - 1)]
        password = password + symbol
    return password

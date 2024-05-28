import string
import random
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1440,900")
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture
def login_generator():
    login = ''
    for symbol in range(random.randint(1, 15)):
        symbol = (string.ascii_letters + string.digits)[
            random.randint(0, len(string.ascii_letters + string.digits) - 1)]
        login = login + symbol
    login = login + '@ya.ru'
    return login


@pytest.fixture
def password_generator():
    password = ''
    for symbol in range(random.randint(6, 30)):
        symbol = (string.ascii_letters + string.digits)[
            random.randint(0, len(string.ascii_letters + string.digits) - 1)]
        password = password + symbol
    return password

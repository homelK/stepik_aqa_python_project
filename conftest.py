import pytest
import time
from selenium import webdriver
import random


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en", help="choose a preferable language for a browser"
    )

@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("--language")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"--lang={browser_language}")
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(chrome_options)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def email_generator():
    return str(time.time()) + "@fakemail.org"

@pytest.fixture(scope="function")
def passw_generator():
    characters = ["1", "g", "f", "d", "t", "!", "&", "?", "*", "F", "h", "#", "_"]
    password = ""

    for i in range(9):
        password += random.choice(characters)

    return password
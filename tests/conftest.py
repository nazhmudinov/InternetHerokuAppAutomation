import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup_and_teardown(request):
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    """“request” is a pytest built-in fixture. with request.cls.driver = web_driver, any class use this fixture will 
get an attribute driver automatically."""
    request.cls.driver = driver
    driver.get('https://the-internet.herokuapp.com/')

    yield
    driver.close()

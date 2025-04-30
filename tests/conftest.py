import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(scope="function")
def browser():
    print('into sel start')
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    print("Initialize driver.....")
    driver.maximize_window()
#    self.driver = driver
#    return driver
#    driver = seleniumCommon().selenium_start()
    yield driver
    print("into selenium end")
    driver.quit()
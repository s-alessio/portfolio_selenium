import pytest
from helper.selenium_common import seleniumCommon

@pytest.fixture
def sc():
    print("utils called")
    return seleniumCommon().selenium_start()

@pytest.fixture(scope="function")
def browser():
    driver = seleniumCommon().selenium_start()
    yield driver
    print("into selenium end")
    driver.quit()
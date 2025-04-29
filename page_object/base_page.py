from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)

    def open(self):
        try:
            self.browser.get(self.url)
        except:
            assert 1==2, "Cannot open page "+self.url

    def is_element_exists(self,driver,loctype, loc):
        try:
            driver.find_element(loctype,loc)
            return True
        except:
            return False

    def is_element_clickable(self,driver,loctype,loc):
        try:
            msg = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((loctype, loc)))
            return True
        except TimeoutException:
            raise TimeoutException(f"{loctype} {loc} is still not clickable")



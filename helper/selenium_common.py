from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class seleniumCommon():

    def selenium_start(self):
        print('into sel start')
        options = Options()
        options.headless = False
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print("Initialize driver.....")
        driver.maximize_window()
        self.driver=driver
        return driver





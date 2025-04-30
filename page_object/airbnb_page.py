from .base_page import BasePage
from .locators import AirBnbLocators
from selenium.webdriver.common.keys import Keys
import time
import re

class AirbnbPage(BasePage):

    def accept_cookies(self):
        self.is_element_clickable(self.browser,*AirBnbLocators.cookie_buttons)
        cbuttons = self.browser.find_elements(*AirBnbLocators.cookie_buttons)
        for cb in cbuttons:
            if cb.text == "Only necessary":
                cb.click()

    def set_max_price(self,max_price):
        assert self.is_element_clickable(self.browser, *AirBnbLocators.filter_button), "Filters button not found or not clickable"
        self.browser.find_element(*AirBnbLocators.filter_button).click()

        assert self.is_element_clickable(self.browser, *AirBnbLocators.price_filter_max), "Field for max price not found or not clickable"
        for i in range(6):
            self.browser.find_element(*AirBnbLocators.price_filter_max).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*AirBnbLocators.price_filter_max).send_keys(max_price)
        self.browser.find_element(*AirBnbLocators.commit_filters_button).click()

    def set_location(self,location):
        assert self.is_element_clickable(self.browser, *AirBnbLocators.where_field), "/Where/ field not found or not clickable"
        where = self.browser.find_element(*AirBnbLocators.where_field)
        where.click()
        where.send_keys(location)

    def set_period(self):
        assert self.is_element_clickable(self.browser, *AirBnbLocators.check_in_field), "/Check in/ field not found or not clickable"
        check_in = self.browser.find_element(*AirBnbLocators.check_in_field)
        check_in.click()
        assert self.is_element_clickable(self.browser, *AirBnbLocators.flexible_tab), "/Flexible/ tab not found or not clickable"
        self.browser.find_element(*AirBnbLocators.flexible_tab).click()
        assert self.is_element_clickable(self.browser, *AirBnbLocators.weekend), "/Weekend/ tab not found or not clickable"
        self.browser.find_element(*AirBnbLocators.weekend).click()
        assert self.is_element_clickable(self.browser, *AirBnbLocators.months_carousel), "Months not found or not clickable"
        months = self.browser.find_elements(*AirBnbLocators.months_carousel)
        assert len(months) > 5, "Not enough months found:" + str(len(months))
        self.browser.find_elements(*AirBnbLocators.months_carousel)[1].click()


    def find_accomodation(self):
        assert self.is_element_clickable(self.browser, *AirBnbLocators.search_button), "Search button not found or clickable"
        self.browser.find_element(*AirBnbLocators.search_button).click()
        time.sleep(5)

    def check_location(self,location):
        assert self.is_element_clickable(self.browser, *AirBnbLocators.selected_location)
        assert "Location\n" + location == self.browser.find_element(
            *AirBnbLocators.selected_location).text, "Displayed selected location doesn't match location required"

    def check_prices(self,max_price):
        i = 0
        assert self.is_element_clickable(self.browser, *AirBnbLocators.total_price), "Total prices not found"
        total_prices = self.browser.find_elements(*AirBnbLocators.total_price)
        for tp in total_prices:
            i += 1
            tp_text = tp.text
            match = re.search(r"(\d+)", tp_text)
            if match:
                # test stops when the first price that exceeds max_price is found
                assert int(match.group(1)) < max_price and int(
                    match.group(1)) > 0, "Incorrect total price: " + tp_text
            else:
                raise AssertionError("Total price not found: " + tp_text)

        assert i > 0, "No results with total price found"
import time
import re
import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys


# Looking for apartments in location
# For weekend
# In the next month
# Cheaper than maxprice per weekend
#
#
#
cookie_buttons = (By.CSS_SELECTOR,"section div button")

filter_button = (By.CSS_SELECTOR , "[data-testid='category-bar-filter-button']")
price_filter_max = (By.ID,"price_filter_max")
commit_filters_button = (By.CSS_SELECTOR,"div.p13966et")
anywhere = (By.CSS_SELECTOR, "[data-testid='little-search']")
where_field = (By.ID, "bigsearch-query-location-input")
check_in_field = (By.CSS_SELECTOR, "[data-testid='structured-search-input-field-split-dates-0']")
flexible_tab = (By.CSS_SELECTOR, "[data-testid='expanded-searchbar-dates-flexible-tab']")
months_carousel = (By.CSS_SELECTOR, "[data-testid='carousel-chip']")
weekend = (By.ID,"flexible_trip_lengths-weekend_trip")
search_button = (By.CSS_SELECTOR, "[data-testid='structured-search-input-search-button']")


selected_location = (By.CSS_SELECTOR, "[data-testid='little-search-location']")
selected_preiod = (By.CSS_SELECTOR, "[data-testid='little-search-anytime']")
appartments_cards = (By.CSS_SELECTOR, "[data-testid='card-container']")
total_price = (By.CSS_SELECTOR,"div._tt122m")



@pytest.mark.parametrize("location,max_price",[("Paris",100)])
def test_can_search_for_appartment(sc,location,max_price):
    driver = sc.selenium_start()
    driver.get("https://www.airbnb.co.uk/")
    #location = "Paris"
    #max_price = 100

    #time.sleep(10)

    # Click on cookie button
    cbuttons = driver.find_elements(*cookie_buttons)
    for cb in cbuttons:
        if cb.text == "Only necessary":
            cb.click()

    # Set max total price
    assert sc.is_element_clickable(driver,*filter_button), "Filters button not found or not clickable"
    driver.find_element(*filter_button).click()

    assert sc.is_element_clickable(driver,*price_filter_max), "Field for max price not found or not clickable"
    for i in range(6):
        driver.find_element(*price_filter_max).send_keys(Keys.BACKSPACE)
    driver.find_element(*price_filter_max).send_keys(max_price)
    driver.find_element(*commit_filters_button).click()


    # Set location
    assert sc.is_element_clickable(driver, *where_field), "/Where/ field not found or not clickable"
    where = driver.find_element(*where_field)
    where.click()
    where.send_keys(location)

    # Set period
    assert sc.is_element_clickable(driver,*check_in_field), "/Check in/ field not found or not clickable"
    check_in = driver.find_element(*check_in_field)
    check_in.click()
    assert sc.is_element_clickable(driver,*flexible_tab), "/Flexible/ tab not found or not clickable"
    driver.find_element(*flexible_tab).click()
    assert sc.is_element_clickable(driver,*weekend), "/Weekend/ tab not found or not clickable"
    driver.find_element(*weekend).click()
    assert sc.is_element_clickable(driver,*months_carousel), "Months not found or not clickable"
    months = driver.find_elements(*months_carousel)
    assert len(months)>5, "Not enough months found:" + str(len(months))
    driver.find_elements(*months_carousel)[1].click()

    # Search and wait
    assert sc.is_element_clickable(driver,*search_button), "Search button not found or clickable"
    driver.find_element(*search_button).click()
    #time.sleep(5)

    # Check that location is match required
    assert sc.is_element_clickable(driver,*selected_location)
    assert "Location\n"+location == driver.find_element(*selected_location).text, "Displayed selected location doesn't match location required"

    # Check prices
    i = 0
    assert sc.is_element_clickable(driver,*total_price), "Total prices not found"
    total_prices = driver.find_elements(*total_price)
    for tp in total_prices:
        i+=1
        tp_text = tp.text
        match = re.search(r"(\d+)", tp_text)
        # max_price+20 - because sometimes total price is slightly exceed max price set in filters
        if match:
            assert int(match.group(1)) < max_price+20 and int(match.group(1))>0, "Incorrect total price: "+tp_text
        else:
            assert 1==2, "Total price not found: "+tp_text

    assert i>0, "No results with total price found"
    #time.sleep(10)



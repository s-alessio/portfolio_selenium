from selenium.webdriver.common.by import By

class AirBnbLocators():
    cookie_buttons = (By.CSS_SELECTOR, "section > div > div > div > button")

    filter_button = (By.CSS_SELECTOR, "[data-testid='category-bar-filter-button']")
    price_filter_max = (By.ID, "price_filter_max")
    commit_filters_button = (By.CSS_SELECTOR, "div.p13966et")
    anywhere = (By.CSS_SELECTOR, "[data-testid='little-search']")
    where_field = (By.ID, "bigsearch-query-location-input")
    check_in_field = (By.CSS_SELECTOR, "[data-testid='structured-search-input-field-split-dates-0']")
    flexible_tab = (By.CSS_SELECTOR, "[data-testid='expanded-searchbar-dates-flexible-tab']")
    months_carousel = (By.CSS_SELECTOR, "[data-testid='carousel-chip']")
    weekend = (By.ID, "flexible_trip_lengths-weekend_trip")
    search_button = (By.CSS_SELECTOR, "[data-testid='structured-search-input-search-button']")

    selected_location = (By.CSS_SELECTOR, "[data-testid='little-search-location']")
    selected_preiod = (By.CSS_SELECTOR, "[data-testid='little-search-anytime']")
    appartments_cards = (By.CSS_SELECTOR, "[data-testid='card-container']")
    total_price = (By.CSS_SELECTOR, "div._10d7v0r")
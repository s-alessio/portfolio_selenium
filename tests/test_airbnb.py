from page_object.airbnb_page import AirbnbPage
import pytest


@pytest.mark.parametrize("location,max_price",[("Paris",100)])
def test_can_search_for_appartment_in_next_month(browser,location,max_price):
    page = AirbnbPage(browser,"https://www.airbnb.co.uk/")
    page.open()

    # Click on cookie button
    page.accept_cookies()

    # Set max total price
    page.set_max_price(max_price)

    # Set location
    page.set_location(location)

    # Set period: flexible weekend in the next month
    page.set_period()

    # Search and wait
    page.find_accomodation()

    # Check that location is match required
    page.check_location(location)

    # Check prices
    page.check_prices(max_price)




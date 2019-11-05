from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_for_button(browser):
    browser.get(link)
    time.sleep(30)
    try:
        button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        print(f"button text = {button.text}")
    except NoSuchElementException:
        assert "button not found"

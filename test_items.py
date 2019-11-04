from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_for_button(browser):
    browser.get(link)
    # WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket")))
    time.sleep(30)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    button.click()

    try:
        button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        print(f"button text = {button.text}")
    except NoSuchElementException:
        assert "button not found"

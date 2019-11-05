from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_for_button(browser):
    browser.get(link)
    #time.sleep(30)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    print(f"button text = {button.text}")
    assert button == button.text, "button is not found"

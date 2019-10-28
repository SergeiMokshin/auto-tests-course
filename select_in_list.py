# Открыть страницу http://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"
# на странице http://suninjuly.github.io/selects2.html. Ваш код и для нее тоже ﻿должен пройти успешно.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = int(input("enter 1 or 2 : "))
if link == 1:
    link = "http://suninjuly.github.io/selects1.html"
else:
    link = "http://suninjuly.github.io/selects2.html"


def sum_arg(arg1, arg2):
    return str(int(arg1) + int(arg2))


try:
    browser = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(sum_arg(num1, num2))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()

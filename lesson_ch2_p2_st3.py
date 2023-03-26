from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    a = int(num1.text)
    num2 = browser.find_element(By.ID, "num2")
    b = int(num2.text)
    x = a + b
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(x)) 
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

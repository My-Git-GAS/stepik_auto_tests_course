from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR, "button")
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    cool = browser.find_element(By.ID, "input_value")
    x = int(cool.text)
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)   
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

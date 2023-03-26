from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 14).until (EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()
    #button1 = browser.find_element(By.CSS_SELECTOR, "button")
    #button1.click()
    cool = browser.find_element(By.ID, "input_value")
    x = int(cool.text)
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)   
    button1 = browser.find_element(By.ID, "solve")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    cool = browser.find_element(By.ID, "input_value")
    x = int(cool.text)
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    #button = browser.find_element(By.TAG_NAME, "button")
    #button2 = browser.find_element(By.ID, "peopleRule")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click() 
    input3 = browser.find_element(By.ID, "robotsRule")
    input3.click() 
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

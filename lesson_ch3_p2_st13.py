from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
      try: 
       link = "http://suninjuly.github.io/registration1.html"
       browser = webdriver.Chrome()
       browser.get(link)
       # Ваш код, который заполняет обязательные поля
       input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block>div.first_class>input")
       input1.send_keys("Ivan")
       input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block>div.second_class>input")
       input2.send_keys("Petrov")
       input6 = browser.find_element(By.CSS_SELECTOR, "div.first_block>div.third_class>input")
       input6.send_keys("Petrov@vanya")
       input3 = browser.find_element(By.CSS_SELECTOR, "div.second_block>div.first_class>input")
       input3.send_keys("Smolensk.phone")
       input4 = browser.find_element(By.CSS_SELECTOR, "div.second_block>div.second_class>input")
       input4.send_keys("Russia")
       # Отправляем заполненную форму
       button = browser.find_element(By.CSS_SELECTOR, "button.btn")
       button.click()
       # Проверяем, что смогли зарегистрироваться
       # ждем загрузки страницы
       time.sleep(1)
       # находим элемент, содержащий текст
       welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
       # записываем в переменную welcome_text текст из элемента welcome_text_elt
       welcome_text = welcome_text_elt.text
       # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
       self.assertEqual( "Congratulations! You have successfully registered!", welcome_text)

      finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


    def test_abs2(self):
      try: 
       link = "http://suninjuly.github.io/registration2.html"
       browser = webdriver.Chrome()
       browser.get(link)
       # Ваш код, который заполняет обязательные поля
       input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block>div.first_class>input")
       input1.send_keys("Ivan")
       input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block>div.second_class>input")
       input2.send_keys("Petrov")
       input6 = browser.find_element(By.CSS_SELECTOR, "div.first_block>div.third_class>input")
       input6.send_keys("Petrov@vanya")
       input3 = browser.find_element(By.CSS_SELECTOR, "div.second_block>div.first_class>input")
       input3.send_keys("Smolensk.phone")
       input4 = browser.find_element(By.CSS_SELECTOR, "div.second_block>div.second_class>input")
       input4.send_keys("Russia")
       # Отправляем заполненную форму
       button = browser.find_element(By.CSS_SELECTOR, "button.btn")
       button.click()
       # Проверяем, что смогли зарегистрироваться
       # ждем загрузки страницы
       time.sleep(1)
       # находим элемент, содержащий текст
       welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
       # записываем в переменную welcome_text текст из элемента welcome_text_elt
       welcome_text = welcome_text_elt.text
       # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
       self.assertEqual( "Congratulations! You have successfully registered!", welcome_text)

      finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()
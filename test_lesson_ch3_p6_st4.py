# import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

@pytest.mark.parametrize('linkes', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_abs1(linkes):
 try:
  browser = webdriver.Chrome()
  browser.implicitly_wait(40)
  link = f"https://stepik.org/lesson/{linkes}/step/1"
  browser.get(link)

  start_login = browser.find_element(By.ID, "ember33")
  start_login.click()
  login = browser.find_element(By.NAME, "login")
  login.send_keys("k1k1kak123456789@gmail.com")
  password = browser.find_element(By.NAME, "password")
  password.send_keys("Qazplm123")
  button = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
  button.click()
  time.sleep(10)
  input = browser.find_element(By.TAG_NAME, "textarea")
  answer = math.log(int(time.time()))
  input.send_keys(answer)
  button2 = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
  button2.click()
  correct_text_elt = browser.find_element(By.CSS_SELECTOR, "div > p").text
  assert 'Correct!' in correct_text_elt, f"нужный текст: {correct_text_elt}"
 finally:
  time.sleep(10)
  browser.quit()

if __name__ == "__main__":
    pytest.main()
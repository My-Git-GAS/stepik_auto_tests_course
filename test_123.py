import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def test_123():
   try:
       browser = webdriver.Chrome()
       browser.implicitly_wait(40)
       link = "https://docs.google.com/forms/d/e/1FAIpQLSdNV0yMD57WcHrMJSXQpU0wUg5v24ie7JO01O_72RhrREzvCg/viewform"
       browser.get(link)
       button = browser.find_element(By.CSS_SELECTOR, "#i8 > div.vd3tt > div")
       button.click()
       button1 = browser.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div > div.lRwqcd > div > span > span")
       button1.click()

       #browser.execute_script("window.scrollBy(0, 100);")
       button2 = browser.find_element(By.CSS_SELECTOR, "#i8 > div.vd3tt > div")
       button2.click()
       button3 = browser.find_element(By.CSS_SELECTOR, "#i24 > div.vd3tt > div")
       button3.click()
       browser.execute_script("window.scrollBy(0, 100);")
       button4 = browser.find_element(By.CSS_SELECTOR, "#i43 > div.vd3tt > div")
       button4.click()
       button5 = browser.find_element(By.CSS_SELECTOR,"#i62 > div.vd3tt > div")
       button5.click()
       browser.execute_script("window.scrollBy(0, 100);")
       button6 = browser.find_element(By.CSS_SELECTOR, "#i84 > div.vd3tt > div")
       button6.click()
       button7 = browser.find_element(By.CSS_SELECTOR, "#i94 > div.vd3tt > div")
       button7.click()
       browser.execute_script("window.scrollBy(0, 100);")
       button8 = browser.find_element(By.CSS_SELECTOR,"#i110 > div.vd3tt > div")
       button8.click()
       button9 = browser.find_element(By.CSS_SELECTOR, "#i126 > div.vd3tt > div")
       button9.click()
       button10 = browser.find_element(By.CSS_SELECTOR, "#i148 > div.vd3tt > div")
       button10.click()
       browser.execute_script("window.scrollBy(0, 100);")
       button11 = browser.find_element(By.CSS_SELECTOR,"#i164 > div.vd3tt > div")
       button11.click()
       button12 = browser.find_element(By.CSS_SELECTOR, "#i186 > div.vd3tt > div")
       button12.click()
       browser.execute_script("window.scrollBy(0, 100);")
       button13 = browser.find_element(By.CSS_SELECTOR, "#i208 > div.vd3tt > div")
       button13.click()
       button14 = browser.find_element(By.CSS_SELECTOR, "#i224 > div.vd3tt > div")
       button14.click()
       browser.execute_script("window.scrollBy(0, 100);")
       button15 = browser.find_element(By.CSS_SELECTOR, "#i237 > div.vd3tt > div")
       button15.click()
       button16 = browser.find_element(By.CSS_SELECTOR, "#i253 > div.vd3tt > div")
       button16.click()
       button_fin = browser.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div > div.lRwqcd > div.uArJ5e.UQuaGc.Y5sE8d.VkkpIf.QvWxOd.M9Bg4d")
       button_fin.click()
   finally:
       time.sleep(15)
       browser.quit()
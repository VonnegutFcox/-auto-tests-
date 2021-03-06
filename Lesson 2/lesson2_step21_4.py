from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/math.html')

    x_element = browser.find_element_by_id('input_value')
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(calc(x_element.text))
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("input[type='radio']#robotsRule")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()

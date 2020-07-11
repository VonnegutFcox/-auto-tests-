from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
  
    select = Select(browser.find_element_by_tag_name("select"))
    
    answer = int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text)

    select.select_by_value("{0}".format(answer))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()

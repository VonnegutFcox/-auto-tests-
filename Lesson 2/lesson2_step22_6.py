from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://SunInJuly.github.io/execute_script.html')

    x_element = browser.find_element_by_id('input_value')
    
    input_ = browser.find_element_by_id('answer')
    input_.send_keys(calc(x_element.text))
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()

    button.click()

    #чтение и вывод кода из JS.alert
    alert = browser.switch_to_alert()
    print(alert.text[80:])
finally:
    time.sleep(5)
    browser.quit()

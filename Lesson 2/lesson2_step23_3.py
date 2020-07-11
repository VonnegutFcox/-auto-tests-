from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    #Открыть страницу http://suninjuly.github.io/alert_accept.html
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #Нажать на кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    #Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    
    time.sleep(1)
    
    #На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = browser.find_element_by_id('input_value').text
    input = browser.find_element_by_id('answer')
    input.send_keys(calc(x))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    #чтение и вывод кода из JS.alert
    alert = browser.switch_to_alert()
    print(alert.text[79:])
    alert.accept()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

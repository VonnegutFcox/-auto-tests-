from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
    button_BOOK = browser.find_element_by_id("book")
    button_BOOK.click()
        
    #На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = browser.find_element_by_id('input_value').text
    input = browser.find_element_by_id('answer')
    input.send_keys(calc(x))
    button = browser.find_element_by_id("solve")
    button.click()
    
    #message = browser.find_element_by_id("verify_message")

    #чтение и вывод кода из JS.alert
    alert = browser.switch_to_alert()
    print(alert.text[79:])
    alert.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

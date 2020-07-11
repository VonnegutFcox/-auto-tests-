from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    elements = browser.find_elements_by_css_selector('input[type="text"][required]')
    for element in elements:  
        element.send_keys('test')

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    
    input_ = browser.find_element_by_id('file')
    
    # добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, 'file.txt')
    input_.send_keys(file_path)
  
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    #чтение и вывод кода из JS.alert
    alert = browser.switch_to.alert
    print(alert.text[80:])
finally:
    time.sleep(2)
    browser.quit()

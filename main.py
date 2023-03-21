import math
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import os




link = "http://suninjuly.github.io/explicit_wait2.html"
current_file = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_file, 'mistake_list.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)
    btn = browser.find_element(By.CSS_SELECTOR, '#book')
    WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100'))
    btn.click()
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    result = math.log(abs(12*math.sin(int(x))))
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(str(result))
    browser.find_element(By.XPATH, '//*[@type = "submit"]').click()
    browser.switch_to.alert

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла



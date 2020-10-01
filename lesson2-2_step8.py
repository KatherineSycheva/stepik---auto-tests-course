import os
from datetime import time

from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

inp1 = browser.find_element_by_name("firstname")
inp1.send_keys("A")
inp1 = browser.find_element_by_name("lastname")
inp1.send_keys("B")
inp1 = browser.find_element_by_name("email")
inp1.send_keys("C")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'new.txt')           # добавляем к этому пути имя файла
ff = browser.find_element_by_id("file")
ff.send_keys(file_path)

button = browser.find_element_by_tag_name("button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(5)
assert True
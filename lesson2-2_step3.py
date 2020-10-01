from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time



link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(int(num1)+int(num2)))  # ищем элемент с текстом "Python"

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
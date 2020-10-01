from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
link1 = "http://suninjuly.github.io/get_attribute.html"
try:
    browser = webdriver.Chrome()
    browser.get(link1)

    x_element = browser.find_element_by_tag_name("img")
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)

    ans = browser.find_element_by_id("answer")
    ans.send_keys(y)

    chb = browser.find_element_by_id("robotCheckbox")
    chb.click()

    rb = browser.find_element_by_id("robotsRule")
    rb.click()



    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
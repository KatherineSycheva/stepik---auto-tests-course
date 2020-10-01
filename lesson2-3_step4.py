from datetime import time
from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element_by_tag_name("button")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x = int(browser.find_element_by_id("input_value").text)
res = math.log(abs(12*math.sin(x)),math.e)
answer = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
answer.send_keys(str(res))
button = browser.find_element_by_tag_name("button")
button.click()
assert True




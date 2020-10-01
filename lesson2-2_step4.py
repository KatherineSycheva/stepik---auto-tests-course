from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

input_value = browser.find_element_by_id('input_value').text

#ln(abs(12*sin(x)))
res = math.log((abs((12*math.sin(int(input_value))))),math.e)

answer = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
answer.send_keys(str(res))
robot = browser.find_element_by_id("robotCheckbox")
robot.click()
rule = browser.find_element_by_id("robotsRule")
rule.click()

button = browser.find_element_by_tag_name("button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
assert True
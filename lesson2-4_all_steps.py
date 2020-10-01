import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = browser.find_element_by_id("book")
price = WebDriverWait(browser, 12).until(
        #EC.element_to_be_clickable((By.ID, "verify"))
        EC.text_to_be_present_in_element((By.ID,"price"), "$100")
    )
print(price)
button.click()

x = int(browser.find_element_by_id("input_value").text)
res = math.log(abs(12*math.sin(x)),math.e)
answer = browser.find_element_by_id("answer")

answer.send_keys(str(res))
button = browser.find_element_by_id("solve")
button.click()
assert True


#message = browser.find_element_by_id("verify_message")

#assert "successful" in message.text
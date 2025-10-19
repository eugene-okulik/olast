from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('start-maximized')

driver = webdriver.Chrome(options=options)
driver.get('https://www.qa-practice.com/elements/input/simple')

text_input = driver.find_element(By.NAME, 'text_string')
text_input.send_keys('text_1')
text_input.submit()

test_text = 'text_1'
search_input_text = driver.find_element(By.ID, 'result-text').text

assert test_text == search_input_text
print(search_input_text)

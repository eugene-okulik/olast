import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_choose_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')

    choose_language = driver.find_element(By.ID, 'id_choose_language')
    select = Select(choose_language)
    select.select_by_visible_text('Python')

    button_submit = driver.find_element(By.ID, 'submit-id-submit')
    button_submit.click()

    expected_text = driver.find_element(By.CLASS_NAME, "result-text").text

    assert "Python" in expected_text
    print(expected_text)


def test_hello(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
    start_button.click()
    expected_text = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']"))
    )
    assert expected_text.text == "Hello World!"

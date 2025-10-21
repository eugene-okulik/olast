from time import sleep
from selenium.webdriver.support import expected_conditions as ec, wait
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def shop(driver):
    driver.get('http://testshop.qa-practice.com/')
    return driver


def test_add_to_card(driver, shop):
    driver.implicitly_wait(2)
    item_desl = driver.find_element(By.XPATH, "//*[text()='Customizable Desk']")
    button_add_to_card = driver.find_element(By.XPATH, "//*[@class='o_wsale_product_btn'][1]")
    ActionChains(driver).move_to_element(item_desl).click(button_add_to_card).perform()
    sleep(3)

    product = driver.find_element(By.XPATH, "//*[@class='product-name product_display_name'][1]").text
    assert '[FURN_0096] Customizable Desk (Steel, White)' in product, \
        (f'Ожидался текст [FURN_0096] Customizable Desk (Steel, White),'
         f'но был получен {product}')
    print(product)

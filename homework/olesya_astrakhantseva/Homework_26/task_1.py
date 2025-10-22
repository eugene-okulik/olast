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


def test_open_in_new_tab(driver, shop):
    # Открытие товара в новой вкладке
    driver.implicitly_wait(2)

    link = driver.find_element(By.XPATH, "//*[text()='Customizable Desk']")
    print(driver.window_handles)
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # Добавление товара в корзину
    button_add = driver.find_element(By.XPATH, "//*[@id='add_to_cart']")
    button_add.click()

    # Нажатие на кнопку продолжения покупок
    button_continue = wait.until(
        ec.element_to_be_clickable(
            (By.XPATH, "//*[text()='Continue Shopping']")
        )
    )
    button_continue.click()
    sleep(2)

    # Закрытие вкладки с товаром и переключение на первую вкладку
    driver.close()
    driver.switch_to.window(tabs[0])

    buttom_shopping = driver.find_element(By.CSS_SELECTOR, "[aria-label='eCommerce cart']")
    buttom_shopping.click()

    item_in_card = driver.find_element(By.CLASS_NAME, 'flex-grow-1').text
    sleep(2)
    assert 'Customizable Desk (Steel, White)' in item_in_card
    print(item_in_card)

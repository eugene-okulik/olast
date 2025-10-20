import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def practice_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    return driver


def test_personal_info(driver):
    first_name = driver.find_element(By.ID, 'firstName')
    first_name.send_keys('Olesya')

    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys('Astraknatseva')

    email = driver.find_element(By.ID, 'userEmail')
    email.send_keys('test@mail.com')


def test_select_gender(driver):
    gender = driver.find_element(By.CLASS_NAME, 'custom-control-label')
    gender.click()


def test_fill_number(driver):
    mobile = driver.find_element(By.ID, 'userNumber')
    mobile.send_keys('79181111111')


def test_select_birth(driver):
    calendar = driver.find_element(By.ID, 'dateOfBirthInput')
    calendar.click()

    choose_month = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
    select = Select(choose_month)
    select.select_by_visible_text('July')

    choose_year = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
    driver.execute_script(
        "arguments[0].value = '1997'; arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", choose_year)

    choose_day = driver.find_element(By.CSS_SELECTOR, "[aria-label='Choose Wednesday, July 2nd, 1997']")
    choose_day.click()


def test_fill_object(driver):
    object = driver.find_element(By.ID, 'subjectsInput')
    object.send_keys('Maths')
    object.send_keys(Keys.ENTER)


def test_select_hobbies(driver):
    hobbies = driver.find_element(By.XPATH, "//label[text()='Music']")
    hobbies.click()


def test_fill_adress(driver):
    adress = driver.find_element(By.ID, 'currentAddress')
    adress.send_keys('Russia, Krasnodar')


def test_select_state_and_city(driver):
    state = driver.find_element(By.ID, 'state')
    state.click()

    ncr_option = driver.find_element(By.XPATH, "//div[text()='NCR']")
    ncr_option.click()

    city = driver.find_element(By.ID, 'city')
    city.click()

    delhi_option = driver.find_element(By.XPATH, "//div[text()='Delhi']")
    delhi_option.click()


def test_upload_form(driver):
    button_submit = driver.find_element(By.ID, "submit")
    button_submit.click()

    submitted_form = driver.find_element(By.ID, "example-modal-sizes-title-lg").text
    print(submitted_form)
    assert "Thanks for submitting the form" in submitted_form


def test_complete_form(driver, practice_form):
    """Полное заполнение формы"""
    test_personal_info(driver)
    test_select_gender(driver)
    test_fill_number(driver)
    test_select_birth(driver)
    test_fill_object(driver)
    test_select_hobbies(driver)
    test_fill_adress(driver)
    test_select_state_and_city(driver)
    test_upload_form(driver)

    submitted_form = driver.find_element(By.ID, "example-modal-sizes-title-lg").text
    assert "Thanks for submitting the form" in submitted_form
    print(submitted_form)

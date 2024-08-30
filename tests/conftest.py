import random
import time
ttime = 0.5

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()  # создали объект для опций
#chrome_options.add_argument('--headless')  # добавили настройку
#chrome_options.add_argument('--window-size=640,480')  # добавили ещё настройку

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

@pytest.fixture(scope='class')
def account_normal():
    return 'iivanov@iivanov.com', '123456'

@pytest.fixture(scope='class')
def account(account_normal):

    email, password = account_normal

    driver.get('https://stellarburgers.nomoreparties.site/login')

    elm = driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(1) > div > div > input')
    elm.send_keys(email)

    elm = driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(2) > div > div > input')
    elm.send_keys(password)

    driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > button').click()

    yield driver, email, password

    driver.quit()

@pytest.fixture(scope='class')
def account_cabinet(account_normal):

    email, password = account_normal

    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.CSS_SELECTOR,'#root > div > header > nav > a').click()

    elm = driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(1) > div > div > input')
    elm.send_keys(email)

    elm = driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(2) > div > div > input')
    elm.send_keys(password)

    driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > button').click()

    yield driver, email, password

    driver.quit()

@pytest.fixture(scope='class')
def account_input(account_normal):

    email, password = account_normal

    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.CSS_SELECTOR,'#root > div > header > nav > a').click()

    elm = driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(1) > div > div > input')
    elm.send_keys(email)

    elm = driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(2) > div > div > input')
    elm.send_keys(password)

    driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > button').click()

    yield driver, email, password

    driver.quit()

@pytest.fixture(scope='class')
def account_register_account(account_normal):

    email, password = account_normal

    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > div > p > a').click()

    elm = driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(1) > div > div > input')
    elm.send_keys(email)

    elm = driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(2) > div > div > input')
    elm.send_keys(password)

    driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > button').click()

    yield driver, email, password

    driver.quit();
#root > div > main > div > div > p:nth-child(2) > a

from selenium.webdriver.support      import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope='class')
def account_forget_password(account_normal):

    email, password = account_normal
    letter_code = '00000000'

    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > div > p:nth-child(2) > a').click()

    time.sleep(ttime); #driver.refresh()
    elm = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset/div/div/input')
    elm.send_keys(email)

    elm = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    elm.click()

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                            "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input[@type='password']")))

    elm = driver.find_element(By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input[@type='password']")
    elm.send_keys(password)

    elm = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input[@type='text']")
    elm.send_keys(letter_code)

    elm = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button[text()='Сохранить']")
    elm.click()

    yield driver, email, password

    driver.quit()

@pytest.fixture(scope='class')
def account_with_any_login():
    def _account_with_any_login(email, password):


        driver.get('https://stellarburgers.nomoreparties.site/login')

        elm = driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(1) > div > div > input')
        elm.send_keys(email)

        if password != '':
            elm = driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(2) > div > div > input')
            elm.send_keys(password)

        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > button').click()

        return email, password

    yield driver, _account_with_any_login

    driver.quit()

@pytest.fixture
def registration_success(account_normal):

    driver = webdriver.Chrome(service=service, options=chrome_options)

    name     = 'Vladimir'
    email    = f'bcc20080913_13_{random.randint(100,999)}@mail.ru'
    password = '123456'

    driver.get('https://stellarburgers.nomoreparties.site/register')

    elm = driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(1) > div > div > input')
    elm.send_keys(name)

    elm = driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(2) > div > div > input')
    elm.send_keys(email)

    elm = driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(3) > div > div > input')
    elm.send_keys(password)

    elm = driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > form > button')
    elm.click()

    yield driver, name, email, password

    driver.quit()

@pytest.fixture
def registration_with_name_email():
    driver = webdriver.Chrome(service=service, options=chrome_options)

    def _registration_with_name_email(driver, name, email, password):
            driver.get('https://stellarburgers.nomoreparties.site/register')

            elm = driver.find_element(By.CSS_SELECTOR,
                                      '#root > div > main > div > form > fieldset:nth-child(1) > div > div > input')
            elm.send_keys(name)

            elm = driver.find_element(By.CSS_SELECTOR,
                                      '#root > div > main > div > form > fieldset:nth-child(2) > div > div > input')
            elm.send_keys(email)

            elm = driver.find_element(By.CSS_SELECTOR,
                                      '#root > div > main > div > form > fieldset:nth-child(3) > div > div > input')
            elm.send_keys(password)

            driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > button").click()

            return (name, email, password)

    yield driver, _registration_with_name_email

    driver.quit()


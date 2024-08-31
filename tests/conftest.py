import random
import time
ttime = 0.5
from locators import *

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

    elm = driver.find_element(By.CSS_SELECTOR, LOGIN_EMAIL)
    elm.send_keys(email)

    elm = driver.find_element(By.CSS_SELECTOR,LOGIN_PASSWORD)
    elm.send_keys(password)

    driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()

    yield driver, email, password

    driver.quit()

@pytest.fixture(scope='class')
def account_cabinet(account_normal):

    email, password = account_normal

    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.CSS_SELECTOR,'#root > div > header > nav > a').click()

    elm = driver.find_element(By.CSS_SELECTOR,LOGIN_EMAIL)
    elm.send_keys(email)

    elm = driver.find_element(By.CSS_SELECTOR,LOGIN_PASSWORD)
    elm.send_keys(password)

    driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()

    yield driver, email, password

    driver.quit()

@pytest.fixture(scope='class')
def account_input(account_normal):

    email, password = account_normal

    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.CSS_SELECTOR,'#root > div > header > nav > a').click()

    elm = driver.find_element(By.CSS_SELECTOR,LOGIN_EMAIL)
    elm.send_keys(email)

    elm = driver.find_element(By.CSS_SELECTOR,LOGIN_PASSWORD)
    elm.send_keys(password)

    driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()

    yield driver, email, password

    driver.quit()

@pytest.fixture(scope='class')
def account_register_account(account_normal):

    email, password = account_normal

    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(By.CSS_SELECTOR,A_REGISTRATION).click()

    elm = driver.find_element(By.CSS_SELECTOR,LOGIN_EMAIL)
    elm.send_keys(email)

    elm = driver.find_element(By.CSS_SELECTOR,LOGIN_PASSWORD)
    elm.send_keys(password)

    driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()

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
    driver.find_element(By.CSS_SELECTOR,A_FORGET).click()

    time.sleep(ttime); #driver.refresh()
    elm = driver.find_element(By.XPATH,LOGIN_EMAIL_FORGET_XPATH)
    elm.send_keys(email)

    elm = driver.find_element(By.XPATH,LOGIN_EMAIL_FORGET_BUTTON_XPATH)
    elm.click()

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, LOGIN_PASSWORD_FORGET_XPATH)))

    elm = driver.find_element(By.XPATH,LOGIN_PASSWORD_FORGET_XPATH)
    elm.send_keys(password)

    elm = driver.find_element(By.XPATH, LOGIN_LETTER_CODE_FORGET_XPATH)
    elm.send_keys(letter_code)

    elm = driver.find_element(By.XPATH, LOGIN_FORGET_BUTTON)
    elm.click()

    yield driver, email, password

    driver.quit()

@pytest.fixture(scope='class')
def account_with_any_login():
    def _account_with_any_login(email, password):


        driver.get('https://stellarburgers.nomoreparties.site/login')

        elm = driver.find_element(By.CSS_SELECTOR,LOGIN_EMAIL)
        elm.send_keys(email)

        if password != '':
            elm = driver.find_element(By.CSS_SELECTOR,LOGIN_PASSWORD)
            elm.send_keys(password)

        driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()

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

    elm = driver.find_element(By.CSS_SELECTOR,REGISTRATION_NAME)
    elm.send_keys(name)

    elm = driver.find_element(By.CSS_SELECTOR,REGISTRATION_EMAIL)
    elm.send_keys(email)

    elm = driver.find_element(By.CSS_SELECTOR,REGISTRATION_PASSWORD)
    elm.send_keys(password)

    elm = driver.find_element(By.CSS_SELECTOR,REGISTRATION_BUTTON)
    elm.click()

    yield driver, name, email, password

    driver.quit()

@pytest.fixture
def registration_with_name_email():
    driver = webdriver.Chrome(service=service, options=chrome_options)

    def _registration_with_name_email(driver, name, email, password):
            driver.get('https://stellarburgers.nomoreparties.site/register')

            elm = driver.find_element(By.CSS_SELECTOR,REGISTRATION_NAME)
            elm.send_keys(name)

            elm = driver.find_element(By.CSS_SELECTOR,REGISTRATION_EMAIL)
            elm.send_keys(email)

            elm = driver.find_element(By.CSS_SELECTOR,REGISTRATION_PASSWORD)
            elm.send_keys(password)

            driver.find_element(By.CSS_SELECTOR, REGISTRATION_BUTTON).click()

            return (name, email, password)

    yield driver, _registration_with_name_email

    driver.quit()


wait_time = 5

from locators import *

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()  # создали объект для опций
service = Service(ChromeDriverManager().install())

@pytest.fixture
def ddriver():
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

'''  
     https://docs.pytest.org/en/stable/how-to/fixtures.html
     Я ничего не придумываю, я беру код или их аналоги из примеров  
'''
@pytest.fixture
def account_normal():
    return 'iivanov@iivanov.com', '123456'

@pytest.fixture
def account_for_success_entrance(account_normal, account_with_any_login):
    email, password = account_normal
    driver, func = account_with_any_login
    email, password = func(email, password)
    yield driver, email, password

@pytest.fixture
def account_input(account_normal, account_with_any_login):
    email, password = account_normal
    driver, func = account_with_any_login
    driver.get(URL_COMMON)
    WebDriverWait(driver,wait_time).until(EC.element_to_be_clickable((By.XPATH, LOGIN_NORMAL_INPUT_WAIT_XPATH)))
    driver.find_element(By.XPATH,LOGIN_NORMAL_INPUT_XPATH).click()
    email, password = func(email, password)
    yield driver, email, password

@pytest.fixture
def account_register_account(account_normal, account_with_any_login):
    email, password = account_normal
    driver, func = account_with_any_login
    driver.get(URL_REGISTRATION)
    driver.find_element(By.CSS_SELECTOR,A_REGISTRATION).click()
    email, password = func(email, password)
    yield driver, email, password

@pytest.fixture
def account_forget_password(ddriver, account_normal):
    email, password = account_normal
    letter_code = '00000000'
    driver = ddriver
    driver.get(URL_LOGIN)
    driver.find_element(By.CSS_SELECTOR,A_FORGET).click()
    WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, LOGIN_EMAIL_FORGET_BUTTON_XPATH)))
    driver.find_element(By.XPATH,LOGIN_EMAIL_FORGET_XPATH).send_keys(email)
    driver.find_element(By.XPATH,LOGIN_EMAIL_FORGET_BUTTON_XPATH).click()
    WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, LOGIN_PASSWORD_FORGET_XPATH)))
    driver.find_element(By.XPATH,LOGIN_PASSWORD_FORGET_XPATH).send_keys(password)
    driver.find_element(By.XPATH, LOGIN_LETTER_CODE_FORGET_XPATH).send_keys(letter_code)
    driver.find_element(By.XPATH, LOGIN_FORGET_BUTTON).click()
    yield driver, email, password

'''  
     https://docs.pytest.org/en/stable/how-to/fixtures.html
     Я ничего не придумываю, я беру код или их аналоги из примеров. Это называется фабрика.
'''
@pytest.fixture
def account_with_any_login(ddriver):
    driver = ddriver
    def _account_with_any_login(email, password):
        driver.get(URL_LOGIN)
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, LOGIN_BUTTON_WAIT_XPATH)))
        driver.find_element(By.XPATH,LOGIN_EMAIL_XPATH).send_keys(email)
        if password != '':
            driver.find_element(By.XPATH,LOGIN_PASSWORD_XPATH).send_keys(password)
        driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH).click()
        return email, password
    yield driver, _account_with_any_login

'''  
     https://docs.pytest.org/en/stable/how-to/fixtures.html
     Я ничего не придумываю, я беру код или их аналоги из примеров.  Это называется фабрика.
'''
@pytest.fixture
def registration_with_name_email(ddriver):
    def _registration_with_name_email(name, email, password):
            driver = ddriver
            driver.get(URL_REGISTRATION)
            WebDriverWait(driver,wait_time).until(EC.element_to_be_clickable((By.XPATH, REGISTRATION_BUTTON_XPATH)))
            driver.find_element(By.XPATH, REGISTRATION_NAME_XPATH).send_keys(name)
            driver.find_element(By.XPATH, REGISTRATION_EMAIL_XPATH).send_keys(email)
            driver.find_element(By.XPATH, REGISTRATION_PASSWORD_XPATH).send_keys(password)
            driver.find_element(By.XPATH, REGISTRATION_BUTTON_XPATH).click()
            return driver, name, email, password
    yield _registration_with_name_email


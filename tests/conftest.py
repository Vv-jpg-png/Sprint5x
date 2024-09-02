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

@pytest.fixture
def account_normal():
    return 'iivanov@iivanov.com', '123456'

@pytest.fixture
def account_for_success_entrance(ddriver, account_normal):
    email, password = account_normal
    driver = ddriver
    driver.get(URL_LOGIN)
    WebDriverWait(driver,wait_time).until(EC.element_to_be_clickable((By.XPATH, LOGIN_BUTTON_WAIT_XPATH)))
    driver.find_element(By.CSS_SELECTOR, LOGIN_EMAIL).send_keys(email)
    driver.find_element(By.CSS_SELECTOR,LOGIN_PASSWORD).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()
    yield driver, email, password

@pytest.fixture
def account_input(ddriver, account_normal):
    email, password = account_normal
    driver = ddriver
    driver.get(URL_COMMON)
    WebDriverWait(driver,wait_time).until(EC.element_to_be_clickable((By.XPATH, LOGIN_NORMAL_INPUT_WAIT_XPATH)))
    driver.find_element(By.XPATH,LOGIN_NORMAL_INPUT_XPATH).click()
    WebDriverWait(driver,wait_time).until(EC.element_to_be_clickable((By.XPATH, LOGIN_BUTTON_WAIT_XPATH)))
    driver.find_element(By.CSS_SELECTOR,LOGIN_EMAIL).send_keys(email)
    driver.find_element(By.CSS_SELECTOR,LOGIN_PASSWORD).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()
    yield driver, email, password

@pytest.fixture
def account_register_account(ddriver, account_normal):
    email, password = account_normal
    driver = ddriver
    driver.get(URL_REGISTRATION)
    driver.find_element(By.CSS_SELECTOR,A_REGISTRATION).click()
    WebDriverWait(driver,wait_time).until(EC.element_to_be_clickable((By.XPATH, LOGIN_BUTTON_WAIT_XPATH)))
    driver.find_element(By.CSS_SELECTOR,LOGIN_EMAIL).send_keys(email)
    driver.find_element(By.CSS_SELECTOR,LOGIN_PASSWORD).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()
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

@pytest.fixture
def account_with_any_login(ddriver):
    driver = ddriver
    def _account_with_any_login(email, password):
        driver.get(URL_LOGIN)
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, LOGIN_BUTTON_WAIT_XPATH)))
        driver.find_element(By.CSS_SELECTOR,LOGIN_EMAIL).send_keys(email)
        if password != '':
            driver.find_element(By.CSS_SELECTOR,LOGIN_PASSWORD).send_keys(password)
        driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()
        return email, password
    yield driver, _account_with_any_login

@pytest.fixture
def registration_with_name_email(ddriver):
    driver = ddriver
    def _registration_with_name_email(driver, name, email, password):
            driver.get(URL_REGISTRATION)
            driver.find_element(By.CSS_SELECTOR,REGISTRATION_NAME).send_keys(name)
            driver.find_element(By.CSS_SELECTOR,REGISTRATION_EMAIL).send_keys(email)
            driver.find_element(By.CSS_SELECTOR,REGISTRATION_PASSWORD).send_keys(password)
            driver.find_element(By.CSS_SELECTOR, REGISTRATION_BUTTON).click()
            return (name, email, password)
    yield driver, _registration_with_name_email


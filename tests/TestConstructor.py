import time
import pytest
wait_time = 5

from locators import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestConstructor():

    def test_constructor_bulki_success(self, account_cabinet):
        driver, email, password = account_cabinet
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver,wait_time).until(EC.presence_of_element_located((By.XPATH,CONSTR_BULKI_WAIT_XPATH)))
        elm = driver.find_element(By.XPATH, CONSTR_BULKI_A_XPATH)
        elm.click()
        assert elm is not None

    def test_constructor_souge_success(self, account_cabinet):
        driver, email, password = account_cabinet
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver,wait_time).until(EC.presence_of_element_located((By.XPATH,
                                        CONSTR_SOUGE_A_XPATH)))
        elm = driver.find_element(By.XPATH, CONSTR_SOUGE_A_XPATH )
        elm.click()
        assert elm is not None

    def test_constructor_nachinki_success(self, account_cabinet):
        driver, email, password = account_cabinet
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver,wait_time).until(EC.presence_of_element_located((By.XPATH,
                                        CONSTR_NACHINKA_A_XPATH)))
        elm = driver.find_element(By.XPATH, CONSTR_NACHINKA_A_XPATH)
        elm.click()
        assert elm is not None
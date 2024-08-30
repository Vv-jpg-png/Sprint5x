import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestConstructor():

    def test_constructor_bulki_success(self, account_cabinet):
        driver, email, password = account_cabinet
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,
                                        '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span')))
        elm = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]')
        elm.click()
        assert elm is not None

    def test_constructor_souge_success(self, account_cabinet):
        driver, email, password = account_cabinet
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,
                                        '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span')))
        elm = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span')
        elm.click()
        assert elm is not None

    def test_constructor_nachinki_success(self, account_cabinet):
        driver, email, password = account_cabinet
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,
                                        '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span')))
        elm = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span')
        elm.click()
        assert elm is not None
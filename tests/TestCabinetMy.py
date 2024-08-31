import time
import pytest
from locators import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCabinetMy():
    def test_my_cabinet_input_success(self,account_cabinet):
        driver, email, password = account_cabinet
        driver.find_element(By.XPATH,CABINET_A_XPATH).click()
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,CABINET_EXIT_BUTTON_XPATH)))
        elm = driver.find_element(By.XPATH,CABINET_EXIT_BUTTON_XPATH)
        assert elm is not None

    def test_my_cabinet_constructor_success(self,account_cabinet):
        driver, email, password = account_cabinet
        driver.find_element(By.XPATH,'//*[@id="root"]/div/header/nav/a').click()
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,CABINET_EXIT_BUTTON_XPATH)))
        elm = driver.find_element(By.XPATH,CABINET_CONSTRUCTOR_A_XPATH)
        elm.click()
        assert elm is not None

    def test_my_cabinet_logotipe_success(self,account_cabinet):
        driver, email, password = account_cabinet
        driver.find_element(By.XPATH,'//*[@id="root"]/div/header/nav/a').click()
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,CABINET_EXIT_BUTTON_XPATH)))
        elm = driver.find_element(By.XPATH,CABINET_LOGOTYPE_A_XPATH)
        elm.click()
        assert elm is not None

    def test_my_cabinet_exit_success(self,account_cabinet):
        driver, email, password = account_cabinet
        driver.find_element(By.XPATH,'//*[@id="root"]/div/header/nav/a').click()
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,CABINET_EXIT_BUTTON_XPATH)))
        elm = (driver.find_element(By.XPATH,CABINET_EXIT_BUTTON_XPATH))
        elm.click()

        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,CABINET_LOGIN_BUTTON_XPATH)))

        assert '/login' in driver.current_url


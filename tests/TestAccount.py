
wait_time = 5

from locators import *
import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestAccount():
        def test_account_success(self,account):
                driver, email, password = account
                WebDriverWait(driver,wait_time).until(EC.element_to_be_clickable((By.XPATH, LOGIN_SUCCESS_WAIT_XPATH)))
                elm = driver.find_element(By.XPATH, LOGIN_SUCCESS_XPATH)
                assert elm is not None

        def test_account_input_success(self,account_input):
                driver, email, password = account_input
                WebDriverWait(driver,wait_time).until(EC.element_to_be_clickable((By.XPATH, LOGIN_SUCCESS_WAIT_XPATH)))
                elm = driver.find_element(By.XPATH, LOGIN_SUCCESS_XPATH)
                assert elm is not None

        #@pytest.mark.skip('error')
        def test_account_cabinet_success(self,account_cabinet):
                driver, email, password = account_cabinet
                WebDriverWait(driver,wait_time).until(EC.element_to_be_clickable((By.XPATH, LOGIN_SUCCESS_WAIT_XPATH)))
                elm = driver.find_element(By.XPATH, LOGIN_SUCCESS_XPATH)
                assert elm is not None

        #@pytest.mark.skip('error')
        def test_register_account_success(self,account_register_account):
                driver, email, password = account_register_account
                WebDriverWait(driver,wait_time).until(EC.element_to_be_clickable((By.XPATH, LOGIN_SUCCESS_WAIT_XPATH)))
                elm = driver.find_element(By.XPATH, LOGIN_SUCCESS_XPATH)
                assert elm is not None

        #@pytest.mark.skip('error')
        def test_account_forget_password(self,account_forget_password):
                driver, email, password = account_forget_password

                ttext = driver.current_url
                aassert = ("/reset-password" in ttext)
                assert aassert
                return

        #pytest.mark.skip('error')
        @pytest.mark.parametrize('account,password',[['ivanov934@iivanov.com','123'],
                                                     ['qwerty@123.ya.org','12345'],
                                                     ['qq','12345'],
                                                     ])
        def test_account_fail(self, account_with_any_login, account, password):
                driver, func = account_with_any_login
                account, password = func(account, password)
                WebDriverWait(driver,wait_time).until(EC.visibility_of_element_located((By.XPATH, LOGIN_WRONG_ACCOUNT_WAIT_XPATH)))
                wrong_text = driver.find_element(By.XPATH, LOGIN_WRONG_ACCOUNT_XPATH)
                assert 'Некорректный пароль' in wrong_text.text
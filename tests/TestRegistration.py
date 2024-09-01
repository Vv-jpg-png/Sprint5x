import pytest
import random
from locators import *
wait_time   = 5

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestRegistration():
    def test_registration_success(self, registration_with_name_email):

        name = 'Vladimir'
        email = f'bcc20080913_13_{random.randint(100, 999)}@mail.ru'
        password = '123456'

        driver, func = registration_with_name_email
        name, email, password = func(driver, name, email, password)

        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, LOGIN_BUTTON_WAIT_XPATH)))
        ttext = driver.current_url
        aassert = ("/login" in ttext)
        assert aassert

    @pytest.mark.parametrize('name,email,password',[['','izivanov@iivanov.com','123456'],
                                                    ['','iyivanov@iivanov@com','123456'],
                                                    ['Vlad','iyivanov@iivanov@com','123456'],
                                                    ['Vlad','@iyivanov@iivanov@com','123456'],
                                                    ['Vlad','iyivanov@iivanov.com','1234'],
                                                    ['Vlad','iyivanov@iivanov.com','12345'],
                                                    ['Vlad','iyivanov@iivanov.com',''],
                                                    ])
    def test_registration_fail_bad_password(self,registration_with_name_email, name, email, password):
        driver, func = registration_with_name_email
        name, email, password = func(driver, name, email, password)
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, REGISTRATION_BUTTON)))
        ttext = driver.current_url
        aassert = ("/register" in ttext)
        assert aassert
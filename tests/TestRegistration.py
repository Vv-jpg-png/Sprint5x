import pytest
import random
from locators import *
wait_time   = 20

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

class TestRegistration():
    #@pytest.mark.skip('xxx')
    def test_registration_success(self, registration_with_name_email):
        name = F'Vladimir{random.randint(1000, 9999)}'
        email = f'bcc20080913_13_{random.randint(1000, 9999)}@mail.ru'
        password = '1234567'
        func = registration_with_name_email
        driver, name, email, password = func(name, email, password)
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, LOGIN_BUTTON_WAIT_XPATH)))
        assert ("/login" in driver.current_url)

    @pytest.mark.parametrize('name,email,password',[['','izivanov@iivanov.com','123456'],
                                                    ['','iyivanov@iivanov@com','123456'],
    #                                                ['Vlad','iyivanov@iivanov@com','123456'],
    #                                                ['Vlad','@iyivanov@iivanov@com','123456'],
    #                                                ['Vlad','iyivanov@iivanov.com','1234'],
    #                                                ['Vlad','iyivanov@iivanov.com','12345'],
    #                                                ['Vlad','iyivanov@iivanov.com',''],
                                                    ])
    def test_registration_fail_bad_password(self,registration_with_name_email, name, email, password):
        func = registration_with_name_email
        driver, name, email, password = func(name, email, password)
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, REGISTRATION_BUTTON_XPATH)))
        assert ("/register" in driver.current_url)
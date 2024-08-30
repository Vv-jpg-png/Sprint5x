import pytest

import time
ttime   = 0.5

class TestRegistration():
    def test_registration_success(self, registration_success):
        driver, name, email, password = registration_success
        time.sleep(ttime)
        driver.refresh()
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
        time.sleep(ttime)
        driver.refresh()
        ttext = driver.current_url
        aassert = ("/register" in ttext)
        assert aassert
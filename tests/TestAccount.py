import time
ttime = 0.5
import random

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class TestAccount():
        def test_account_success(self,account):
                driver, email, password = account
                return

        def test_account_input_success(self,account_input):
                driver, email, password = account_input
                return

        def test_account_cabinet_success(self,account_cabinet):
                driver, email, password = account_cabinet
                return

        def test_register_account_success(self,account_register_account):
                driver, email, password = account_register_account
                return

        def test_account_forget_password(self,account_forget_password):
                driver, email, password = account_forget_password

                time.sleep(ttime)

                ttext = driver.current_url
                aassert = ("/login" in ttext) # ????????????
                aassert = ("/reset-password" in ttext)
                assert aassert
                return

        @pytest.mark.parametrize('account,password',[['ivanov934@iivanov.com','123'],
                                                     ['qwerty@123.ya.org','12345'],
                                                     ['qq','12345'],
                                                     #['qq1',''], # ?????????????
                                                     ])
        def test_account_fail(self, account_with_any_login, account, password):
                driver, func = account_with_any_login
                account, password = func(account, password)

                #@// *[ @ id = "root"] / div / main / div / form / fieldset[2] / div / p
                wrong_text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/p")
                assert 'Некорректный пароль' in wrong_text.text
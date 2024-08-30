import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCabinetMy():
    ##@pytest.mark.skip('error')
    def test_my_cabinet_input_success(self,account_cabinet):
        driver, email, password = account_cabinet
        driver.find_element(By.XPATH,'//*[@id="root"]/div/header/nav/a').click()
        # // *[ @ id = "root"] / div / main / div / nav / ul / li[3] / button
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,
                                        "//*[@id='root']/div/main/div/nav/ul/li[3]/button")))
        elm = driver.find_element(By.XPATH,"//*[@id='root']/div/main/div/nav/ul/li[3]/button")
        assert elm is not None

    def test_my_cabinet_constructor_success(self,account_cabinet):
        driver, email, password = account_cabinet
        driver.find_element(By.XPATH,'//*[@id="root"]/div/header/nav/a').click()
        # // *[ @ id = "root"] / div / main / div / nav / ul / li[3] / button
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,
                                        "//*[@id='root']/div/main/div/nav/ul/li[3]/button")))
        elm = driver.find_element(By.XPATH,"//*[@id='root']/div/header/nav/ul/li[1]/a")
        elm.click()
        assert elm is not None

    def test_my_cabinet_logotipe_success(self,account_cabinet):
        driver, email, password = account_cabinet
        driver.find_element(By.XPATH,'//*[@id="root"]/div/header/nav/a').click()
        # // *[ @ id = "root"] / div / main / div / nav / ul / li[3] / button
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,
                                        "//*[@id='root']/div/main/div/nav/ul/li[3]/button")))
        elm = driver.find_element(By.XPATH,"//*[@id='root']/div/header/nav/div/a")
        elm.click()
        assert elm is not None

    def test_my_cabinet_exit_success(self,account_cabinet):
        driver, email, password = account_cabinet
        driver.find_element(By.XPATH,'//*[@id="root"]/div/header/nav/a').click()
        # // *[ @ id = "root"] / div / main / div / nav / ul / li[3] / button
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,
                                        "//*[@id='root']/div/main/div/nav/ul/li[3]/button")))
        elm = (driver.find_element(By.XPATH,"//*[@id='root']/div/main/div/nav/ul/li[3]/button"))
        elm.click()

        #// *[ @ id = "root"] / div / main / div / form / button
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,
                                        '//*[@id="root"]/div/main/div/form/button[text()="Войти"]')))

        assert '/login' in driver.current_url


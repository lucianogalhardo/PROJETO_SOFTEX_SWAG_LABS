from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

import pytest
import time


@pytest.fixture
def setup_teardown():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


#primeiro teste: bloqueio de login com senha incorreta

def test_bloqueio_senha_incorreta(setup_teardown):

    driver = setup_teardown
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("user123")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    erro = driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]')
    assert erro.is_displayed()
    assert "Epic sadface: Username and password do not match any user in this service" in erro.text
    time.sleep(1)




#segundo teste: bloqueio de login com campos vazios

def test_bloqueio_campos_vazios(setup_teardown):

    driver = setup_teardown
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    erro = driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]')
    assert erro.is_displayed()
    assert "Epic sadface: Username is required" in erro.text
    time.sleep(3)




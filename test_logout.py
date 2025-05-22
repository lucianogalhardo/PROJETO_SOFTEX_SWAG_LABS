from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture
def setup_teardown():
    # Setup
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/v1/")
    #driver.set_window_position(2000, 0)
    #driver.implicitly_wait(10)
    time.sleep(2)
    # Teardown
    yield driver
    driver.quit()

def find_id(driver, elemento):
    return driver.find_element(By.ID, elemento)

# Testando o logout
def test_logout(setup_teardown):
    # Recuperar o driver
    driver = setup_teardown
    # Fazer login
    campo_usuario = find_id(driver, "user-name")
    campo_usuario.send_keys("standard_user")
    campo_senha = find_id(driver, "password")
    campo_senha.send_keys("secret_sauce")
    btn_login = find_id(driver, "login-button")
    btn_login.click()
    time.sleep(5)
    
    # Clicar no menu lateral
    btn_menu = driver.find_element(By.CSS_SELECTOR, ".bm-burger-button")
    btn_menu.click()
    time.sleep(5)
    
    # Clicar no botão logout
    btn_logout = find_id(driver, "logout_sidebar_link")
    btn_logout.click()
    time.sleep(10)
    
    # # Validar se o usuário foi desconectado
    # assert driver.current_url == "https://www.saucedemo.com/v1/"
    # assert driver.find_element(By.ID, "login-button").is_displayed()

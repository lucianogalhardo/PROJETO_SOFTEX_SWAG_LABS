from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture
def setup_teardown():
    
    # Setup
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/")
    
    driver.implicitly_wait(10)
    time.sleep(2)
    
    # Teardown
    yield driver
    driver.quit()


def find_id(driver, elemento):
    return driver.find_element(By.ID, elemento)

# metodo para aceitar o alert
# def accept_alert_chrome(driver, timeout=10):
    
#     alert = Alert(driver)
#     alert_text = alert.text.lower()
#     if "senha" in alert_text:
#         alert.accept()
    

# Testando o logout
def test_logout(setup_teardown):
    # Recuperar o driver
    driver = setup_teardown
    # Fazer login
    campo_usuario = find_id(driver, "user-name")
    campo_usuario.send_keys("standard_user")
    campo_senha = find_id(driver, "password")
    campo_senha.send_keys("secret_sauce")
    time.sleep(2)
    btn_login = find_id(driver, "login-button")
    btn_login.click()
    time.sleep(2)

    # Aceitar o alert
    # accept_alert_chrome(driver)

    # Clicar no menu lateral
    btn_menu = driver.find_element(By.CSS_SELECTOR, ".bm-burger-button")
    btn_menu.click()
    time.sleep(2)
    
    # Clicar no botão logout
    btn_logout = find_id(driver, "logout_sidebar_link")
    btn_logout.click()
    time.sleep(2)
    
    # Validar se o logout foi feito com sucesso
    assert driver.title == "Swag Labs"
    assert driver.current_url == "https://www.saucedemo.com/"
    assert driver.find_element(By.CSS_SELECTOR, ".login_logo").is_displayed()

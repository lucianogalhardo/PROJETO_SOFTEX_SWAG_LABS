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

# Testando o botão "About"
def test_about(setup_teardown):
    driver = setup_teardown

    # Fazer login
    campo_usuario = find_id(driver, "user-name")
    campo_usuario.send_keys("standard_user")
    campo_senha = find_id(driver, "password")
    campo_senha.send_keys("secret_sauce")
    time.sleep(2)
    botao_login = find_id(driver, "login-button")  
    botao_login.click()
    time.sleep(2)

    # Clicar no menu lateral
    btn_menu = driver.find_element(By.CSS_SELECTOR, ".bm-burger-button")
    btn_menu.click()
    time.sleep(2)

    # Clicar no botão "About"
    btn_about = find_id(driver, "about_sidebar_link")
    btn_about.click()
    time.sleep(2)

    # Verificar se a URL contém "Saucelabs"
    assert "saucelabs" in driver.current_url
    # Verificar se o título contém "Sauce Labs"
    assert "Sauce Labs" in driver.title
    

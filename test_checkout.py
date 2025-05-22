import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def find_id(driver, id):
    return driver.find_element(By.ID, id)

def test_checkout_success(driver):
    # Login
    find_id(driver, "user-name").send_keys("standard_user")
    find_id(driver, "password").send_keys("secret_sauce")
    find_id(driver, "login-button").click()
    time.sleep(5)

    # Adicionar item ao carrinho
    find_id(driver, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(5)

    # Ir ao carrinho
    find_id(driver, "shopping_cart_container").click()
    time.sleep(5)

    # Iniciar checkout
    find_id(driver, "checkout").click()
    time.sleep(5)

    # Inserindo os dados
    find_id(driver, "first-name").send_keys("Jan")
    find_id(driver, "last-name").send_keys("QA")
    find_id(driver, "postal-code").send_keys("12345")
    time.sleep(5)

    # Continuar e finalizar compra
    find_id(driver, "continue").click()
    time.sleep(5)
    find_id(driver, "finish").click()
    time.sleep(5)

    # Verificar mensagem de sucesso
    mensagem = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert mensagem == "Thank you for your order!"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

# Fixture para setup e teardown do Selenium
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

# Função utilitária
def find_id(driver, id):
    return driver.find_element(By.ID, id)

# Teste de login + adicionar item ao carrinho
def test_add_to_cart(driver):
    # Login
    find_id(driver, "user-name").send_keys("standard_user")
    find_id(driver, "password").send_keys("secret_sauce")
    find_id(driver, "login-button").click()
    time.sleep(4)
    
    # Adicionar produto
    find_id(driver, "add-to-cart-sauce-labs-backpack").click()

    # Ir para o carrinho
    find_id(driver, "shopping_cart_container").click()
    time.sleep(4)

    # Validar que o produto está no carrinho
    item_nome = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert item_nome == "Sauce Labs Backpack"

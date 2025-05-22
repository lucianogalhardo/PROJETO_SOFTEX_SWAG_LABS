from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time


# Aqui Abre o navegador, vai para o site e fecha no final.
@pytest.fixture
def setup():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()

# Aqui estou fazendo login com o usuário padrão
def login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


# Aqui estou ordenando os produtos do mais caro para o mais barato
def ordenar_preco_maior_para_menor(driver):
    seletor = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    seletor.select_by_value("hilo") 
    time.sleep(4)


# Aqui estou removendo um item específico do carrinho. No caso o Sauce Labs Backpack.
def remover_item_do_carrinho(driver):
    # Aqui estou clicando no carrinho
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click() 
    # Aqui estou removendo o item do carrinho usando ID.
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click() 
    time.sleep(4)

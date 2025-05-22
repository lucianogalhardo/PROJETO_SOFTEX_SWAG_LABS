from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time


# Aqui Abre o navegador, vai para o site e fecha no final.
#  Fixture serve para configurar o driver (abre/fecha navegador automaticamente)
@pytest.fixture
def setup():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()


# Aqui estou fazendo login como usuário padrão.
def login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


# TESTE 1 - ORDENANDO PRODUTOS DO MAIS CARO AO MAIS BARATO

# Aqui estou ordenando os produtos do mais caro para o mais barato
def ordenar_preco_maior_para_menor(driver):
    seletor = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    seletor.select_by_value("hilo")
    time.sleep(4)

# TESTE 2 - REMOVENDO ITEM DO CARRINHO

# Aqui estou removendo um item específico do carrinho. No caso o Sauce Labs Backpack.
def remover_item_do_carrinho(driver):
    # Aqui estou indo para a página do carrinho antes de remover o item
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)  # Espera a página do carrinho carregar

    # Aqui estou removendo o item do carrinho usando ID.
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    time.sleep(2)  # Espera o item ser removido
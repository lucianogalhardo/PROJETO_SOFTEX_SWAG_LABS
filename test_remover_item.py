from selenium.webdriver.common.by import By
from automacao import setup, login, remover_item_do_carrinho

from selenium.webdriver.common.by import By
from automacao import setup, login, remover_item_do_carrinho
import time

# Aqui estou testando se consigo remover um item do carrinho com sucesso
def test_remover_item_do_carrinho(setup):
    driver = setup
    login(driver)

    # Aqui estou adicionando um item (Sauce Labs Backpack) usando By.ID
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(2)  # Espera o item ser adicionado ao carrinho

    remover_item_do_carrinho(driver)

    # Aqui estou verificando se o carrinho está vazio.
    # Estou usando By.CLASS_NAME para localizar todos os elementos com a classe "cart_item"
    itens = driver.find_elements(By.CLASS_NAME, "cart_item")  # find_elements retorna todos os itens com essa classe.
    assert len(itens) == 0 

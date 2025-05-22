from selenium.webdriver.common.by import By
from automacao import setup, login, ordenar_preco_maior_para_menor

def test_ordenar_maior_para_menor(setup):
    driver = setup
    login(driver)

    ordenar_preco_maior_para_menor(driver)

    precos_elementos = driver.find_elements(By.CLASS_NAME, "inventory_item_price") #find_elements retorna todos os itens com aquela classe.
    precos = [float(p.text.replace("$", "")) for p in precos_elementos]

    assert precos == sorted(precos, reverse=True)

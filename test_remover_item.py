import time
from selenium.webdriver.common.by import By
from automacao import setup, login, remover_item_do_carrinho

def test_remover_item_do_carrinho(setup):
    driver = setup

    # 1. Aqui estou fazendo login
    login(driver)
    time.sleep(3)

    # 2. Aqui estou adicionando um item ao carrinho (sauce labs backpack)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    print("Item adicionado ao carrinho")
    time.sleep(2)

    # 3. Esou indo ao carrinho
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)
    print("Página do carrinho:", driver.current_url)

    # 4. Estou removendo o item
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    print("Item removido")
    time.sleep(2)

    # 5. Aqui estou validando a remoção do item
    assert "remove-sauce-labs-backpack" not in driver.page_source
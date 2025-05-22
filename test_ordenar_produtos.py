from selenium.webdriver.common.by import By
from automacao import setup, login, ordenar_preco_maior_para_menor

def test_ordenar_maior_para_menor(setup):
    driver = setup
    
    #1 Aqui estou fazendo login
    login(driver)
    
    # 2 Aqui estou ordenando os produtos do maior para o menor preço
    ordenar_preco_maior_para_menor(driver)
    
    # 3 Aqui estou capturando todos os elementos de preço da página
    precos_elementos = driver.find_elements(By.CLASS_NAME, "inventory_item_price") #find_elements retorna todos os itens com aquela classe.
    
    # 4 Aqui estou convertendo os textos de preço para valores numéricos (float)
    precos = [float(p.text.replace("$", "")) for p in precos_elementos]
    
    #5 Aqui estou validando se os preços estão ordenados do maior para o menor
    assert precos == sorted(precos, reverse=True)
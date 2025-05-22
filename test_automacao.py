from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time


@pytest.fixture
def setup_teardown():
    # Setup
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/v1/")
    driver.set_window_position(2000, 0)
    driver.implicitly_wait(10)
    time.sleep(2)
    # Teardown
    yield driver
    driver.quit()

def find_id(driver, elemento):
    return driver.find_element(By.ID, elemento)


def test_botao_muda_texto(setup_teardown):
    # Recuperar o driver
    driver = setup_teardown
    # Mapear o botão clique me
    btn_click_me = driver.find_element(By.CSS_SELECTOR, "#buttonSimple")
    # recuparar o texto inicial
    texto_antes = btn_click_me.get_attribute("value")
    # Clicar no botão
    btn_click_me.click()
    time.sleep(1)
    # recuperar o texto final
    texto_depois = btn_click_me.get_attribute("value")
    time.sleep(2)
    # validar se os textos são diferentes
    assert texto_antes == "Clique Me!" 
    assert texto_depois == "Obrigado!"

def test_preencher_campo_nome(setup_teardown):
    driver = setup_teardown
    campo_nome = driver.find_element(By.ID, "formNome")
    campo_nome.send_keys("David")
    time.sleep(2)
    assert campo_nome.get_attribute("value") == "David"

def test_preencher_checkbox(setup_teardown):
    driver = setup_teardown
    checkbox_pizza = driver.find_element(By.ID, "formComidaPizza")
    checkbox_pizza.click()
    selected = checkbox_pizza.is_selected()
    time.sleep(2)
    assert selected == True

def test_preencher_radio(setup_teardown):
    driver = setup_teardown
    # checkbox_pizza = driver.find_element(By.ID, "formSexoFem")
    radio_fem = find_id(driver, "formSexoFem")
    radio_fem.click()
    selected = radio_fem.is_selected()
    time.sleep(2)
    assert selected == True

def test_multiplos_checkboxes(setup_teardown):
    driver = setup_teardown

    carne = find_id(driver, "formComidaCarne")
    frango = find_id(driver, "formComidaFrango")
    pizza = find_id(driver, "formComidaPizza")
    veg = find_id(driver, "formComidaVegetariana")

    checkboxes = [carne, frango, pizza, veg]
    
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()
        assert checkbox.is_selected() == True, f"O checkbox {checkbox.get_attribute('id')} deveria estar selecionado"

def test_dropdown(setup_teardown):
    driver = setup_teardown

    dropown_escolaridade = find_id(driver, "formEscolaridade") 

    opcao = Select(dropown_escolaridade)
    opcao.select_by_value("doutorado")

    time.sleep(2)

    opcao_selecionada = opcao.first_selected_option
    assert opcao_selecionada.get_attribute("value") == "doutorado"

def test_clicar_primeiro_item_tabela(setup_teardown):
    driver = setup_teardown

    primeiro_botao = driver.find_element(By.CSS_SELECTOR, '#tabelaUsuarios tr td input[type="button"]')
    primeiro_botao.click()

    alert = Alert(driver)

    assert alert.text == "Francisco"

    alert.accept()
    time.sleep(3)

def test_clicar_item_selecionado(setup_teardown):
    driver = setup_teardown

    botoes = driver.find_elements(By.CSS_SELECTOR, '#tabelaUsuarios tr td input[type="button"]')
    botoes[2].click()
    time.sleep(4)

def test_esperar_dinamicamente(setup_teardown):
    driver = setup_teardown

    # Timeout Explicito -> time.sleep(n)
    # Timeout Implicito -> esperar condiçoes para seguir com o fluxo

    find_id(driver, "buttonDelay").click()

    wait = WebDriverWait(driver, 10)
    novo_campo = wait.until(EC.visibility_of_element_located((By.ID, "novoCampo")))

    novo_campo.send_keys("Teste")
    print("--------------------------------")
    print(novo_campo.get_attribute("value"))
    time.sleep(5)

    assert novo_campo.get_attribute("value") == "Teste"

# pytest -s -k test_clicar_item_selec test_automacao.py, para mostrar o print no terminal.
# git checkout-b SSL-25_DAVID_AUTOMACAO_TEST_CASE
# git commit "Task-123: Implementação do caso de teste A e B"


   









from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurar o navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Executar em modo headless (sem interface gráfica)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

driver = webdriver.Chrome(options=options)

# Acessar a URL
url = 'https://www.webmotors.com.br/carros/sp-cotia/volkswagen/golf?tipoveiculo=carros&localizacao=-23.6026684%2C-46.9194693x100km&estadocidade=S%C3%A3o%20Paulo-Cotia&marca1=VOLKSWAGEN&modelo1=GOLF&lkid=1042&page=1'
driver.get(url)
time.sleep(5)  # Esperar a página carregar

# Extrair dados
carros = driver.find_elements(By.CLASS_NAME, '_Container_70j0p_1')
for carro in carros:
    nome = carro.find_element(By.CLASS_NAME, '_web-title-medium_qtpsh_51').text
    modelo = carro.find_element(By.CLASS_NAME, '_body-regular-small_qtpsh_152').text
    ano = carro.find_element(By.CLASS_NAME, '_body-regular-small_qtpsh_152').text
    km = carro.find_elements(By.CLASS_NAME, '_body-regular-small_qtpsh_152')[1].text
    localizacao = carro.find_element(By.CLASS_NAME, '_body-regular-small_qtpsh_152').text
    preco = carro.find_element(By.CLASS_NAME, '_body-bold-large_qtpsh_78').text
    
    print(f'Nome: {nome}')
    print(f'Modelo: {modelo}')
    print(f'Ano: {ano}')
    print(f'Quilometragem: {km}')
    print(f'Localização: {localizacao}')
    print(f'Preço: {preco}')
    print('-' * 50)

# Fechar o navegador
driver.quit()
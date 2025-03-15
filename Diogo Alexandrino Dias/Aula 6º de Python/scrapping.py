import requests
from bs4 import BeautifulSoup
import time
import random

# Lista de User-Agents
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
]

# URL do site
url = 'https://www.webmotors.com.br/carros/sp-cotia/volkswagen/golf?tipoveiculo=carros&localizacao=-23.6026684%2C-46.9194693x100km&estadocidade=S%C3%A3o%20Paulo-Cotia&marca1=VOLKSWAGEN&modelo1=GOLF&lkid=1042&page=1'

# Configurar headers
headers = {
    'User-Agent': random.choice(user_agents),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'https://www.webmotors.com.br/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

# Fazer a requisição HTTP
resposta = requests.get(url, headers=headers)

# Verificar se a requisição foi bem-sucedida
if resposta.status_code == 200:
    print('Requisição feita com sucesso.')
    
    # Preencher o BeautifulSoup com o conteúdo da página
    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    # Encontrar todos os cards de carros
    carros = soup.find_all('div', class_='_Container_70j0p_1')
    
    # Iterar sobre cada carro e extrair as informações
    for carro in carros:
        # Nome do carro
        nome = carro.find('h2', class_='_web-title-medium_qtpsh_51')
        nome = nome.text.strip() if nome else 'Nome não encontrado'
        
        # Modelo do carro
        modelo = carro.find('h3', class_='_body-regular-small_qtpsh_152')
        modelo = modelo.text.strip() if modelo else 'Modelo não encontrado'
        
        # Ano do carro
        ano = carro.find('p', class_='_body-regular-small_qtpsh_152')
        ano = ano.text.strip() if ano else 'Ano não encontrado'
        
        # Quilometragem do carro
        km = carro.find_all('p', class_='_body-regular-small_qtpsh_152')
        km = km[1].text.strip() if len(km) > 1 else 'Quilometragem não encontrada'
        
        # Localização do carro
        localizacao = carro.find('p', class_='_body-regular-small_qtpsh_152')
        localizacao = localizacao.text.strip() if localizacao else 'Localização não encontrada'
        
        # Preço do carro
        preco = carro.find('p', class_='_body-bold-large_qtpsh_78')
        preco = preco.text.strip() if preco else 'Preço não encontrado'
        
        # Exibir as informações
        print(f'Nome: {nome}')
        print(f'Modelo: {modelo}')
        print(f'Ano: {ano}')
        print(f'Quilometragem: {km}')
        print(f'Localização: {localizacao}')
        print(f'Preço: {preco}')
        print('-' * 50)
        
        # Adicionar um pequeno atraso para evitar bloqueios
        time.sleep(random.uniform(1, 3))
else:
    print('Erro na requisição:', resposta.status_code)
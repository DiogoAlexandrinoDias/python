import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker
import random

# Inicializar o Faker para gerar nomes e cidades aleatórios
fake = Faker('pt_BR')

# Gerar 100 pessoas
nomes = [fake.first_name() for _ in range(30)]
idades = [random.randint(18, 40) for _ in range(30)]
cidades_aleatorias = [fake.city() for _ in range(30)]  # Gerar cidades aleatórias

# Criar o DataFrame com os dados gerados
dados = {
    "Nome": nomes,
    "Idade": idades,
    "Cidade": cidades_aleatorias
}

df = pd.DataFrame(dados)

# Exibir o DataFrame
print("DataFrame com 100 pessoas geradas aleatoriamente:")
print(df)

# Salvar DataFrame no CSV
df.to_csv('100_pessoas.csv', index=False)

# Visualizar o DataFrame a partir do CSV
df_csv = pd.read_csv('100_pessoas.csv')

# Filtrar o DataFrame para idades maiores que 25
df_filtrado = df[df['Idade'] > 25]
print("\nPessoas com idade maior que 25 anos:")
print(df_filtrado)

# Ordenar o DataFrame por idade (decrescente)
df_ordenado = df.sort_values(by='Idade', ascending=False)
print("\nDataFrame ordenado por idade (decrescente):")
print(df_ordenado)

# Exibir estatísticas descritivas
print("\nEstatísticas descritivas da coluna 'Idade':")
print(df['Idade'].describe())

# Média de idade por cidade
media_cidade = df.groupby('Cidade')['Idade'].mean()
print("\nMédia de idade por cidade:")
print(media_cidade)

# Criar gráfico de distribuição de idade por cidade
df.plot(kind='bar', x='Nome',y='Idade', color='Black')
plt.title('Distribuição de idade por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Idade')
plt.suptitle('')  # Remove o título automático do boxplot
plt.xticks(rotation=90)  # Rotacionar os nomes das cidades para melhor visualização
plt.show()
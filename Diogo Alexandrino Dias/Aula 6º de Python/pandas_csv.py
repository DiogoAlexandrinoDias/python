import pandas as pd
import matplotlib.pyplot as plt

# Criar os dados para o nosso DataFrame
dados = {
    "Nome": ["Arthur", "Maria", "Mateus", "Carlos", "Bruna"],
    "Idade": [28, 22, 18, 35, 20],
    "Cidade": ["Cotia", "Carapicuíba", "Cotia", "Osasco", "Cotia"]
}

# Criar o DataFrame
df = pd.DataFrame(dados)

# Exibir o DataFrame  
print(df)

# Salvar DataFrame no CSV
df.to_csv('pandas_dados.csv', index=False)

# Visualizar o DataFrame a partir do CSV
df_csv = pd.read_csv('pandas_dados.csv')

# Filtrar o DataFrame para idades maiores que 25
df_filtrado = df[df['Idade'] > 25]  # Corrigido: 'Idade' em vez de 'idade'
print(df_filtrado)

df_ordenado =df.sort_values(by='Idade', ascending=False)
print (df_ordenado)# Do maior para o menor (Decrecente)

#Exibir estariscas
print(df.describe())

# MEdia por cidade, coluna idade
media_cidade = df.groupby('Cidade')['Idade'].mean()
print(media_cidade)

#criando grafico
#df.plot(kind='pie', x='Nome',y='Idade', color='Black')
#plt.title('Idade das Pessoas')
#plt.xlabel('Nome')
#plt.ylabel('idade')
#plt.show()

df.boxplot(column='Idade', by='Cidade', grid=False)
plt.title('Distribuição de idade por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Idade')

plt.show()

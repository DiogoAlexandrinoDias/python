import csv 

# criar e escrever um arquivo TXT
# W -> Write -> Escrita
with open ('dados.txt', 'w', encoding='utf-8') as arquivo :
    arquivo.write('Nome,idade,cidade\n')
    arquivo.write('Alberto,92,Chique-Chiquen/BA\n')    
    arquivo.write('Arthur,28,Arraial/RJ\n')  
    arquivo.write('Matheus,92,cotia/SP\n')

# Ler o conteudo    
# r -> Read -> Ler     
with open('dados.txt', 'r', encoding='utf-8') as arquivo:
    print('Conteudo do Arquivo txt :')
    print(arquivo.read()) 

# Criando arquivo csv
dados = [
    ['Nome','Idade','Cidade'],
    ['Carlos','32','Santa Isabel'],
    ['Tulio','53','Carapikuiba'],
    ['Rafael','18','Serra do Tabão']    
]

with open ('dados.csv','w', newline='',encoding='utf-8') as csvarquivo:
    escritor = csv.writer(csvarquivo)
    escritor.writerows(dados) 


# Criar arquivo csv
with open ('dados.csv','r',encoding='utf-8') as csvarquivo:
    leitor = csv.reader(csvarquivo)
    print('\nConteudo do arquivo CSV')
    for linha in leitor:    
        print(linha)







    


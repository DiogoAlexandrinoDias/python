""" 
Sistema de desconto de veiculos 
Solicite o nome do veiculo
e preço do veiculo 
se o preço > 80K -> 60% de desconto
se o preço > 50K -> 30% de desconto
se o preço > 30K -> Não sxiste desconto 
 """



print('Ola, Poderia me passar o nome de seu veiculo e o preço dele ?')
nome_veiculo = input('digite o nome do veiculo :')
preço_veiculo = float(input('digite o preço veiculo :'))

if preço_veiculo > 800000:
    desconto = 0.60
elif preço_veiculo > 50000 :
    desconto = 0.30
else:
    desconto = 0

valor_desconto = preço_veiculo * desconto
valor_final = preço_veiculo - valor_desconto


print('o nome do vaiculo é', nome_veiculo)
print('o valor do veiculo é', valor_final)
print('o desconto foi:', desconto)
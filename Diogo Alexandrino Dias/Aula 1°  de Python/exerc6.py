
# Numero pares em um intervalo 

"""
Solicite dois números inteiros ao usuario
Representando o imicio e o fim de intervalo
mostre todos os numero pares nesse intervalo
(incluindo limite inicial e final, se forem pares)
"""

print ('Dois números inteiros imicio e o fim')
print('digite o primerio numero')
n1 = int(input())
print('digite o segundo numero')
n2 = int(input())
# Range (valor inicial, final, e quanto diminui)
for y in range(n1, n2, +1 ):
     print(y)
     if y % 2 == 0:
        print ('o numero e par', y)
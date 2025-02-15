""" 
Desenvolver um sistema que recebe
Valor de A, Valor de B e Valor de C
Calcular de Bhaskara
Delta = b² - 4 * a + * c
Bhaskara
 """

print ('Bem vindo a calculadora de Bhaskara ')
print ('Me informe os 3 numeros a seguir')

valorA = float(input('Digite o valor A'))
valorB = float(input('Digite o valor B'))
valorC = float(input('Digite o valor C '))


delta = (valorB ** 2 ) - 4 * valorA  * valorC
print ('Seu valor de delta seria',delta)
raizdedelta = delta ** 0.5

xP1 = -(valorB)
xP2 = xP1 + raizdedelta

print(xP2)

""" # Se o valor de Δ for maior que zero (Δ > 0), a equação terá duas raízes reais e distintas.
if delta > 0 

#Se o valor de Δ for igual a zero (Δ = 0), a equação apresentará uma raiz real.
elif  delta == 0

#Se o valor de Δ for menor que zero (Δ<0), a equação não possui raízes reais.    
elif delta < 0 """


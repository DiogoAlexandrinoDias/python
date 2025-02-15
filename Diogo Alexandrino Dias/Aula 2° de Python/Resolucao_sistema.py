
import math

print ('calculadora de Bhaskara')

a = float(input('Digite o valor de A'))
b = float(input('Digite o valor de B'))
c = float(input('Digite o valor de C'))

delta = b**2 - 4 * a * c
print('Delta',delta)

raiz_delta = math.sqrt(delta) 

x1= (-b + raiz_delta) / (2 *a)
x2= (-b - raiz_delta) / (2 *a)

print('valor x1',x1)
print('valor x2',x2) 
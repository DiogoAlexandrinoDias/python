#calculadora de IMC
""" Solicite o peso en Kg e altura do usuario em metros
    Calcule IMc  (indice de nassa corporal)
     peso / (altura * altura)  """

print ('Digite o seu peso em Kg')
Kg = float(input())
print ('Digite o sua altura em Cm')
Cm = float(input())

divisao = Kg / ( Cm * Cm )

print ('seu IMC e ',divisao )
if divisao <= 18.5 :
    print('Abaixo do normal')
elif divisao >= 18.5 and divisao <= 24.9:
    print('Normal')
elif divisao >= 24.9 and divisao <= 29.9:
    print('Sobrepeso')
elif divisao >= 29.9  and divisao <= 34.9:
    print('Obesidade grau I')
elif divisao >= 34.9 and divisao <= 39.9:
    print('Obesidade grau II')
elif divisao >= 39.9 :
    print ('Obesidade grau III')
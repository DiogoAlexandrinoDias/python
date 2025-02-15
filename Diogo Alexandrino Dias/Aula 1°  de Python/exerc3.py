# verificar se é imapr ou par 
""" 
Digite ym nuemro interio 
Virifique se o numero é impar ou  par
Escreva a mesangem corespondente
 """
print ('seja bem vindo ao sistema imporpar')
print ('Digite o nimero correspondente')
numero = int(input())

resto = numero % 2 #10 / 2 = 0

if resto != 0 :
    print('e um numero impar')
else :
    print ('e um numero par')
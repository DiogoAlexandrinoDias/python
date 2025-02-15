""" 
vericar se uma palavra e uma um palindromo
caso  seja, exiba é palidromo
caso nãos eka exiba não e um palindromo
a verificando de ser case sensitive



valendo = a barra de chocolate  """

palavra = input ('Digite a palavra e vera se e palindrome ou não')

palavra = palavra.lower()

if palavra == palavra[::-1]:
    print(palavra,'e uma palindrome')
else:
    print(palavra,'não e um palindrome')
""" palavra = input().lower().strip()replace(' ', '') print(palavra) """
#desenvolva uma aplicacao que leia o comprimento de tres retas
#e diga ao usuario se elas podem ou nao formar um triangulo.
#| b - c | < a < b + c 
#| a - c | < b < a + c 
#| a - b | < c < a + b 
"""Resolucao Curso em video python
print("-="*20)
print("Analisador de Triangulo")
print("-="*20)
r1 = float(input("insira o comprimento da primeira reta "))
r2 = float(input("insira o comprimento da segunda reta ")) 
r3 = float(input("insira o comprimento da terceira reta "))
if r1 < r2 + and r2 < r3 + r3 and r3 < r1 + r2:
    print("Os seguimentos podem formar um triangulo!")
else:
    print("Os segmentos acima nao podem formar um triangulo")
"""

a = float(input("insira o comprimento da primeira reta "))
b = float(input("insira o comprimento da segunda reta ")) 
c = float(input("insira o comprimento da terceira reta "))


triangulo = (b - c) < a < (b + c)
triangulo2 = (a - c) < b < (a + c) 
triangulo3 = (a - b) < c < (a + b)

teste = triangulo, triangulo2, triangulo3

if triangulo == True and triangulo2 == True and triangulo3 == True:
    print("As retas informadas formam um triangulo!")
    
else:
    (triangulo, triangulo2, triangulo3 == False)
    print("As retas informadas nao formam um triangulo")
    
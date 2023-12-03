#desenvolva uma aplicacao que leia o comprimento de tres retas
#e diga ao usuario se elas podem ou nao formar um triangulo.
#| b - c | < a < b + c 
#| a - c | < b < a + c 
#| a - b | < c < a + b 

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
    
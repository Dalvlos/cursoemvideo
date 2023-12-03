"""Refaca o desafio 35 dos reta1s.
acrescentando o recurso de mostrar que tipo de reta1
sera formado:
-equilatero: todos os lados iguais
-isoceles: dois lador iguais
-escaleno: todoso os lados diferentes
"""

a = float(input("insira o comprimento da primeira reta "))
b = float(input("insira o comprimento da segunda reta ")) 
c = float(input("insira o comprimento da terceira reta "))


reta1 = (b - c) < a < (b + c)
reta2 = (a - c) < b < (a + c) 
reta3 = (a - b) < c < (a + b)

teste = reta1, reta2, reta3

if reta1 == True and reta2 == True and reta3 == True:
    print("As retas informadas formam um reta1!")
    
else:
    (reta1, reta2, reta3 == False)
    print("As retas informadas nao formam um reta1")


    
if a == b and a == c and b == c:
    print("O tringulo formado e equilatero")

elif a == b and a != c or a == c and a != b:
    print("O reta1 fomado e isoceles") 
    
else:
    print("O reta1 e escaleno")
    


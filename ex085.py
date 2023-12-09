"""

Crie um programa onde o usuario possa digitar 
sete valores numericos e cadastre-os em uma lista unica
que mantenha separados os valores pares e impares.
No final, mostre os valores pares e impares em ordem crescente



numeros = []
contador = 0
while contador < 7:
    numero = int(input('Enter number: '))
    
    if numero % 2 == 0:
        numeros.insert(0, numeros)
    else:
        numeros.append(numeros)  
    contador += 1
print("Lista final:", numeros)

"""


lista = []

for c in range(1, 7):
    num = int(input("Digite o valor: "))
    if num % 2 ==0:
        lista.insert(0, num)
        
    else:
        lista.append(num)
    
print(lista)
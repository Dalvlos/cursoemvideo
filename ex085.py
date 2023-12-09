"""

Crie um programa onde o usuario possa digitar 
sete valores numericos e cadastre-os em uma lista unica
que mantenha separados os valores pares e impares.
No final, mostre os valores pares e impares em ordem crescente

"""

numeros = []
for _ < 8:
    numero = int(input('Enter number: '))
    
    if numero % 2 == 0:
        numeros.insert(0, numeros)
    else:
        numeros.append(numeros)  

print("Lista final:", numeros)
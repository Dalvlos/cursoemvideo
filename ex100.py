"""
faça um programa que tenha uma lista chamada
numeros e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5
numeros e vai colocá-los dentro de uma lista
e a segunda função vai mostrar a soma entre
todos os valores PARES sorteados pela função
anterior.

make a program that has a list called
numbers and two functions called sorteia() and
sumPar(). The first function will draw 5
numbers and will place them in a list
and the second function will show the sum between
all EVEN values drawn by the function
previous.

"""
from random import randint 
from time import sleep

def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end=" ")
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f"{n}", end=" ", flush=True)
        sleep(0.1)
    print("Sorteio finalizado")

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor %2 == 0:
            soma += valor
    print(f"Somando os valores pares de {lista}, temos {soma}")
    
    
numeros = list()
sorteia(numeros)
somaPar(numeros)

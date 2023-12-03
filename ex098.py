""""
Faça um programa que tenha uma função
chamada contador(), que receba parâmetros
inicio, fim e passo e realiza a contagem.

seu programa tem que realizar três contagens
através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada.

"""
from time import sleep

def contador(i, f, p):
    
    if p < 0:
        p *= -1
    if p == 0:
        p=1
    
    print("=-" * 20)
    print(f"contagem de {i} ate {f} de {p} em {p}")
    sleep(1)
    
        
    
    if i < f:
        contador = i
        while contador <= f:
            print(f"{contador}", end= " ", flush=True)
            sleep(0.5)
            contador += p
        print(" Fim!")
    else:
        contador = i
        while contador >= f:
            print(f"{contador} ", end=" ", flush=True)
            sleep(0.5)
            contador -= p
        print(" Fim!")
 
contador(1, 10, 1)
contador(10, 0, 2)
print("=-"*20)

print("Personalize a contagem")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contador (inicio, fim, passo)
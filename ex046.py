"""
Faca uma aplicacao que mostre na tela uma contagem regressiva
para o estouro de fogos de artificio, indo de 10 ate 0, 
com uma pausa de 1 segundo entre elas. 

"""
from time import sleep

for segundo in range(10, -1, -1):
    print(segundo)
    sleep(1)
print("***** Feliz ano novo *****")
"""
faça um programa que tenha uma função
chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem
com tamanho adaptável.

ex.
escreva(ola mundo!)

saida:
____________
Ola, Mundo!
____________
"""

def escreva(a):
    letras = len(a) + 4
    linhas = letras * "="
    print(linhas) 
    print(f"  {a}")
    print(linhas)

#Main Aplication 
a = str(input("Escreva seu nome: "))
escreva(a)
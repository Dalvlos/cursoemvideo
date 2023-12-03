#faca um programa que leia um ano qualquer
#e mostre se e ano bissexto ou nao.

""" resolucao da aula do curso em video python/guanabara
from datetime import date

ano = int(input("Que ano quer analisar? insira 0 para analisar o ano atual!"))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} e bissexto".fortmat(ano))
else:
    print("O ano {} nao e bissexto".format(ano))
"""


from calendar import isleap

ano = int(input("digite um ano: "))
print("Analisando o ano {}".format(ano))
print("...")
teste = ano
bisesto = isleap(teste)

if bisesto == True:
    print("O ano {} e bissexto.".format(ano))
else:
    print("O ano {} nao e bisexto.".format(ano))
    

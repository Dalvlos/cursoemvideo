"""faca uma aplicacao que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:
-Se ele ainda ira se alistar ao servico militar. 
-Se e o momento de se alistar.
-Se ja passou o tempo do alistamento.

Sua aplicacao tambem devera mostrar o tempo que falta 
ou o prazo que excedido do alistamento militar obrigatorio.
"""

from datetime import date

ano_de_nascimento = int(input("Insira seu ano de nascimento: "))

data_atual = date.today()
ano_corrente = data_atual.year

idade = ano_corrente - ano_de_nascimento

calculo_de_idade_excedente = idade - 18
calculo_idade = 18 - idade 

if calculo_de_idade_excedente >= 1: 
    print("Voce excedeu a idade para o alistamento militar obrigatorio em {} anos".format(calculo_de_idade_excedente))
elif calculo_de_idade_excedente == 0: 
    print("Parabens! Este ano devera se alistar no servico militar obrigatorio.")
elif idade <= 17: print("Voce ira aguardar {} ano(s) para o alistamento!".format(calculo_idade))

"""
reposta do curso em video


"""

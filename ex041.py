"""A confederacao nacional de natacao precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com sua idade:
-ate 9 anos:MIRIM
-ate 14 anos:INFANTIL
-ate 19 anos:JUNIOR
-ate 20 anos:SENIOR
-acima:MASTER
"""

"""
from datetime import date 
import datetime

dia = int(input('Dia: ')) 
mes = int(input('Mes: ')) 
ano = int(input('Ano: '))

data = datetime.date(ano, mes, dia) 
diferenca = (data.today() - data) 
rslt = (diferenca / 365.25)
idade = (rslt.days)

print('Você nasceu {}/{}/{} e tem {} anos'.format(data.day, data.month, data.year, rslt.days))

if idade <= 9:
    print("O atleta participara na categoria MIRIM")

elif idade > 9 and idade <= 14:
    print("O atleta participara da categoria INFANTIL")

elif idade > 14 and idade <= 19:
    print("O atleta participara na categoria JUNIOR")

elif idade == 20:
    print("O atleta participara na categoria SENIOR")

elif idade > 20:
    print("O atleta participara na categoria MASTER")
"""

from datetime import date
import datetime

dataatual = date.today().year

ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = dataatual - ano_nascimento

print ("O(a) atleta tem {} anos de idade".format(idade))

if idade <= 9:
    print("Classificado na categoria MIRIM")
elif idade <= 14:
    print("Classificado na categoria INFANTIL")
elif idade <= 19:
    print("Classificado na categoria JUNIOR")
elif idade <= 25:
    print("Classificado na categoria SENIOR")
else:
    print("Classificado na categoria MASTER")
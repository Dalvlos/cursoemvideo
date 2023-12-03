"""Crie uma aplicacao que leia duas notas de um aluno 
e calcule sua media. mostrando uma mensagem no final,
de acordo com a media obtida:
-media abaixo de 5.0: REPROVADO
-media entre 5.0 e 6.9: RECUPERACAO
-media 7.0 ou superior: APROVADO
"""

from ast import If, Or


primeira_nota = float(input("digite a primeira nota: "))

segunda_nota = float(input("digite a segunda nota: "))

m_nota = (primeira_nota + segunda_nota) / 2

print(m_nota)

if m_nota >= 7:
    print("APROVADO!")

elif m_nota < 5:
    print("REPROVADO!")

elif m_nota < 7 and m_nota >= 5:
    print("RECUPERACAO!")

""" SOLUCAO CURSO EM VIDEO

n1 = float(input("Digite a nota do aluno: "))
n2 = float(input("Digite a nota do aluno: "))

media = (n1 + n2) / 2

print("O aluno tirou as notas {:.1f} e {:.1f}, a media obtida foi de {:.1f}".format(n1, n2, media))

if media >= 5 and media < 7:
    print("O aluno esta em RECUPERACAO!")

elif media < 5:
    print("O aluno esta REPROVADO!")

elif media >= 7:
    print("O aluno esta APROVADO!")

"""
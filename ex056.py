"""
Desenvolva uma aplicacao que leia 
o nome, idade e sexo de 4 pessoas
Ao final mostre:
-A media de idade do grupo.
-Qual o nome do mais velho.
-Quantas mulheres tem menos de 20 anos.
"""

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ""
totalmulhermenos20 = 0

for p in range(1, 5):
    nome = str(input("Nome do usuario: ")).strip()
    idade = int(input("Qual a idade do usuario: "))
    sexo = str(input("Escolha o genero [M/F]: ")).strip()      
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in "Ff" and idade < 20:
        totalmulhermenos20 += 1
        
mediaidade = somaidade / 4 
print("A media de idade das pessoas e de {}".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}.".format(maioridadehomem, nomemaisvelho))
print("{} mulheres tem menos de 20 anos".format(totalmulhermenos20))
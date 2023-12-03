"""

Faca uma aplicacao que leia o sexo de uma pessoa
mas so aceite os valores "M" ou "F".
Caso esteja errado, peca a digitacao novamente
ate ter um valor correto.

"""


sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados invalidos! Por favor digite seu sexo. [M] para masculino ou [F] para feminino: ")).strip().upper()[0]
print("sexo {} registrado com sucesso!".format(sexo))
        
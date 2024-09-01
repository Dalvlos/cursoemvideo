""" 

Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionario se por acaso a CTPS for diferente de zero
o dicionario recebera tambem o ano da contratacao e o salario.
Calcule e acrescente, alem da idade, com quantos anos a pessoa ira se aposentar.

"""

import datetime


anoAtual = datetime.date.today().year

cadastro_Funcionario = {
    'nome' : '',
    'anoDeNascimento' : None,
    'carteiraDeTrabalho' : None,
    'idade' : None,
    'anoDeContratacao' : None,
    'salario' : None,
    'anosParaContribuirAposentadoria' : None,
}

cadastro_Funcionario['nome'] = input("Digite o nome: ")
cadastro_Funcionario['anoDeNascimento'] = int(input("Digite o ano de nascimento: "))
cadastro_Funcionario['carteiraDeTrabalho'] = int(input("Digite o número da carteira de trabalho: "))
if cadastro_Funcionario['carteiraDeTrabalho'] != 0:
    cadastro_Funcionario['idade'] = anoAtual - cadastro_Funcionario['anoDeNascimento']
    cadastro_Funcionario['anoDeContratacao'] = int(input("Digite o ano de contratação: "))
    cadastro_Funcionario['salario'] = float(input("Digite o salário: "))
    cadastro_Funcionario['anosParaContribuirAposentadoria'] = 65 - cadastro_Funcionario['idade']



print("\nCadastro do Funcionário:")
for chave, valor in cadastro_Funcionario.items():
    print(f"{chave}: {valor}")
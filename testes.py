"""def contador(* num):
    tam = len(num)
    print(f"Valores recebidos {num} e ao todos sao {tam} numeros!")


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)"""


"""def dobra(lst):

    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

numero = 75
dezena = numero // 10
unidade = numero % 10
print("Dezena:", dezena)
print("Unidade:", unidade)

conta = 15000 / 21
print(conta)

frase = str("paralelepipedo")
vogais = str("aeiou")
totalVogais = " "
contador = 0
for i in frase:
    if i in vogais:
        totalVogais = i 
        contador += 1
print(contador)

minha_string = "Olá, mundo!"
lista_de_caracteres = list(minha_string)
print(lista_de_caracteres)


#!/bin/python

#!/bin/python3

#!/bin/python3

import math
import os
import random
import re
import sys


class Multiset:
    
    def __init__(self):
        self.M=[]
    
    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.M.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if len(self.M):
            if val in self.M:
                self.M.remove(val)

    def __contains__(self, val):
        if val in self.M:
            return True
        # returns True when val is in the multiset, else returns False
        return False
    
    def __len__(self):
        # returns the number of elements in the multiset
        
        return len(self.M)
if __name__ == '__main__':
    
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
    
if __name__ == '__main__':
    n = int(input().strip())
if n <= 2:
    print('Weird')
elif n >= 2 and n <= 5:
    print('Not Weird')
elif n >= 6 and n <= 20:
    print('Weird')
else:
    print('Not Weird')
    
def numeros_primos_intervalo(inicio, fim):
    numeros_primos = []

    for num in range(inicio, fim + 1):
        if num > 1:
            eh_primo = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    eh_primo = False
                    break
            if eh_primo:
                numeros_primos.append(num)

    return numeros_primos

primos_ate_100 = numeros_primos_intervalo(1, 100)
print(primos_ate_100)

def cadastro():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    sexo = input("Digite seu sexo: ")
    email = input("Digite seu endereço de email: ")
    
    dados_usuario = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo,
        'email': email
    }
    
    return dados_usuario

# Chamando a função e recebendo os dados do usuário
informacoes_usuario = cadastro()

# Exibindo os dados coletados
print("Dados do usuário:")
for chave, valor in informacoes_usuario.items():
    print(f"{chave}: {valor}")

import sqlite3

# Conectar ao banco de dados (ou criar um novo se não existir)
conexao = sqlite3.connect('dados_usuarios.db')

# Criar uma tabela para armazenar os dados do usuário
conexao.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        sexo TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

def cadastro():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo: ")
    email = input("Digite seu endereço de email: ")
    
    # Inserir os dados na tabela
    conexao.execute('''
        INSERT INTO usuarios (nome, idade, sexo, email)
        VALUES (?, ?, ?, ?)
    ''', (nome, idade, sexo, email))

    # Commit para salvar as mudanças no banco de dados
    conexao.commit()
    
    return {
        'nome': nome,
        'idade': idade,
        'sexo': sexo,
        'email': email
    }

# Chamando a função para coletar os dados do usuário
informacoes_usuario = cadastro()

# Exibindo os dados coletados
print("Dados do usuário:")
for chave, valor in informacoes_usuario.items():
    print(f"{chave}: {valor}")

# Fechar a conexão com o banco de dados quando não for mais necessário
conexao.close()
"""

lista_principal = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

resultado = [[valor * 2 if valor % 2 == 0 else valor * 3 for valor in lista] for lista in lista_principal]

print(resultado)
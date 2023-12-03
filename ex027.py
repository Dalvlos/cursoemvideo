###faca um software que leia o nome completo de uma pessoa.
#mostrando em seguida o primeiro e o ultimo nome separadamente
#ex: Ana Maria de Souza
#primeiro = Ana
#segundo = Souza

n = str(input("Digite nome e sobrenome: ")).strip()
nome = n.split()
print("Ola, como vai!?")
print("seu primeiro nome e {}".format(nome[0]))
print("seu ultimo nome e {}".format(nome[len(nome)-1]))

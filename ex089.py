"""

crie um programa que leia nome e duas notas de varios alunos
e guarde tudo em uma lista composta. No final mostre um boletim
contendo a media de cada um e permita que o usuario possa mostrar
as notas de cada aluno individualmente.

"""
class boletimDoAluno:
    def __init__(self):
        self.aluno = None
        self.nota1 = None
        self.nota2 = None

    def alunos(self):
        self.aluno = str(input("Nome do Aluno: "))

    def notasBoletim(self):
        self.nota1 = float(input("Digite a primeira nota do aluno: "))
        self.nota2 = float(input("Digite a segunda nota do aluno: "))

    def calcularMedia(self):
        media = (self.nota1 + self.nota2) / 2
        return media
    
# Criando uma instância da classe
boletim = boletimDoAluno()

continuar = True
while continuar:
    # Solicitando o nome do aluno
    boletim.alunos()

    # Solicitando as notas do aluno
    boletim.notasBoletim()

    # Calculando e imprimindo a média do aluno
    media_do_aluno = boletim.calcularMedia()
    print(f"A média do aluno {boletim.aluno} é: {media_do_aluno}")

    resposta = input("Deseja cadastrar outro aluno? (S/N)")
    if resposta.lower() == "n":
        continuar = False

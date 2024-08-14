"""

Faca um programa que leia o nome a media de um aluno
guardando tambem a situacao em um dicionario. No final
mostre o conteudo da estrutura na tela.

"""
def aluno_nome_e_media():
    dadosDoAluno = {}
    
    alunoNome = str(input("Nome do aluno: "))
    alunoNota1 = float(input(f"Nota do aluno {alunoNome}: "))
    alunoNota2 = float(input(f"Segunda nota do aluno {alunoNome}: "))
    mediaNota = (alunoNota1 + alunoNota2) / 2

    dadosDoAluno ['alunoNome'] = alunoNome
    dadosDoAluno ['alunoNota1'] = alunoNota1
    dadosDoAluno ['alunoNota2'] = alunoNota2
    dadosDoAluno ['mediaNota'] = mediaNota
    return(dadosDoAluno)


aluno_nome_e_media()

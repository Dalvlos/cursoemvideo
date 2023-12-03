"""
faça um programa que tenha uma função
chamada area() que receba as dimensões de um terreno
retangular (largura e cumprimento) e mostre a
area do terreno.
"""

def area(largura, comprimento):
    a = largura * comprimento
    print(f" A area total do terreno {largura} x {comprimento} e de {a}m2.")


#programa principal
print("Controle de terrenos")
print("=-" * 20)
largura = float(input("Informe a laergura do terreno em m2: "))
comprimento = float(input( "informe o cumprimento do terreno em m2: "))
area(largura, comprimento)
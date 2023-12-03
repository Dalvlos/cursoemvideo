"""
Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai quitar o imovel.

calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30%
do salario ou entao o emprestimo sera negado."""
"""
"""


valor_casa = float(input("Valor do imovel: R$"))
salario_comprador = float(input("Salario do comprador(a):"))
numero_de_parcelas = int(input("Quantos anos de financiamento? ")) * 12

valor_parcelas = valor_casa / numero_de_parcelas

if valor_parcelas <= (salario_comprador / 100 * (30)):
    print("Financiamento aprovado! Total de  {:.0f} parcelas e pagamentos mensais de R${:.2f}.".format(numero_de_parcelas, valor_parcelas))
else:
    print ("Financiamento nao aprovado!")

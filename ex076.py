"""
Crie um programa que tenha uma tupla unica
com nome de produtos e seus respectivos precos, na sequencia.

No final mostre uma listagem de precos, organizando os dados 
em forma tabular.

from tabulate import tabulate

produtos = ('arroz', 20.00, 'feijao', 10.00, 'acucar', 7.00, 'detergente', 5.00, 'bolacha', 3.00)

table = tabulate(produtos, headers=["Produto", "Preco"], tablefmt="grid")

print(table)"""

produtos = ('arroz', 20.00, 
            'feijao', 10.00, 
            'acucar', 7.00, 
            'detergente', 5.00, 
            'bolacha', 3.00)
print('-'*40)
print('Lista de produtos e precos: ')
print('-'*40)
for item in range(0, len(produtos)):
    if item %2 == 0:
        print(f'{produtos[item]:.<30}', end='')
    else:
        print(f'R${produtos[item]:>10.2f}')

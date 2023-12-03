"""

Crie uma aplicacao onde o usuario digite uma expressao
qualquer que use parenteses. Seu aplicativo devera analisar se 
a expressao passada esta com os parenteses abertos e fechados na ordem correta.

"""

a = str(input('Digite uma expressao numerica: '))
pilha = []
for simb in a:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')    
if len(pilha) == 0:
    print('Sua expressao esta valida!')
else:
    print('Sua expressao eesta errada!')

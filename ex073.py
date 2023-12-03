"""
Crie uma tupla preenchida com os 
20 primeiros colocados da tabela 
do campeonato brasileiro de futebol.
na ordem de colocacao. depois mostre:
a)Apenas os 5 primeiros colocados.
b)Os ultimos 4 colocados da tabela.
c)Uma lista com os times em ordem alfabetica
d)Em que posicao na tabela esta o time do Fortaleza.


"""
times = ("Botafogo", "Palmeiras", "Gremio", "Flamengo", "Fluminense", 
        "Bragantino", "Athletico-PR", "Fortaleza", "Athletico-MG", 
        "Cuiaba", "Sao Paulo", "Cruzeiro", "Corinthians", 
        "Internacional", "Goias", "Bahia", "Santos", 
        "Vasco da Gama", "America-MG", "Coritiba")

print("=-"*40)
print (f"Lista de times: {times}")
print("=-"*40)
#No fatiamento de strings no print abaixo o ultimo elemento `e ignorado ao exibir a tupla no terminal.
print(f"Os 5 primeiros colocados: {times[0:5]}")
print("=-"*40)
print(f"Os 4 ultimos colocados: {times[-4:]}")
print("=-"*40)
print(f"Times em ordem alfabetica: {sorted(times)}")
print(f'O Fortaleza esta na {times.index("Fortaleza")+1}• posicao')

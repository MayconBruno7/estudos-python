"""
073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Bragantino.

"""

 
print("Classificação Brasileiro Série A")
	
times = ('Palmeiras', 'Flamengo', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Internacional',	
		'Atlético-MG', 'América-MG', 'Bragantino', 'Santos', 'São Paulo', 'Botafogo', 'Goiás', 'Ceará',
		'Fortaleza','Cuiabá','Avaí','Coritiba','Atlético','Juventude')

print("=" * 50)
print(f'Lista de times: {times}')
print("=" * 50)
#print(f"Os 5 primeiros colocados são: {times[0:5]}")
#print(f"Os quatro ultimos são os times:{times[-4:]}")
#print(f"Times em ordem alfabetica: {sorted(times)}")
#print(f"O Bragantino está na posição: {times.index('Bragantino') + 1}")

#for t in range(len(times) - 20, len(times) - 15):
#	print(times[t])

#for t in range(len(times) - 4, len(times)):
#	print(times[t])

#for t in range(len(times) - 19, len(times) - 18):
#	print(f"Times em ordem alfabetica: {sorted(times)}")



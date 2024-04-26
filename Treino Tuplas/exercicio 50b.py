"""
AUTOR.....: Maycon Bruno
DATA/HORA.: 17/08/2022 as 13:41
FINALIDADE: 50) Crie uma tupla com a classificação 
				dos 20 pilotos de formula 1 do
				campeonato de 2019 na ordem de 
				classificação:

				a) Exiba a lista de classificação completa dos pilotos;
				b) Exiba os 3 primeiros colocados;
				c) Exiba os 4 últimos colocados;
				d) Exiba o índice onde está o piloto “K. Raikkonen”;
"""

pilotos = (
	"Lewis Hamilton",
	"Valtteri Bottas",
	"Max Vestappen",
	"Rubens Barrichelo",
	"Charles Leclerc",
	"Sebastian Vettel",
	"Carlos Sainz Jr.",
	"Pierre Gasly",
	"Alexander Albon",
	"Daniel Riccardo",
	"Sergio Perez",
	"Lando Norriz",
	"Kimi Haikkenen",
	"Danill Kayat",
	"Nico Hulkemberg",
	"Lance Stroll",
	"Kevin Magnussen",
	"Antonio Giovinazzi",
	"Romain Grosjan",
	"Robert Kubica",
	"George Russell"
	)

print("=" *50)
print("Classificação dos pilotos de F1 2019")

for posicao, nome in enumerate(pilotos):
	print(f"{n + 1:>2.0f} - {pilotos[n]}")

print("-" * 40)
print()
print("Três primeiros colocados no campeonato")
print()

for n in range(3):
	print(f"{n + 1:>2.0f} - {pilotos[n]}")

print("-" * 40)
print()
print("Quatro ultimos colocados no campeonato")
print()

for x in range(len(pilotos - 4), len(pilotos))
	print(f"{n + 1:>2.0f} - {pilotos[x]}")


print()
print("Buscando piloto:")

while True:

	busca = input("Informe o nome do piloto:")

	if busca == "":
		break

	achou = False

	for n in range(len(pilotos)):
		if pilotos[n].upper() == busca.upper():
			print(f"O piloto {busca} está localizado no indice {n}, e ficou na posição {n + 1} no campeonato")
			achou = True
			break

	if not achou:
		print("Piloto não localizado.")

	print("-" * 40)



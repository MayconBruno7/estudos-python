from random import shuffle

participantes = ["Joaquim", "Maria", "Heitor", "Daniel", "Ana", "Carlos"]

shuffle(participantes)

print("Ordem de apresentação:")
for i in range(len(participantes)):
    print(f"{i + 1}º: {participantes[i]}")
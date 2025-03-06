from random import randint


listaAluno = ["Joaquim", "Maria", "Heitor", "Daniel"]

num_aleatorio = randint(0,3)

print('============================')
print('Numero sorteado: {0}' .format(num_aleatorio))
print(listaAluno[num_aleatorio])
print('============================')

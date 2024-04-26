"""
AUTOR.....: Maycon Bruno 
DATA/HORA.: 23/09/2022 as 20:05
FINALIDADE: (4,0 pontos). Solicite ao usuário a entrada 
			do nome e da altura de 11 jogadores, armazene 
			estes dados em listas. Ao final, apresente:
				a) Uma listagem com os dados, nome e altura 
				para os 11 jogadores titulares.
				b) Nome e a altura do jogador mais alto do time.
				c) Nome, altura e índice na lista para o 
				jogador mais baixo do time (menor estatura)
"""

nome = list()
altura = list()

indMaisAlto = -1
indMaisBaixo = -1

for x in range(3): 

    nome.append(input('Informe o nome do jogador: '))
    altura.append(int(input('Informe a altura do jogador(cm): ')))

    if x == 0:
        indMaisAlto = x
        indMaisBaixo = x

    else:
        if altura[x] < indMaisBaixo:
            indMaisBaixo = x
        
        if altura[x] > indMaisAlto:
            indMaisAlto = x
     

print()
print('Listando os jogadores')
print('Nome                 Altura')
print()

for x in range(len(nome)):
    print(f'{nome[x].ljust(20)} {altura[x]}')

print(f'O jogador mais alto do time é {nome[indMaisAlto]} e tem {altura[indMaisAlto]}')
print(f'O jogador mais baixo do time é {nome[indMaisBaixo]} e tem {altura[indMaisBaixo]} e está no indice {indMaisBaixo}')

    
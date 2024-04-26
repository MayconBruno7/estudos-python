"""
Autor: Maycon Bruno
Data: 01/10/2022 ás 11:32

    Faça um programa que solicite ao usuario o nome e a idade de 5 pessoas armazene em uma matriz e depois mostre esssas pessoas na tela do usuario,
    em ordem alfabetica.

"""

pessoas = []

for x in range(5):
    print(f'Informe os dados para a pessoas {str(x + 1)}')
    nome = (input('Informe o nome: '))
    idade = int(input('Informe a idade: '))

    pessoas.append([nome, idade])

for x in range(1, len(pessoas)):
    for y in range(len(pessoas) - 1, 0, -1):
        if pessoas[y][0] < pessoas[y - 1][0]:
            aux = pessoas[y]
            pessoas[y] = pessoas[y - 1]
            pessoas[y - 1] = aux

print()
print('Exibindo em ordem alfabetica')
print()
print('Nome                  Idade')
print()

for x in range(len(pessoas)):
    print(f'{pessoas[x][0]:<22}', end='')
    print(f'{pessoas[x][1]}')
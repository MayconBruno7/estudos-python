"""
AUTOR.....: Maycon Bruno
DATA/HORA.: 24/09/2022 as 13:25
FINALIDADE: Criar uma lista de ordenação para 5 pessoas (em ordem alfabetica) com suas respectivas idades utilizando o metodo bolha.

"""

nome = list()
idade = list()

print()
print('Ordenando as pessoas por ordem alfabetica')
print()

for x in range(5):

    nome.append(input('Informe o nome da pessoa: '))
    idade.append(int(input('Informe a idade da pessoa: ')))

    for x in range(1, len(nome)):
        for y in range(len(nome) - 1, 0, -1):
            if nome[y] < nome[y - 1]:
                auxNome = nome[y]
                nome[y] = nome[y - 1]
                nome[y - 1] = auxNome 

                auxIdade = idade[y]
                idade[y] = idade[y - 1]
                idade[y - 1] = auxIdade

print()
print('Exibindo a lista ordenada em ordem alfabetica com a idade de cada pessoa na frente')
print()

for x in range(len(nome)):
    print(f'{nome[x]} - {idade[x]}')

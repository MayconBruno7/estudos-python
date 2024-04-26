"""
Autor: Maycon Bruno
Data: 02/10/2022 ás 09:54

    Faça um programa que solicite ao usuario o nome e a idade de 5 alunos de uma turma armazene em uma lista e depois adicione essa lista dentro de uma matriz e ainda mostre esssas pessoas na 
    tela do usuario em ordem alfabetica.

"""

aluno = []
turma = []

for x in range(1):
    print(f'Informe os dados para a pessoa {str(x + 1)}')
    aluno.append(input('Informe o nome da pessoa: '))
    aluno.append(int(input('Informe a idade da pessoa: ')))

    turma.append(aluno[:])
    aluno.clear()

for x in range(1, len(turma)):
    for y in range(len(turma) - 1, 0, -1):
        if turma[y][0] < turma[y - 1][0]:
            aux = turma[y]
            turma[y] = turma[y - 1]
            turma[y - 1] = aux

print()
print('Exibindo a lista em ordem alfabetica')
print()
print('Nome                Idade')

for x in range(len(turma)):
    print(f'{turma[x][0]:<22}', end='')
    print(f'{turma[x][1]}')
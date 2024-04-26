"""
    Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

"""

alunos = []

notas = []

for c in range(1):
    print(f'Informe o dado para o aluno {c + 1}')

    nome = input('Informe o nome do aluno: ')
    
    soma = 0

    for l in range(4):
        print(f'BIMESTRE {l + 1}')
        notas.append(float(input('Informe a nota do aluno: ')))
        soma += notas[l]
        print()

    alunos.append([nome, (soma/4), notas[:]])
    notas.clear()
  

print()
print('Exibindo os alunos e as suas médias')
print()
print('Nome                 Média B1  B2  B3  B4')

for aluno in alunos:
    print(f'{aluno[0]:<17}', end='  ')
    print(f'{aluno[1]:>5}', end='   ')

    notas = aluno[2]

    for x in range(len(notas)):
        print(f'{notas[x]:>1.1f}', end=' ')
    print()
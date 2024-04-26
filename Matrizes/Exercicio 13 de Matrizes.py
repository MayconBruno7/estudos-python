"""
Nome: Maycon Bruno
Data: 04/10/2022 ás 10:48

   13)  Desenvolver um programa que efetue a leitura dos
        nomes e idade de 5 alunos e também de suas 4 notas
        bimestrais. Ao final, o programa deverá apresentar o nome,
        idade, suas médias e a média geral dos 5 alunos. Armazenar
        os dados em uma matriz.

"""
matrizAlunos = []
nota         = []

for x in range(1):
    print(f'Informe os dados para o aluno {x + 1}')
    nome  = str(input('Informe o nome do aluno: '))
    idade = (int(input('Informe a idade do aluno: ')))

    soma  = 0 

    for y in range(4):
        nota.append(float(input('Informe a nota do bimestre' + str(y + 1) + ': ')))
        soma += nota[y]

    matrizAlunos.append([nome, idade, (soma/4), nota[:]])
    nota.clear()
print()


print('Nome                  Idade Média B.1  B.2  B.3  B.4')

for aluno in matrizAlunos:
    print(f'{aluno[0]:<20}', end='')
    print(f'{aluno[1]:>7.0f}', end='')
    print(f'{aluno[2]:>6.2f}', end='')
    
    notas = aluno[3]

    for n in range(len(notas)):
        print(f'{notas[n]:>5.2f}', end='')
    print()


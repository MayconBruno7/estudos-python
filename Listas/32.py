"""
-------------------------------------------------
DATA/HORA..: 13/08/2022 às 10:16
ESCRITO POR: Maycon Bruno
FINALIDADE.: 32) Desenvolva um algoritmo que solicite ao usuário que 
                informe o nome, sexo e idade de 10 alunos. No final 
                apresente:

                - O nome do aluno mais novo.
                - O nome do aluno mais velho do sexo Masculino.
                - A média de idade das alunas.
-------------------------------------------------
"""

repeat = 0

alunoNovoNome = ''
alunoVelhoNome = ''

alunoNovo = 0
alunoVelho = 0

somaIdadeAlunas = 0
qtdeAlunas = 0

while repeat <= 3:

    name = input("Informe o nome do aluno:")
    idade = int(input("Informe a idade do aluno:"))

    while True:

        print("Favor informar (M) para masculino e (F) para feminino.")

        sexo = input("Informe o sexo do aluno:")

        if sexo.upper() == "M" or sexo.upper() == "F":
            break
        else:
            print("Favor informar um sexo válido!")


    if idade < alunoNovo or repeat == 0:
            alunoNovo = idade 
            alunoNovoNome = name
    if sexo.upper() == "M":
        if idade > alunoVelho:
            alunoVelho = idade 
            alunoVelhoNome = name
    else:
         somaIdadeAlunas += idade 
         qtdeAlunas += 1

    repeat += 1

print("=" * 50)
print()
print(f"O nome do aluno mais novo é {alunoNovoNome} e tem {alunoNovo} anos de idade.")
print(f"O aluno mais velho tem {alunoVelho} anos de idade e se chama {alunoVelhoNome}.")
print(f"A média de idade das alunas é {(somaIdadeAlunas / qtdeAlunas):<3.0f}")
print()
print("=" * 50)


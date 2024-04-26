"""
-------------------------------------------------
DATA/HORA..: 27/06/2022 às 14:11
ESCRITO POR: Maycon Bruno
FINALIDADE.: 32) Desenvolva um algoritmo que solicite ao usuário que 
                informe o nome, sexo e idade de 10 alunos. No final 
                apresente:

                - O nome do aluno mais novo.
                - O nome do aluno mais velho do sexo Masculino.
                - A média de idade das alunas.
-------------------------------------------------

"""

nome = (input("Informe o nome:"))
idade = int(input("Informe a idade:"))
sexo = (input("Informe o sexo (M) para masculino e (F) para feminino:"))

aluNovoNome = ""
aluVelhoIdade = 0

alunoVelhoNome = ""
aluNovoIdade = 0
mediAlunas = 0
qtdAlunas = 0

repeat = 1 

while repeat <= 3:

    nome = (input("Informe o nome:"))
    idade = int(input("Informe a idade:"))

    while True:

        sexo = (input("Informe o sexo (M) para masculino e (F) para feminino:"))

        if sexo.upper() == "M" or sexo.upper() == "F":
            break
        else:
            print("Sexo é inválido!")

    if idade < aluNovoIdade or repeat == 1:
        aluNovoNome   = nome
        aluNovoIdade  = idade

    if sexo.upper() == "M":
        if idade > aluVelhoIdade:
            alunoVelhoNome = nome
            aluVelhoIdade  = idade

    else: 
        qtdAlunas  += idade
        mediAlunas += 1

    repeat += 1

print("=" * 50)
print(f"Aluno mais novo é {aluNovoNome} e tem {aluNovoIdade} ano(s)")
print(f"O Aluno mais velho do sexo masculino é {alunoVelhoNome} e tem {aluVelhoIdade} ano(s)")
print(f"A média de idade das alunas é {(qtdAlunas / mediAlunas):<3.0f}") 
print("=" * 50)


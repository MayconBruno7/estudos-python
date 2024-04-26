"""
-------------------------------------------------
DATA/HORA..: 26/06/2022 às 15:33
ESCRITO POR: Maycon Bruno
FINALIDADE.: 26) Tendo como dados de entrada a altura e o sexo 
                de uma pessoa, construa o programa em Python e 
                que calcule seu peso ideal, 
                utilizando as seguintes fórmulas:
                    Para homens: (72.7*h) - 58
                    Para mulheres: (62.1*h) - 44.7, onde h = altura
-------------------------------------------------

"""

sexo = input("Informe o sexo (M) para masculino e (F) para feminino:")
altura = float(input("Informe a sua altura:"))

if sexo.upper == "M":
    pesoIdeal = (72.7 * altura) - 58
elif sexo.upper == "F":
    pesoIdeal = (62.1 * altura) - 44.7
else:
    print ("Sexo informado inválido!")

if pesoIdeal != 0:
    print("========")
    print("Seus peso ideal é ", pesoIdeal)
    print("========")
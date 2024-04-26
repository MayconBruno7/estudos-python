"""
-------------------------------------------------
DATA/HORA..: 10/08/2022 às 15:28
ESCRITO POR: Maycon Bruno
FINALIDADE.: 26) Tendo como dados de entrada a altura e o sexo 
                de uma pessoa, construa o programa em Python e 
                que calcule seu peso ideal, 
                utilizando as seguintes fórmulas:
                    Para homens: (72.7*h) - 58
                    Para mulheres: (62.1*h) - 44.7, onde h = altura
-------------------------------------------------
"""

altura = float(input("Nos informe a sua altura:"))
print("Digite (M) para masculino e (F) para feminino")
sexo = input("Informe o sexo:")

if sexo.upper() == "M":
    pesoIdeal = (72.7 * altura) - 58

elif sexo.upper() == "F":
    pesoIdeal = (62.1 * altura) - 44.7

else:
    print("=" * 50)
    print("")
    print("Favor informar um valor válido!")
    print("=" * 50)
    print("")

print(f"O seu peso ideal {pesoIdeal}")
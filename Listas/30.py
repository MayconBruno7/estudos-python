"""
-------------------------------------------------
DATA/HORA..: 12/08/2022 às 19:29
ESCRITO POR: Maycon Bruno
FINALIDADE.: 30) Elabore um algoritmo que, solicite a idade de um nadador,
                classifique-o em uma das seguintes categorias e informe sua
                categoria.

                Idade                   Categoria
                ---------------------------------
                5 até 7 anos            Infantil A
                8 até 10 anos           Infantil B
                11 até 13 anos          Juvenil A
                14 até 17 anos          Juvenil B
                Maiores de 18 anos      Adulto
-------------------------------------------------
"""

idade = int(input("Informe a sua idade:"))

if idade >= 5 and idade <= 7:
    print("Categoria: Infantil A")
elif idade >= 8 and idade <= 10:
    print("Categoria: Infantil B")
elif idade >= 11 and idade <= 13:
    print("Categoria: Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Categoria: Juvenil B")
elif idade >= 18:
    print("Categoria: Adulto")
else:
    print("Idade inválida, atleta não pode nadar!")

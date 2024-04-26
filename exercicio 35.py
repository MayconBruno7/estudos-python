"""
-------------------------------------------------
DATA/HORA..: 12/07/2022 às 11:08
ESCRITO POR: Maycon Bruno
FINALIDADE.: 35) Ler 20 números e ao final informar quantos número(s) est(á)ão
            no intervalo entre 10 (inclusive) e 50 (inclusive).
-------------------------------------------------
"""

qtdNumeros = 0 

for x in range(20):

    numero = int(input("Informe um valor"))

    if numero >= 10 and numero <=50:
        qtdNumeros += 1

print("=" * 50)
print("Você digitou", qtdNumeros, "no intervalo de 10 a 50!")
print("=" * 50)

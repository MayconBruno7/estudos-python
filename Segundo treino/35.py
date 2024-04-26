"""
-------------------------------------------------
DATA/HORA..: 14/08/2022 às 10:34
ESCRITO POR: Maycon Bruno
FINALIDADE.: 35) Ler 20 números e ao final informar quantos número(s) est(á)ão
            no intervalo entre 10 (inclusive) e 50 (inclusive).

-------------------------------------------------
"""
qtdIntervalo = 0 

for x in range(20):

    num = int(input("Informe um número:"))

    if num >= 10 and num <= 50:
        qtdIntervalo += 1


print()
print("=" * 50)
print(f"Foram digitados {qtdIntervalo} no intervalo de 10 a 50.")
print()
print("=" * 50)
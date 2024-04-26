"""
-------------------------------------------------
DATA/HORA..: 10/08/2022 às 15:06
ESCRITO POR: Maycon Bruno
FINALIDADE.: 19) Ler dois valores numéricos e apresentar a 
                 diferença do maior valor pelo menor valor.
-------------------------------------------------
"""

num1 = float(input("Informe um valor:"))
num2 = float(input("Informe mais um valor:"))

if num1 > num2:
     diferenca = num1 - num2
else:
     diferenca = num2 - num1

print("=" * 50)
print("")
print("")
print("")
print(f"A diferença do maior valor para o menor valor é de {diferenca}")
print("")
print("")
print("")
print("=" * 50)

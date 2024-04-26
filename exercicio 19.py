"""
-------------------------------------------------
DATA/HORA..: 26/06/2022 às 14:45
ESCRITO POR: Maycon Bruno
FINALIDADE.: 19) Ler dois valores numéricos e apresentar a 
                 diferença do maior valor pelo menor valor.
-------------------------------------------------

"""
maior = 0

v1 = int(input("Informe o primeiro valor:"))
v2 = int(input("Informe o segundo valor:"))

if v1 == v2:
	print("Os valore são iguais, portanto não há diferença.")
elif v1 > v2:
	diferenca = v1 - v2
	maior = v1
else: 
	diferenca = v2 - v1
	maior = v2

print("=" * 50)
print("O maior valor é", maior)
print("A diferença do maior valor pelo menor valor é igual á:", diferenca) 
print("=" * 50)
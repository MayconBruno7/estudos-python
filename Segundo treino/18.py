"""
-------------------------------------------------
DATA/HORA..: 10/08/2022 às 14:59
ESCRITO POR: Maycon Bruno
FINALIDADE.: 18) Ler dois valores para as variáveis A e B, e 
				efetuar as trocas dos valores de forma que a 
				variável A passe a possuir o valor da
				variável B e a variável B passe a possuir o 
				valor da variável A. Apresentar os valores trocados
-------------------------------------------------
"""

A = int(input("Informe um valor para a variavel (A):"))
B = int(input("Informe um valor para a variavel (B):"))

x = A
A = B
B = x 

print("=" * 50)
print(f"O valor de (A) agora é {A} e o valor de (B) agora é {B}")
print("=" * 50)
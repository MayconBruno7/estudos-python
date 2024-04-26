"""
-------------------------------------------------
DATA/HORA..: 13/06/2022 às 19:49
ESCRITO POR: Maycon Bruno
FINALIDADE.: 34) Leia 10 valores inteiros e determine:  
                    - Qual é o menor valor informado;
                    - Qual é o maior valor informado;
                    - A soma dos valores informados;
                    - A média dos valores informados.
-------------------------------------------------
"""
maior = 0
menor = 0
soma = 0

for x in range(10):

    num = int(input("Informe um valor:"))

    if x == 0:
        maior = num
        menor = num
    else:
        if num < menor:
            menor = num 
        else:
            maior = num

    soma += num

print()
print('=' * 50)
print()
print(f"O menor valor informado é {menor}")
print(f"O maior valor informado é {maior}")
print(f"A soma dos valores é {soma}")
print(f"A média entre os valores informados é de {(soma / 10):<12.2f}")
print()
print('=' * 50)
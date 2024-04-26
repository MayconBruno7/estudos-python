"""
	AUTOR.....: Maycon Bruno
	DATA/HORA.: 11/11/2022 AS 16:34
	
		22) Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar. 

"""

def teste(valor):
    
    if (valor % 2) == 0:
        return True

    else:
        return False
    
num = int(input('Informe o valor que deseja avaliar: '))

if teste(num):
    print(f'O valor {num} é par!!')

else:
    print('O valor informado não é par!!')
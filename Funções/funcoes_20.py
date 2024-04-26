"""
	AUTOR.....: Maycon Bruno
	DATA/HORA.: 11/11/2022 AS 15:37
	
		20) Escreva um procedimento chamado METADE que divida um valor do tipo real (passado como parâmetro) pela metade.

"""

def metade(val):
    return(val / 2)

valor = float(input('Informe o valor desejado: '))

print()
print(f'A metade de {valor} digitado é {metade(valor)}')
print()
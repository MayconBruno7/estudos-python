"""
	AUTOR.....: Maycon Bruno
	DATA/HORA.: 11/11/2022 AS 15:37
	
		21) Escreva uma função chamado TROCA que receba duas variáveis inteiras (X e Y) e troque o conteúdo entre elas

"""

def troca():
    global x, y
    
    aux = x
    x   = y
    y   = aux
    
x = int(input('Informe o valor para x: '))
y = int(input('Informe o valor para y: '))

troca()

print()
print(f'X: {x} ')
print()
print(f'Y: {y} ')
print()
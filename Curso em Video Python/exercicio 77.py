"""
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
 Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

 """

palavras = ('mouse', 'teclado', 'monitor', 'caixa de som', 'mesa', 'gabinete', 'placa de video',
'memoria ram', 'Fonte') 

for p in palavras:
	print(f'\nNa palavra {p} temos ', end="")

	for letra in p:
		if letra.lower() in 'aeiou':
			print(f'{letra} ', end="")

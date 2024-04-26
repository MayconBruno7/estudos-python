"""
	AUTOR.....: Maycon Bruno
	DATA/HORA.: 11/11/2022 AS 15:37
	
		19) Escreva um procedimento que receba uma string S e um inteiro positivo N e exiba a string S por N vezes seguidas na tela.
"""

def exibeTexto(t, q):
    print()
    for x in range(q):
        print(f'Você informou o texto {t} exibindo texto {q} vez(es).')
        print()
        q -= 1
        
texto   = input('Informe o texto que deseja exibir: ')
qtd     = int(input('Informe a quantidade de vezes que deseja exibir o texto: '))

exibeTexto(texto, qtd)
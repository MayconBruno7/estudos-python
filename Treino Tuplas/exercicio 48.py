"""
AUTOR.....: Maycon Bruno
DATA/HORA.: 17/08/2022 as 09:34
FINALIDADE: 48) Crie uma tupla com os valores referente aos meses do ano
				preenchidos por extenso. Seu programa deverá pedir ao usuário
				para informar o mês desejado e imprimir na tela o mês por
				extenso pegando a descrição na tupla criada. Se o usuário
				informar um mês inválido, dar uma mensagem e pedir para
				informar novamente o mês.
"""

mesExtenso = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Novembro', 'Dezembro')

while True:
	
	mes = int(input("Favor informar um mês:"))

	if mes > 0 and mes <= 12:
		print(f"O mês informado foi {mesExtenso[mes - 1]}")
	else:
		print("Mês informado é inválido!")

	rspd = input("Deseja informar um novo mês (S/N?):")

	if rspd.upper() != "S":
		break

	print('=' * 50)
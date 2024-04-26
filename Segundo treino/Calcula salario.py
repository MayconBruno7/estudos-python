"""
    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.   
"""

while True:

    porHora = float(input('Informe os ganhos por hora: '))
    horasDia = float(input('Informe as horas trabalhadas no mês: '))

    print()
    print('Exibindo o sálario do trabalhador')
    print(f'O seu sálario mensal de acordo com os ganhos e horas trabalhadas é: {porHora * horasDia}')

    rspd = input('Deseja saber mais algum sálario? (S/N): ')

    if rspd.upper() != 'S':
        break
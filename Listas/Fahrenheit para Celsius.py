"""
    Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
"""

grauF = float(input('Informe a quantidade de graus Fahrenheit para a conversão para Celsius: '))

print()
print('Exibindo a conversão')
print(f'A conversão de {grauF} F° para Celsius é {5 * ((grauF - 32) / 9):>.2f} C°')
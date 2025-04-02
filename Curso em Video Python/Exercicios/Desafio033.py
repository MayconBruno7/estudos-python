num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))
num3 = int(input("Informe o terceiro numero: "))

maiorNumero = 0
menorNumero = 0

if num1 > maiorNumero:
    maiorNumero = num1
    menorNumero = num1
if num2 > maiorNumero:
    maiorNumero = num2
if num3 > maiorNumero:
    maiorNumero = num3
if num1 < menorNumero:
    menorNumero = num1
if num2 < menorNumero:
    menorNumero = num2
if num3 < menorNumero:
    menorNumero = num3

print('-' * 20)
print("Maior número: {}" . format(maiorNumero))
print("Menor número: {}" . format(menorNumero))
print('-' * 20)
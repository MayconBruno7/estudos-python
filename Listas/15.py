"""
-------------------------------------------------
15) Faça um algoritmo que receba dois números e ao final
				mostre a soma, subtração, multiplicação e a divisão 
				dos números lidos
-------------------------------------------------
"""

print("Favor informar os seguintes dados:")
print()

v1 = float(input("Informe o valor 1:"))
v2 = float(input("Informe o valor 2:"))

soma = v1 + v2
multi = v1 * v2
divi = v1 / v2

if v1 < v2:
	subtracao = v2 - v1
else: 
	subtracao = v1 - v2

print("=" * 50)
print()
print(f"Soma:.............{soma}")
print(f"Subtração:...{subtracao}")
print(f"Multiplicação:...{multi}")
print(f"Divisão:..........{divi}")
print()
print("=" * 50)

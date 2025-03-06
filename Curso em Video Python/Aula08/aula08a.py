import math
import random
import emoji 

num = int(input("Digite um número: "))
raiz = math.sqrt(num)

print("A raiz quadrada do numero é: {0}" .format(math.ceil(raiz)));

# num = random.random()
num = random.randint(1,1000)

print("Numero aleatório: {0}" . format(num))

print(emoji.emojize("Olá, mundo :earth_americas:"))
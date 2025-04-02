import random

numAleatorio =  random.randint(0, 5)

usuarioNumTentativa = int(input("Tente adivinhar o numero entre 0 e 5 gerado pelo sistema: "))

print("Número gerado pelo sistema {}" .format(numAleatorio))

if usuarioNumTentativa == numAleatorio:
    print("Parabéns você acertou o número aleatorio gerado pelo sistema!")
else:
    print("Infelizmente você não acertou o numero aleatório")
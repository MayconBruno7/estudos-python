velocidadeCarro = int(input("Informe a velocidade do carro: "))

if velocidadeCarro > 80:
    print("Você foi multado!")
    valor_multa = (velocidadeCarro - 80) * 7
    print("O valor da multa é de: {}" .format(valor_multa))

else:
    print("Dentro dos limites de velocidade!")


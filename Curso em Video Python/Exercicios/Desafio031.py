distanciaEmKm = float(input("Informe a quantidade de km da viagem: "))

print("-" * 20)

if distanciaEmKm <= 200:
    print("O valor da passagem é: R${:.2f}" .format(distanciaEmKm * 0.5))
    
else: 
    print("O valor da passagem é: R${:.2f}" .format(distanciaEmKm * 0.45))
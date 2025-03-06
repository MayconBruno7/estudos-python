val_carteira = float(input("Informe o valor em carteira: "))

print('=' * 20)
print("Cotação Dolar: 3,27")
print("Você pode comprar {0} Doláres" . format(val_carteira * 3.27).replace(".", ","))
print('=' * 20)
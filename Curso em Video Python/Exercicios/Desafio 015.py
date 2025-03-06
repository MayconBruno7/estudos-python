km          = float(input("Informe a quantidade de quilometros rodados: "))
dias        = int(input("Informe a quantidade de dias em que o carro foi locado: "))
preco_dia   = 60
km_rodado   = 0.15

print("===================================")
print("Quilometros rodados: " + str(km))
print("Preço por km rodado: {0}" . format(km_rodado));
print("Preço a pagar pelos km de locação: {0:.2f}" . format(km * km_rodado));
print("===================================")
print("Quantidade de dias em que o veículo foi locado: {0}". format(dias))
print("Preço por dia da locação do veículo: {0}" . format(preco_dia));
print("Preço a pagar pelos dias de locação: {0}" . format(dias * preco_dia));
print("===================================")
print("Valor total da locação do veiculo: {0:.2f}" . format((km * km_rodado) + (dias * preco_dia)));
print("===================================")
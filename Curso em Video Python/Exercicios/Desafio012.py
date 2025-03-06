val_produto = float(input('Informe o valor do produto: '))
valor_desconto  = (val_produto * 5) / 100

print('O produto que custava R$ {0}, na promoção com desconto de 5% vai custar {1} R$ e o seu valor final é de {2} R$.' . format(val_produto, valor_desconto, str(val_produto - valor_desconto).replace(".", ",")))
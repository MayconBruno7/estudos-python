nome_cidade = input('Informe o nome da cidade para verificação se começa com santo: ')

divide_palavra = nome_cidade.lower().split()

comeca_com_santo = divide_palavra[0].find('santo')

if comeca_com_santo != -1:
    print('A cidade "{}" começa com o nome santo!' . format(nome_cidade))
    
else:
    print('A cidade "{}" não começa com o nome santo!' . format(nome_cidade))
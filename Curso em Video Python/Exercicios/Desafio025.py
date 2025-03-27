nome_pessoa = input('Informe o nome da pessoa: ')

nome_tem_silva = nome_pessoa.lower().find('silva')

if nome_tem_silva != -1:
    print('O nome "{}" tem o nome silva! ' . format(nome_pessoa))
    
print('O nome "{}" não tem o nome silva! ' . format(nome_pessoa))
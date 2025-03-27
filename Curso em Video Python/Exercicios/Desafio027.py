nome_pessoa = input('Informe o nome completo da pessoa: ')

primeiro_nome = nome_pessoa.split()
print('Primeiro nome: {}' .format(primeiro_nome[0]))

ultimo_nome = nome_pessoa.split()
print('Ultimo nome: {}' .format(ultimo_nome[len(ultimo_nome) - 1]))
nome_completo = str(input('Informe o nome completo: '))

print('Nome com todas as letras maiúsculas: ' + nome_completo.upper())
print('Nome com todas as letras minusculas: ' + nome_completo.lower())
print('Quantidade de letras sem espaço: {}' .format(len(nome_completo.strip())))
sem_espaços = nome_completo.split()
print('Quantidade de letras que tem o primeiro nome: {}' . format(len(sem_espaços[0])))   

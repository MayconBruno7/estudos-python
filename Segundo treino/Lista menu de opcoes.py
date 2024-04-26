"""
AUTOR.....: Maycon Bruno
DATA/HORA.: 24/09/2022 as 13:06
FINALIDADE: 10) Solicite ao usuário o nome e a idade 
			de 10 pessoas, armazene em listas. Crie um 
			menu de opções:
			1) Cadastrar pessoa
			2) Exibir em ordem crescente de Nome
			3) Exibir em ordem decrescente de Idade.
			4) Sair
"""

nome = list()
idade = list()

while True:

    print('Menu de opções')
    print()
    print('1) Cadastrar pesssoas')
    print('2) Exibir em ordem crescente de nome')
    print('3) Exibir em ordem decrescente de idade') 
    print("4) Sair")
    print()

    opcao = int(input('Informe a opção desejada: '))

    if opcao == 1:
        
        if len(nome) > 10:
            print('Limite maximo de pessoas atingido!')
        
        else:
            print('Adicionando pessoas')

            nome.append(input('Informe o nome: '))
            idade.append(int(input('Informe a idade da pessoa: ')))

    elif opcao == 2:

        if len(nome) == 0:
            print('Não existem pessoas cadastradas!')

        else:
            for x in range(1, len(idade)):
                for y in range(len(idade) - 1, 0, -1):
                    if nome[y] < nome[y - 1]:
                        auxIdade = idade[y]
                        idade[y] = idade[y - 1]
                        idade[y - 1] = auxIdade 

                        auxNome = nome[y]
                        nome[y] = nome[y - 1]
                        nome[y - 1] = auxNome
                    
            print('Exibindo em ordem crescente de nome:')

            for x in range(len(nome)):
                print(f'{nome[x]} - {idade[x]}')

    elif opcao == 3:

        if len(nome) == 0:
            print('Não existem pessoas cadastradas!')

        else:
            for x in range(1, len(idade)):
                for y in range(len(idade) - 1, 0, -1):
                    if idade[y] > idade[y - 1]:
                        auxIdade = idade[y]
                        idade[y] = idade[y - 1]
                        idade[y - 1] = auxIdade 

                        auxNome = nome[y]
                        nome[y] = nome[y - 1]
                        nome[y - 1] = auxNome
                    
            print('Exibindo em ordem decrescente de nome:')

            for x in range(len(nome)):
                print(f'{nome[x]} - {idade[x]}')

    elif opcao == 4:

        sair = input('Deseja sair do app (S/N)? ')

        if sair.upper() == 'S':
            break 

    else:
        print('Opção digitada inválida!')






"""
AUTOR.....: Maycon Bruno
DATA/HORA.: 24/09/2022 as 13:25
FINALIDADE: Criar um menu de opçôes utilizando metodo bolha.

"""

nome = list()
idade = list()

while True:

    print("+" * 40)
    print("MENU DE OPÇÕES:")
    print("+" * 40)
    print("1 - Adicionar pessoas")
    print("2 - Exibir as pessoas ordem alfabetica")
    print("3 - Exibir ordem decrescente idade")
    print("4 - Exibir por idade ")
    print("5 - Pesquisar pessoa")
    print("6 - Sair")
    print("Digite a opção desejada: ", end="")

    opcao = int(input())

    if opcao == 1:

        print('Adicionando pessoas')
        nome.append(input('Informe a pessoa que deseja adicionar: '))
        idade.append(int(input('Informe a idade da pessoa: ')))

    elif opcao == 2:
        for x in range(1, len(nome)):
            for y in range(len(nome) - 1, 0, -1):
                if nome[y] < nome[y - 1]:
                    auxIdade = idade[y]
                    idade[y] = idade[y - 1]
                    idade[y - 1] = auxIdade

                    auxNome = nome[y]
                    nome[y] = nome[y - 1]
                    nome[y - 1] = auxNome

        print('Exibindo as pessoas em ordem alfabetica')                
        print()

        for x in range(len(nome)):
            print(f'{nome[x]} - {idade[x]}')

    elif opcao == 3:
        for x in range(1, len(idade)):
            for y in range(len(idade) - 1, 0, -1):
                if idade[y] < idade[y - 1]:
                    auxIdade = idade[y]
                    idade[y] = idade[y - 1]
                    idade[y - 1] = auxIdade
            
                    auxNome = nome[y]
                    nome[y] = nome[y - 1]
                    nome[y - 1] = auxNome

        print('Exibindo em ordem decrescente de idade')
        print()

        for x in range(len(idade)):
            print(f'{nome[x]} - {idade[x]}')

    elif opcao == 4:
        for x in range(1, len(idade)):
            for y in range(len(idade) - 1, 0, -1):
                if idade[y] > idade[y - 1]:
                    auxIdade = idade[y]
                    idade[y] = idade[y - 1]
                    idade[y - 1] = auxIdade

                    auxNome = nome[y]
                    nome[y] = nome[y - 1]
                    nome[y - 1] = auxNome
                
        print('Exibindo por ordem crescente de idade')
        print()

        for x in range(len(idade)):
            print(f'{nome[x]} - {idade[x]}')
        
    elif opcao == 5:

        print('Buscando pessoas')
        
        buscaNome = input("Informe o nome que deseja pesquisar: ")
        lAchou = False

        for x in range(len(nome)):
            if buscaNome.upper() == nome[x].upper():
                lAchou = True
                print(f"Nome: {nome[x]}, tem {idade[x]} ano(s)")
        
        if not lAchou:      
            print(f"Não foi possível localizar {buscaNome} na lista de pessoas")


    elif opcao == 6:
        break

    else:
        print('Opção inválida!')
"""
    17) Desenvolver um programa de agenda que armazene informações como: o nome, idade, cep, cidade e telefone de 10 pessoas (utilize o
        dicionários). Apresente um menu ao usuário:
            – Cadastrar contato
            - Listar contatos:
                - Em ordem alfabética
                - Em ordem de telefone
            - Pesquisa de contatos:
                - Por nome
                - Por telefone
            – Sair

"""

contatos = dict()
agenda   = list() 

qtdPessoas = 0

while True:

    print('Menu de opções')
    print()
    print('1) Cadastrar contatos')
    print('2) Listar contatos')
    print('3) Pesquisa de contatos')
    print('4) Sair')
    print()

    opc = int(input('Informe a opção desejada: '))

    if opc == 1:

        if qtdPessoas == 10:
            break
            
        else:
            print()
            print('Cadastrando pessoas')
            print()

            contatos['nome']        = input('Nome...: ')
            contatos['idade']       = int(input('Idade...: '))
            contatos['cep']         = int(input('Cep...:'))
            contatos['cidade']      = input('Cidade...:')
            contatos['telefone']    = int(input('Telefone..:'))

            agenda.append(contatos.copy())
            qtdPessoas += 1
        
    elif opc == 2:

        if qtdPessoas == 0: 
            print('Não existem contatos cadastrados')

        else:
            print()
            print('Listando contatos')
            print()
            print('1) Ordem alfabética')
            print('2) ordem de telefone')
            print()

            opc2 = int(input('Como deseja listar: '))

            if opc2 == 1:

                print()
                print('Listando contatos por ordem alfabética')
                print()

                for a in range(1, len(agenda)):
                    for c in range(len(agenda) - 1, 0, - 1):
                        if agenda[c]['nome'].upper() < agenda[c - 1]['nome'].upper:
                            auxContatos         = agenda[c]
                            agenda[c] = agenda[c - 1]
                            agenda[c - 1]  = auxContatos

                for contatos in range(len(agenda)):
                    print(f'{agenda[contatos]["nome"]}', end='  ')
                    print(f'{agenda[contatos]["idade"]}', end='   ')
                    print(f'{agenda[contatos]["cep"]}', end='   ')
                    print(f'{agenda[contatos]["cidade"]}', end='    ')
                    print(f'{agenda[contatos]["telefone"]}')

            if opc2 == 2:

                print()
                print('Listando por ordem de telefone')
                print()

                for a in range(1, len(agenda)):
                    for c in range(len(agenda) - 1, 0, -1):
                        if agenda[c]["telefone"] < agenda[c - 1]["telefone"]:
                            auxTelefone     = agenda[c]
                            agenda[c]       = agenda[c - 1]
                            agenda[c - 1]   = auxTelefone
                
                for contatos in range(len(agenda)):
                    print(f'{agenda[contatos]["nome"]}', end='  ')
                    print(f'{agenda[contatos]["idade"]}', end='   ')
                    print(f'{agenda[contatos]["cep"]}', end='   ')
                    print(f'{agenda[contatos]["cidade"]}', end='    ')
                    print(f'{agenda[contatos]["telefone"]}')

    elif opc == 3: 
        
        if qtdPessoas == 0: 
            print('Não existem contatos cadastrados')

        else:

            while True:
            
                print()
                print('Como deseja pesquisar?')
                print()
                print('1) Por nome')
                print('2) Por telefone')
                print()
            
                opc3 = int(input('Informe a opção desejada: '))

                lAchou = False

                if opc3 == 1: 

                    print()
                    buscaNome = input('Informe o nome que deseja buscar: ')
                    print()

                    for n in range(len(agenda)):
                        if buscaNome.upper() == agenda[n]["nome"].upper():
                            lAchou = True

                            print(f'{agenda[n]["nome"]}', end='  ')
                            print(f'{agenda[n]["idade"]}', end='   ')
                            print(f'{agenda[n]["cep"]}', end='   ')
                            print(f'{agenda[n]["cidade"]}', end='    ')
                            print(f'{agenda[n]["telefone"]}')

                    if not lAchou:
                        print(f'Não foi possivel localizar {buscaNome}')

                lAchou = False 

                if opc3 == 2:

                    print()
                    buscaTelefone = int(input('Informe o numero de telefone que deseja buscar: '))
                    print()

                    for t in range(len(agenda)):
                        if buscaTelefone == agenda[t]["telefone"]:
                            lAchou = True

                            print(f'{agenda[t]["nome"]}', end='  ')
                            print(f'{agenda[t]["idade"]}', end='   ')
                            print(f'{agenda[t]["cep"]}', end='   ')
                            print(f'{agenda[t]["cidade"]}', end='    ')
                            print(f'{agenda[t]["telefone"]}')

                    if not lAchou:
                        print(f'Não foi possivel localizar {buscaNome}')
            
   
            
            

            

    print()
    print('Menu de opções')
    print()
    print('1) Cadastrar')
    print('2) Listagem de funcionários (Por nome, por idade aposentadoria decrescente e função')
    print('3) Busca de funcionários (Por nome, por função.')
    print('4) O nome e função do funcionário que possui o menor salário..')
    print('5) Funcionário mais velho')
    print('6) A média de salário de todos os funcionários.')
    print('7) Sair')
    print()
 

    



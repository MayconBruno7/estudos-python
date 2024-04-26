"""
AUTOR.....: Maycon Bruno
DATA/HORA.: 06/11/2022 as 11:06
FINALIDADE: Crie um dicionário d e coloque nele seus dados: nome, idade, telefone,endereço.
                • Usando o dicionário d criado anteriormente, imprima seu nome.
                
"""

d       = dict()
pessoas = list()

while True:
    
    print()
    print('Menu de opções')
    print()
    print('1) Cadastrar informações')
    print('2) Exibir informações cadastradas')
    print('3) Exibir informações cadastradas em ordem crescente')
    print('4) Exibir informações cadastradas em ordem decrescente')
    print('5) Buscar pessoas')
    print('6) Sair')
    
    opc = int(input('Informe a opção desejada: '))
    
    if opc == 1:
        
        d["nome"]       = input('Informe o nome que deseja cadastrar: ')
        d["idade"]      = int(input('Informe a idade: '))
        d["telefone"]   = int(input('Informe o telefone: '))
        d["endereco"]   = input('Informe o endereço: ')
        
        pessoas.append(d.copy())
        
    elif opc == 2:
        
        while True:
            
            print()
            print('SubMenu')
            print()
            print('1) Somente o nome')
            print('2) Somente a idade')
            print('3) Somente o telefone')
            print('4) Somente o endereço')
            print('5) Todas as informações das pessoas cadastradas')
            print('6) Sair')
            
            opc2 = int(input('Como deseja exibir as informações: '))

            if opc2 == 1:
                
                print() 
                print('Exibindo somente os nomes cadastrados')
                print()

                for informações in pessoas:
                    print(f'{informações["nome"]}')
                    
            elif opc2 == 2: 
                
                print()
                print('Exibindo somente as idades cadastradas')
                print()
                
                for informações in pessoas:
                    print(f'{informações["idade"]}')
                    
            elif opc2 == 3:
                
                print()
                print('Exibindo somente os telefones cadastrados')
                print()
                for informações in pessoas:
                    print(f'{informações["telefone"]}')
                    
            elif opc2 == 4:
                
                print()
                print('Exibindo somente os endereços cadastrados')
                print()
                
                for informações in pessoas:
                    print(f'{informações["endereco"]}')
                    
            elif opc2 == 5:
                
                print()
                print('Exibindo todas as informações cadastradas')
                print()
                print('Nome                     Idade   Telefone        Endereço')
                
                for informações in pessoas:
                    print(f'{informações["nome"]:<21}', end=' ')
                    print(f'{informações["idade"]:>5.0f}', end='    ')
                    print(f'{informações["telefone"]:>6.0f}', end='    ')
                    print(f'{informações["endereco"]:25}')
                    
            elif opc2 == 6:
                print('Você saiu da opção 2!')
                break
            
            else:
                print('Por favor digite uma opção válida!')
    
    elif opc == 3:
        
        # ordemcrescente
        
    elif opc == 4 
    
        # ordem decrescente
        
    elif opc == 5:
        
        while True:
            print()
            print('SubMenu')
            print()
            print('1) Por nome')                
            print('2) Por idade')
            print('3) Por telefone')
            print('4) Por endereço')
            print('5) Sair')
            
            opc3 = int(input('Informe a opção desejada: '))
            
            if opc3 == 1:
                
                print()
                print('Buscando por nome')
                print()
                
                achou = False
                
                buscaNome = input('Informe o nome que deseja buscar: ')
            
                for informações in pessoas:
                    if buscaNome.upper() == informações["nome"].upper():
                        achou = True
                        print('Nome                     Idade   Telefone        Endereço')
                        print(f'{informações["nome"]:<21}', end=' ')
                        print(f'{informações["idade"]:>5.0f}', end='    ')
                        print(f'{informações["telefone"]:>6.0f}', end='    ')
                        print(f'{informações["endereco"]:25}')
                        
                if not achou:
                    print(f'Não foi possivel encontrar o nome {buscaNome}')
            
            elif opc3 == 2:
                
                print()
                print('Buscando por idade')
                print()

                buscaIdade = int(input('Informe a idade que deseja buscar: '))

                achou = False

                for informações in pessoas:
                    if buscaIdade == informações["idade"]:
                        achou = True
                        print('Nome                     Idade   Telefone        Endereço')
                        print(f'{informações["nome"]:<21}', end=' ')
                        print(f'{informações["idade"]:>5.0f}', end='    ')
                        print(f'{informações["telefone"]:>6.0f}', end='    ')
                        print(f'{informações["endereco"]:25}')
                        
                if not achou:
                    print(f'Não foi possivel encontrar o nome {buscaIdade}')
                    
            elif opc3 == 3:
                
                print()
                print('Buscando por telefone')
                print()
                
                achou = False
                
                buscaTelefone = int(input('Informe o telefone que deseja buscar: '))
            
                for informações in pessoas:
                    if buscaTelefone == informações["telefone"]:
                        achou = True
                        print('Nome                     Idade   Telefone        Endereço')
                        print(f'{informações["nome"]:<21}', end=' ')
                        print(f'{informações["idade"]:>5.0f}', end='    ')
                        print(f'{informações["telefone"]:>6.0f}', end='    ')
                        print(f'{informações["endereco"]:25}')
                        
                if not achou:
                    print(f'Não foi possivel encontrar o nome {buscaTelefone}')
                    
            elif opc3 == 4:
                
                print()
                print('Buscando por endereço')
                print()
                
                achou = False
                
                buscaEndereco = input('Informe o endereço que deseja buscar: ')
            
                for informações in pessoas:
                    if buscaEndereco.upper() == informações["endereco"].upper():
                        achou = True
                        print('Nome                     Idade   Telefone        Endereço')
                        print(f'{informações["nome"]:<21}', end=' ')
                        print(f'{informações["idade"]:>5.0f}', end='    ')
                        print(f'{informações["telefone"]:>6.0f}', end='    ')
                        print(f'{informações["endereco"]:25}')
                        
                if not achou:
                    print(f'Não foi possivel encontrar o nome {buscaEndereco}')
                    
            elif opc3 == 5:
                
                print('Você finalizou a opção 3!')
                break
                    
            else:
                print('Por favor informe uma opção válida!')
                
    elif opc == 6:
        
        print('Você finalizou o programa!')
        break
    
    else:
        print('Por favor digite uma opção válida!')
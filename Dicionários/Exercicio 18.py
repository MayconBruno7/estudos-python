"""
18) Uma empresa deseja cadastrar seus funcionários em um sistema no
    qual será inserido (nome, ano de nascimento, sexo, salário, função, ano
    primeiro emprego), calcule e armazene a idade de aposentadoria do
    funcionário com mais de 40 anos de idade (vamos utilizar como base 35
    anos de trabalho para homens e 30 para mulheres), armazene estes dados
    em um dicionário. Crie um menu de opções conforme abaixo:
        1) Cadastrar
        2) Listagem de funcionários (Por nome, por idade aposentadoria decrescente e
        função)
        3) Busca de funcionários (Por nome, por função).
        4) O nome e função do funcionário que possui o menor salário.
        5) Funcionário mais velho
        6) A média de salário de todos os funcionários.
        7) Sair

"""

funcionarios    = list()
info            = dict()

qtdFuncionarios = 0

indMenorSalario = -1

funcionarioMaisVelho = - 1

while True:
    
    print()
    print('Menu de opções')
    print()
    print('1) Cadastrar')
    print('2) Listagem de funcionários (Por nome, por idade aposentadoria decrescente e função)') # idade de aposentadoria não esta funcionando
    print('3) Busca de funcionários (Por nome, por função)') 
    print('4) O nome e função do funcionário que possui o menor salário..')
    print('5) Funcionário mais velho')
    print('6) A média de salário de todos os funcionários.') # media não funciona
    print('7) Sair')
    print()
    
    opc = int(input('Informe a opção desejada: '))
    
    if opc == 1:
        
            info["nome"]            = input('Informe o nome do funcionário: ') 
            info["nascimento"]      = int(input('Informe o ano de nascimento do funcionário: '))
            info["sexo"]            = input('Informe o sexo do funcionário F = Feminino e M = Masculino: ')
            info["salario"]         = float(input('Informe o salário do funcionário: '))
            info["funcao"]          = input('Informe a função do funcionário: ') 
            info["pEmprego"]        = input('Informe o ano do primeiro emprego do funcionário: ')

            info["idade"] = 2022 - info["nascimento"]
            funcionarios.append(info.copy())
            qtdFuncionarios += 1
            
    elif opc == 2:
        
        print()
        print('Listagem de funcionários')
        print()
        print('Como deseja listar?')
        print()
        print('1) Por nome')
        print('2) Por idade de aposentadoria decrescente')
        print('3) Por função')
        print()
        
        opc2 = int(input('Informe a opção desejada: '))
        
        if opc2 == 1:
            
            print()
            print('Listando funcionarios por nome')
            print()
            
            for informacoes in range(1, len(funcionarios)):
                for f in range(len(funcionarios) -  1, 0, -1):
                    if funcionarios[f]["nome"].upper() < funcionarios[f - 1]["nome"].upper():
                        auxNome             = funcionarios[f]
                        funcionarios[f]     = funcionarios[f - 1]
                        funcionarios[f - 1] = auxNome
                        
            for f in range(len(funcionarios)):
                print(f'{funcionarios[f]["nome"]}', end='   ')
                print(f'{funcionarios[f]["nascimento"]}', end=' ')
                print(f'{funcionarios[f]["sexo"]}', end='   ')
                print(f'{funcionarios[f]["salario"]}', end='    ')
                print(f'{funcionarios[f]["funcao"]}', end='   ')
                print(f'{funcionarios[f]["pEmprego"]}')

        if opc2 == 2:
            
            print()
            print('Listando funcionários por ordem decrescente de aposentadoria')
            print()
            
            for informacoes in range(1, len(funcionarios)):
                for f in range(len(funcionarios) -  1, 0, -1):
                    if funcionarios[f]["aposentadoriaM"] and funcionarios[f]["aposentadoriaF"] > funcionarios[f - 1]["nome"]:
                        auxNome = funcionarios[f]
                        funcionarios[f] = funcionarios[f - 1]
                        funcionarios[f - 1] = auxNome
                        
            for f in range(len(funcionarios)):
                print(f'{funcionarios[f]["nome"]}', end='   ')
                print(f'{funcionarios[f]["nascimento"]}', end=' ')
                print(f'{funcionarios[f]["sexo"]}', end='   ')
                print(f'{funcionarios[f]["salario"]}', end='    ')
                print(f'{funcionarios[f]["funcao"]}', end=' ')
                print(f'{funcionarios[f]["pEmprego"]}')     
                
        if opc2 == 3:
            
            print()
            print('Listando por função')
            print()
            
            for informacoes in range(1, len(funcionarios)):
                for f in range(len(funcionarios) -  1, 0, -1):
                    if funcionarios[f]["funcao"].upper() < funcionarios[f - 1]["funcao"].upper():
                        auxFuncao           = funcionarios[f]
                        funcionarios[f]     = funcionarios[f - 1]
                        funcionarios[f - 1] = auxFuncao
                        
            for f in range(len(funcionarios)):
                print(f'{funcionarios[f]["nome"]}', end='   ')
                print(f'{funcionarios[f]["nascimento"]}', end=' ')
                print(f'{funcionarios[f]["sexo"]}', end='   ')
                print(f'{funcionarios[f]["salario"]}', end='    ')
                print(f'{funcionarios[f]["funcao"]}', end= '    ')
                print(f'{funcionarios[f]["pEmprego"]}')
                    
        
    elif opc == 3:      
        
        print()
        print('Opções de busca de funcionários')  
        print()
        print('1) Por nome')
        print('2) Por função')
        print()
        
        opc3 = int(input('Informe como deseja buscar: '))
        
        achouNome = False

        if opc3 == 1:
            
            print()
            print('Buscando por nome')
            print()
            
            buscaNome = input('Informe o nome que deseja buscar: ')
            
            for f in range(len(funcionarios)):
                if buscaNome.upper() == funcionarios[f]["nome"].upper():
                    achouNome = True

                    print(f'{funcionarios[f]["nome"]}', end='   ')
                    print(f'{funcionarios[f]["nascimento"]}', end='   ')
                    print(f'{funcionarios[f]["sexo"]}', end='   ')
                    print(f'{funcionarios[f]["salario"]}', end='   ')
                    print(f'{funcionarios[f]["funcao"]}', end='   ')
                    print(f'{funcionarios[f]["pEmprego"]}')

            if not achouNome:
                print(f'Não foi possivel localizar o funcionario {buscaNome}')
                    
        achouFuncao = False
        
        if opc3 == 2:
            
            print()
            print('Buscando por função')
            print()

            buscaFuncao = input('Informe a função que deseja buscar: ')
            
            for f in range(len(funcionarios)):
                if buscaFuncao.upper() == funcionarios[f]["funcao"].upper():
                    achouFuncao = True

                    print(f'{funcionarios[f]["nome"]}', end='   ')
                    print(f'{funcionarios[f]["nascimento"]}', end='   ')
                    print(f'{funcionarios[f]["sexo"]}', end='   ')
                    print(f'{funcionarios[f]["salario"]}', end='   ')
                    print(f'{funcionarios[f]["funcao"]}', end='   ')
                    print(f'{funcionarios[f]["pEmprego"]}') 

            if not achouFuncao:
                print(f'Não foi possivel localizar os funcionarios da função {buscaFuncao}')
            
    

    elif opc == 4:

        if len(funcionarios) == 1:
            indMenorSalario = 0

        else:
            if funcionarios[len(funcionarios) - 1]["salario"] < funcionarios[indMenorSalario]["salario"]:
                indMenorSalario = len(funcionarios) - 1
                    

        print(f'O funcionário que tem o menor salário é {funcionarios[indMenorSalario]["nome"]} e está na função {funcionarios[indMenorSalario]["funcao"]}')

    elif opc == 5:

        if len(funcionarios) == 1:
            funcionarioMaisVelho = 0

        else:
            if funcionarios[len(funcionarios) - 1]["nascimento"] - 2022 > funcionarios[len(funcionarios) - 1]["nascimento"] - 2022:
                funcionarioMaisVelho = len(funcionarios) - 1
        
        print(f'O funcionario mais velho é {funcionarios[funcionarioMaisVelho]["nome"]} e está na função {funcionarios[funcionarioMaisVelho]["funcao"]} ')

    elif opc == 6:

        print()
        print('Exibindo a media de idade dos funcionarios')
        print()

       
        print(f'{(info["media"]) / len(funcionarios)}')

    elif opc == 7:
        print('Você finalizou o programa')
        break

    else:
        print('Opção inválida!')






                    
                
                
            
            
    
    
    
    
         
    
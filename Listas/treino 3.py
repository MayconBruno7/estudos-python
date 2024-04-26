"""
    Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas 
    brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um 
    programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
        $200 - $299
        $300 - $399
        $400 - $499
        $500 - $599
        $600 - $699
        $700 - $799
        $800 - $899
        $900 - $999
        $1000 em diante
"""

salario     = list()
auxSalario  = list()

while True:
    
    print()
    print('Menu de opções')
    print()
    print('1) Cadastrar vendedor.')
    print('2) Mostrar vendedores com seu salario liquido.')
    print('3) Exibir pessoas que recebem salários entre determinasdos valores.')
    print('4) Encerrar programa.')
    print()
    
    opc = int(input('Informe a opção desejada: '))
    
    if opc == 1:
        
        print()
        print('Cadastrando vendedores')
        print()
        
        nome            =    input('Informe o nome do vendedor: ')
        vendasBrutas    = float(input('Informe o valor da venda bruta: '))
        salarioLiquido  = (vendasBrutas * 9  + 200) / 100 + 200
        
        salario.append([nome, vendasBrutas, salarioLiquido])
        
    elif opc == 2:
        
        print()
        print('Exibindo vendedores cadastrados')
        print()
       
        print('Nome             Vendas          Salário Liquido')
        print()
        
        for v in range(len(salario)):
            print(f'{salario[v][0]:<13}', end='    ')
            print(f'{salario[v][1]:<12}', end='    ')
            print(f'{salario[v][2]}')
            
    elif opc == 3:
        
        print()
        print('Como deseja exibir? ')
        print()
        print('1) R$ 200 - R$ 299')
        print('2) R$ 300 - R$ 399')
        print('3) R$ 400 - R$ 499')
        print('4) R$ 500 - R$ 599')
        print('5) R$ 600 - R$ 699')
        print('6) R$ 700 - R$ 799')
        print('7) R$ 800 - R$ 899')
        print('8) R$ 900 - R$ 999')
        print('9) R$ 1000 em diante')
        print()
        
        opc3 = int(input('Informe a opção desejada: '))
        
        if opc3 == 1:
            
            print()
            print('Exibindo salários entre R$ 200 - R$ 299')
            print()
            
            for s in range(len(salario)):
                if salario[s][2] >= 200 and salario[s][2] <= 299:
                    print('Nome             Vendas          Salário Liquido')
                    print()
                    
                    for v in range(len(salario)):
                        print(f'{salario[v][0]:<13}', end='    ')
                        print(f'{salario[v][1]:<12}', end='    ')
                        print(f'{salario[v][2]}')
                        
        elif opc3 == 2:
            
            print()
            print('Exibindo salários entre R$ 300 - R$ 399')
            print()
            
            for s in range(len(salario)):
                if salario[s][2] >= 300 and salario[s][2] <= 399:
                    print('Nome             Vendas          Salário Liquido')
                    print()
                    
                    for v in range(len(salario)):
                        print(f'{salario[v][0]:<13}', end='    ')
                        print(f'{salario[v][1]:<12}', end='    ')
                        print(f'{salario[v][2]}')
                                
        elif opc3 == 3:
            
            print()
            print('Exibindo salários entre R$ 400 - R$ 499')
            print()
            
            for s in range(len(salario)):
                if salario[s][2] >= 400 and salario[s][2] <= 499:
                    print('Nome             Vendas          Salário Liquido')
                    print()
                    
                    for v in range(len(salario)):
                        print(f'{salario[v][0]:<13}', end='    ')
                        print(f'{salario[v][1]:<12}', end='    ')
                        print(f'{salario[v][2]}')
        
        elif opc3 == 4:
            
            print()
            print('Exibindo salários entre R$ 500 - R$ 599')
            print()
            
            for s in range(len(salario)):
                if salario[s][2] >= 500 and salario[s][2] <= 599:
                    print('Nome             Vendas          Salário Liquido')
                    print()
                    
                    for v in range(len(salario)):
                        print(f'{salario[v][0]:<13}', end='    ')
                        print(f'{salario[v][1]:<12}', end='    ')
                        print(f'{salario[v][2]}')

        elif opc3 == 5:
            
            print()
            print('Exibindo salários entre R$ 600 - R$ 699')
            print()
            
            for s in range(len(salario)):
                if salario[s][2] >= 600 and salario[s][2] <= 699:
                    print('Nome             Vendas          Salário Liquido')
                    print()
                    
                    for v in range(len(salario)):
                        print(f'{salario[v][0]:<13}', end='    ')
                        print(f'{salario[v][1]:<12}', end='    ')
                        print(f'{salario[v][2]}')

        elif opc3 == 6:
            
            print()
            print('Exibindo salários entre R$ 700 - R$ 799')
            print()
            
            for s in range(len(salario)):
                if salario[s][2] >= 700 and salario[s][2] <= 799:
                    print('Nome             Vendas          Salário Liquido')
                    print()
                    
                    for v in range(len(salario)):
                        print(f'{salario[v][0]:<13}', end='    ')
                        print(f'{salario[v][1]:<12}', end='    ')
                        print(f'{salario[v][2]}')

        elif opc3 == 7:
            
            print()
            print('Exibindo salários entre R$ 800 - R$ 899')
            print()
            
            for s in range(len(salario)):
                if salario[s][2] >= 800 and salario[s][2] <= 899:
                    print('Nome             Vendas          Salário Liquido')
                    print()
                    
                    for v in range(len(salario)):
                        print(f'{salario[v][0]:<13}', end='    ')
                        print(f'{salario[v][1]:<12}', end='    ')
                        print(f'{salario[v][2]}')

        elif opc3 == 8:
            
            print()
            print('Exibindo salários entre R$ 900 - R$ 999')
            print()
            
            for s in range(len(salario)):
                if salario[s][2] >= 900 and salario[s][2] <= 999:
                    print('Nome             Vendas          Salário Liquido')
                    print()
                    
                    for v in range(len(salario)):
                        print(f'{salario[v][0]:<13}', end='    ')
                        print(f'{salario[v][1]:<12}', end='    ')
                        print(f'{salario[v][2]}')

        elif opc3 == 9:
            
            print()
            print('Exibindo salários apartir de R$ 1000')
            print()
            
            for s in range(len(salario)):
                if salario[s][2] > 1000:
                    print('Nome             Vendas          Salário Liquido')
                    print()
                    
                    for v in range(len(salario)):
                        print(f'{salario[v][0]:<13}', end='    ')
                        print(f'{salario[v][1]:<12}', end='    ')
                        print(f'{salario[v][2]}')

        else:
            print('Informe uma opção válida!')
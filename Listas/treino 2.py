"""
    Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser 
    armazenado). Após esta entrada de dados, faça:
        Mostre a quantidade de valores que foram lidos;
        Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
        Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
        Calcule e mostre a soma dos valores;
        Calcule e mostre a média dos valores;
        Calcule e mostre a quantidade de valores acima da média calculada;
        Calcule e mostre a quantidade de valores abaixo de sete;
        Encerre o programa com uma mensagem;

"""

valores     = list()

qtdValores  = 0
soma        = 0

while True:
    
    print()
    print('Menu de opções')
    print()
    print('1) Cadastrar notas')
    print('2) Mostre a quantidade de valores que foram lidos')
    print('3) Exiba todos os valores na ordem em que foram informados, um ao lado do outro')
    print('4) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro')
    print('5) Calcule e mostre a soma dos valores')
    print('6) Calcule e mostre a média dos valores')
    print('7) Calcule e mostre a quantidade de valores acima da média calculada')
    print('8) Calcule e mostre a quantidade de valores abaixo de sete')
    print('9) Encerre o programa')
    print()
    
    opc = int(input('Informe a opção desejada: '))
    
    if opc == 1:
        
        qtdValores += 1
         
        print()
        print('Cadastrando notas')
        print()
        print(f'Informade a {qtdValores}° nota.')
        print()
        notas  = float(input('Informe a nota: '))
        soma += notas
        
        valores.append(notas)
        print()
        
    elif opc == 2:
        
        if qtdValores == 0:
            print('Não foi informada nenhuma nota')
            
        else: 
            print()
            print('Mostrando a quantidade de valores lidos')
            print()
            print(f'A quantidade de valores lidos é {qtdValores}')
            print
            
    elif opc == 3:
        
        if qtdValores == 0:
            print('Não foi informada nenhuma nota')
            
        else: 
            print()
            print('Exibindo os valores um ao lado do outro na ordem em que foram informados')
            print()
        
            for n in range(len(valores)):
                print(f'{valores[n]}', end='    ')
            print()
        
    elif opc  == 4:
        
        if qtdValores == 0:
            print('Não foi informada nenhuma nota')
            
        else: 
            print()
            print('Exibindo valores na ordem inversa em que foram digitados um abaixo do outro')
            print()
            
            for n in range(1, len(valores)):
                for v in range(len(valores) - 1, 0, -1):
                    if valores[v] > valores[v - 1]:
                        auxValores      = valores[v]
                        valores[v]      = valores[v - 1]
                        valores[v - 1]  = auxValores
                        
            for n in range(len(valores)):
                print(f'{valores[n]}')
            print()

    elif opc == 5:
        
        if qtdValores == 0:
            print('Não foi informada nenhuma nota')
            
        else: 
            print()
            print('Mostrando a soma dos valores')
            print()
            print(f'A soma dos valores é {soma}.')
            print()
        
    elif opc == 6:
        
        if qtdValores == 0:
            print('Não foi informada nenhuma nota')
            
        else: 
            print()
            print('Mostrando a media dos valores')
            print()
            print(f'Foram digitados {qtdValores} e a media dos valores é {(soma) / 4}')
            print()
            
    elif opc == 7:
        
        if qtdValores == 0:
            print('Não foi informada nenhuma nota')
            
        else: 
            print()
            print('Mostrando valores acima da média')
            print()
            
            for nota in range(len(valores)):
                if valores[nota] >= 7:
                    media = valores[nota]
                    print(f'{media}')
                
                if media < 0:    
                    print('Não foi informado nenhum valor acima da média!')
            print()
            
    elif opc == 8:
        
        if qtdValores == 0:
            print('Não foi informada nenhuma nota')
            
        else: 
            print()
            print('Exibindo valores abaixo de sete')
            print()
            
            for nota in range(len(valores)):
                if valores[nota] < 7:
                    media = valores[nota]
                    print(f'{media}')
                
                if media == 0:
                    print('Não foi informado nenhum valor abaixo da média')
            print()
                
    elif opc == 9:
        
        print('Você finalizou o programa!')
        break

    else:
        print('Favor informar uma opção válida!')
        print()
                
           
        
        
        
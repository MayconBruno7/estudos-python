"""
    Autor: Maycon Bruno
    Data : 19/01/2023
    
    32) Desenvolva um algoritmo que solicite ao usuário que 
                informe o nome, sexo e idade de 10 alunos. No final 
                apresente:

                - O nome do aluno mais novo.
                - O nome do aluno mais velho do sexo Masculino.
                - A média de idade das alunas.

"""

alunos      = list()
info        = dict()

alunoNovoM  = -1
alunoNovoF  = -1

alunoVelhoM = -1
alunoVelhoF = -1

qtdAlunos   = 0
media       = 0

while True:
    
    print()
    print('Menu de opções')
    print()
    print('1) Adicionar aluno')    
    print('2) Aluno(a) mais velho cadastrado')
    print('3) Aluno(a) mais novo cadastrado')
    print('4) Media de idade dos alunos cadastrados')   
    print('5) Listar todos os alunos cadastrados')
    print('6) Sair') 
    print()
    
    opc = int(input('Informe a opção desejada: '))
    
    if opc == 1:
        
        if qtdAlunos == 10:
            print('Quantidade máxima de alunos adicionados')
            
        else:
            
            print()
            print('Adicionando alunos')
            print()
            
            info["nome"]    = input('Informe o nome do aluno: ')
            
            while True:
                
                print()
                print('=' * 50)
                print('M - Masculino, F - Feminino')
                print('=' * 50)
                print()
                
                info["sexo"]    = input('Informe o sexo do aluno: ')
                
                if info["sexo"].upper() == 'M' or info["sexo"].upper() == 'F':
                    break
                
                else:
                    print()
                    print('Por favor informe um sexo válido!')
                
            info["idade"]   = int(input('Informe a idade do aluno: '))
            media           += info["idade"]
            
            alunos.append(info.copy())
            print(alunos)
            qtdAlunos += 1
            
    elif opc == 2:
        
        print()
        print('SubMenu aluno mais velho')
        print()
        print('1) Sexo Masculino')
        print('2) Sexo Feminino')
        print()
        
        opc2 = int(input('Sexo: '))
        
        if opc2 == 1:
            
            for informacoes in range(len(alunos)):
                if alunos[informacoes]["sexo"].upper() == 'M':
                    if informacoes == 0:
                        alunoVelhoM  = informacoes
                        
                    else:
                        if alunos[informacoes]["idade"] > alunos[alunoVelhoM]["idade"]:
                            alunoVelhoM  = informacoes

            print(f'O aluno mais velho do sexo masculino cadastrado é {alunos[alunoVelhoM]["nome"]} e tem {alunos[alunoVelhoM]["idade"]} anos de idade')
            
        if opc2 == 2:
            
            for informacoes in range(len(alunos)):
                if alunos[informacoes]["sexo"].upper() == 'F':
                    if informacoes == 0:
                        alunoVelhoF  = informacoes
                        
                    else:
                        if alunos[informacoes]["idade"] > alunos[alunoVelhoF]["idade"]:
                            alunoVelhoF  = informacoes
            
            print(f'O aluno mais velho do sexo feminino cadastrado é {alunos[alunoVelhoF]["nome"]} e tem {alunos[alunoVelhoF]["idade"]} anos de idade')
                    
    elif opc == 3:
        
        print()
        print('SubMenu aluno mais novo')
        print()
        print('1) Sexo Masculino')
        print('2) Sexo Feminino')
        print()
        
        opc3 = int(input('Sexo: '))
        
        if opc3 == 1:
            
            for informacoes in range(len(alunos)):
                if alunos[informacoes]["sexo"].upper() == 'M':
                    if informacoes == 0:
                        alunoNovoM  = informacoes
                        
                    else:
                        if alunos[informacoes]["idade"] < alunos[alunoNovoM]["idade"]:
                            alunoNovoM  = informacoes

            print(f'O aluno mais velho do sexo masculino cadastrado é {alunos[alunoNovoM]["nome"]} e tem {alunos[alunoNovoM]["idade"]} anos de idade')
            
        if opc3 == 2:
            
            for informacoes in range(len(alunos)):
                if alunos[informacoes]["sexo"].upper() == 'F':
                    if informacoes == 0:
                        alunoNovoF  = informacoes
                        
                    else:
                        if alunos[informacoes]["idade"] < alunos[alunoNovoF]["idade"]:
                            alunoNovoF  = informacoes
            
            print(f'O aluno mais velho do sexo feminino cadastrado é {alunos[alunoNovoF]["nome"]} e tem {alunos[alunoNovoF]["idade"]} anos de idade')
            
    elif opc == 4: 
        
        print()
        print('=' * 50)
        print(f'A média de todos os alunos cadastrados é: {media / len(alunos)}')             
        print('=' * 50)
        print() 
        
    elif opc == 5:           

        print()
        print('SubMenu - Todos alunos cadastrados')
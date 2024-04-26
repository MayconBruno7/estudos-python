"""
    1. Escreva um programa completo em Python, que realiza o cadastro dos projetos desenvolvidos pelos alunos da FASM. Em termos gerais cada 
    projeto deverá ser cadastrado com os seguintes atributos:
        • Nome do Aluno (String)
        • Nome do Projeto (String)
        • Curso do Aluno (String)
        • Professor Orientador (String)
        • Ano de Desenvolvimento (Integer)

        Implemente o seguinte menu principal:
            1 - Cadastrar Projeto
            2 – Busca de projetos
            3 – Listagem de Projetos
            4 – Sair
"""

#
def menu():

    global projetos

    while True:

        print('=' * 50)
        print('1 - Cadastrar Projeto')
        print('2 – Busca de projetos')
        print('3 – Listagem de Projetos')
        print('4 – Sair')
        print('=' * 50)

        opc = int(input('Informe opção desejada: '))

        if opc == 1: 

            cadastro()

        elif opc == 2: 

            buscaProjetos(projetos)

        elif opc == 3: 

            Ordem_A(projetos)

        elif opc == 4:

            print('Você finalizou o programa!')
            break

        else:
            mensagem()

# 
def cadastro():

    while True:
        
        alunos = dict()

        alunos["nome"]              = input('Informe o nome do aluno: ')
        alunos["projeto"]           = input('Informe o nome do projeto: ')
        alunos["curso"]             = input('Informe o curso do aluno: ')
        alunos["Prof"]              = input('Informe o nome do professor orientador: ')
        alunos["anoDes"]            = int(input('Informe o ano de desenvolvimento: '))

        projetos.append(alunos.copy())
        
        sair = input('Deseja cadastrar mais pessoas? (S/N): ')
        
        if sair.upper() == 'N':
            print('Você saiu do menu de cadastramento!')
            break
        
        print()
        print('=' * 50)

#
def buscaProjetos(projetos):

    while True:
        
        print()
        print('Como deseja buscar? ')
        print()
        print('1) Por nome do aluno')
        print('2) Por nome do pojeto')
        print('3) Por curso')
        print('4) Por professor')
        print('5) Por ano')
        print('6) Sair')
        print()

        opc2 = int(input('Informe como deseja buscar: '))

        if opc2 == 1:

            buscaProjetosNomeAluno(projetos)
        
        elif opc2 == 2:

            buscaNomeProjeto(projetos)

        elif opc2 == 3: 

            buscaCurso(projetos)

        elif opc2 == 4: 

            buscaProfessor(projetos)

        elif opc2 == 5: 

            buscaAno(projetos)
        
        elif opc2 == 6:
            break
        
        else:
            
            mensagem()
        
#
def buscaProjetosNomeAluno(projetos):
    
    while True:
        
        print()
        print('Buscando por aluno')
        print()

        alunoBusca = input('Informe o aluno que deseja buscar: ')
        achou = False

        for alunos in range(len(projetos)):
            if alunoBusca.upper() == projetos[alunos]["nome"].upper():
                achou = True
                print(f'O aluno {projetos[alunos]["nome"]} foi encontrado o nome do seu projeto é {projetos[alunos]["projeto"]} ele está no curso {projetos[alunos]["curso"]} com professor orientador {projetos[alunos]["Prof"]} e o seu ano de desenvolvimento foi {projetos[alunos]["anoDes"]}')

        if not achou:
            print(f'Não foi possivel localizar o projeto do aluno {alunoBusca}')
            
        sair = input('Deseja buscar por mais alunos? (S/N): ')
            
        if sair.upper() == 'N':
            print('Você saiu do submenu de busca por alunos!')
            break
        
        print()
        print('=' * 50)

#
def buscaNomeProjeto(projetos):
    
    while True:
        
        print()
        print('Por qual nome de projeto deseja buscar? ')
        print()

        projetoBusca = input('Informe o nome do projeto que deseja buscar? ')
        achou = False

        for trabalhos in range(len(projetos)):
            if projetoBusca.upper() == projetos[trabalhos]["projeto"].upper():
                achou = True
                print(f'O projeto {projetos[trabalhos]["projeto"]} foi encontrado pertence ao aluno {projetos[trabalhos]["nome"]} ele está no curso {projetos[trabalhos]["curso"]} com professor orientador {projetos[trabalhos]["Prof"]} e o seu ano de desenvolvimento foi {projetos[trabalhos]["anoDes"]}')

        if not achou:
            print(f'Não foi possivel localizar o projeto {projetoBusca}')
        
        sair = input('Deseja buscar por mais projetos? (S/N): ')
        
        if sair.upper() == 'N':
            print('Você saiu da busca de projetos!')
            break
        
        print()
        print('=' * 50)
   
#     
def buscaCurso(projetos):
    
    while True:
        
        print()
        print('Por qual curso deseja buscar? ')
        print()

        projetoCurso = input('Informe o nome do curso que deseja buscar? ')
        achou = False

        for trabalhos in range(len(projetos)):
            if projetoCurso.upper() == projetos[trabalhos]["curso"].upper():
                achou = True
                print(f'O curso {projetos[trabalhos]["curso"]} foi encontrado pertence ao aluno{projetos[trabalhos]["nome"]} seu projeto {projetos[trabalhos]["projeto"]} com professor orientador {projetos[trabalhos]["Prof"]} e o seu ano de desenvolvimento foi {projetos[trabalhos]["anoDes"]}')

        if not achou:
            print(f'Não foi possivel localizar o curso {projetoCurso}')
            
        sair = input('Deseja buscar por mais algum curso? (S/N): ')
        
        if sair.upper() == 'N':
            print('Você saiu do submenu busca de curso!')
            break
        
        print()
        print('=' * 50)

#      
def buscaProfessor(projetos):
    
    while True:
        
        print()
        print('Por qual professor orientador deseja buscar? ')
        print()

        projetoProf = input('Informe o nome do professor orientador que deseja buscar? ')
        achou = False

        for trabalhos in range(len(projetos)):
            if projetoProf.upper() == projetos[trabalhos]["Prof"].upper():
                achou = True
                print(f'O projeto {projetos[trabalhos]["projeto"]} foi encontrado pertence ao aluno {projetos[trabalhos]["nome"]} ele está no curso {projetos[trabalhos]["curso"]} com professor orientador {projetos[trabalhos]["Prof"]} e o seu ano de desenvolvimento foi {projetos[trabalhos]["anoDes"]}')

        if not achou:
            print(f'Não foi possivel localizar o professor orientador {projetoProf}')
            
        sair = input('Deseja buscar por mais professores orientadores? (S/N): ')
        
        if sair.upper() == 'N':
            print('Você saiu do submenu busca de pessoas!')
            break
        
        print()
        print('=' * 50)
 
#       
def buscaAno(projetos):
    
    while True:
        
        print()
        print('Por qual ano deseja buscar? ')
        print()

        projetoAno = int(input('Informe o ano que deseja buscar? '))
        achou = False

        for trabalhos in range(len(projetos)):
            if projetoAno == projetos[trabalhos]["anoDes"]:
                achou = True
                print(f'O projeto {projetos[trabalhos]["projeto"]} foi encontrado pertence ao aluno {projetos[trabalhos]["nome"]} ele está no curso {projetos[trabalhos]["curso"]} com professor orientador {projetos[trabalhos]["Prof"]} e o seu ano de desenvolvimento foi {projetos[trabalhos]["anoDes"]}')

        if not achou:
            print(f'Não foi possivel localizar o ano de desenvolvimento {projetoAno}')
    
        sair = input('Deseja buscar por mais algum ano de desenvolvimento? (S/N): ')
        
        if sair.upper() == 'N':
            print('Você saiu do submenu de busca por ano de desenvolvimento!')
            break
        
        print()
        print('=' * 50)
        
#
def Ordem_A(Ordem_Aluno):

    while True:
        print('=' * 50)
        print('Como deseja ordenar os Projetos? \n')
        print('1 - Por Aluno')
        print('2 - Por Projeto')
        print('3 - Por Curso')
        print('4 - Por Professor')
        print('5 - Por Ano')
        print('6 - Sair')

        opc3 = int(input('Informe a opção desejada: '))

        if opc3 == 1:
        
            listagemAluno(Ordem_Aluno)

        elif opc3 == 2:
            
            listagemProjeto(Ordem_Aluno)

        elif opc3 == 3:
        
            listagemCurso(Ordem_Aluno)

        elif opc3 == 4:
            
            listagemProfessor(Ordem_Aluno)

        elif opc3 == 5:
            
            listagemAno(Ordem_Aluno)
        
        elif opc3 == 6:
            break
            
        else:
            
            mensagem()
 
#   
def listagemAluno(Ordem_Aluno):
    
    for x in range(1, len(Ordem_Aluno)):
        for y in range(len(Ordem_Aluno) -1 , 0 , -1):
            if Ordem_Aluno[y]["nome"] < Ordem_Aluno[y  - 1]["nome"]:
                auxNome		        = Ordem_Aluno[y]
                Ordem_Aluno[y]		= Ordem_Aluno[y - 1]
                Ordem_Aluno[y  -1 ] = auxNome

    mensagemExibe("nome")
            
    info(Ordem_Aluno)

#
def listagemProjeto(Ordem_Aluno):
    
    for x in range(1, len(Ordem_Aluno)):
        for y in range(len(Ordem_Aluno) -1 , 0 , -1):
            if Ordem_Aluno[y ]["projeto"] < Ordem_Aluno[y  - 1]["projeto"]:
                auxNome             = Ordem_Aluno[y ]
                Ordem_Aluno[y ]     = Ordem_Aluno[y  -1 ]
                Ordem_Aluno[y  -1 ] = auxNome

    mensagemExibe("projeto")
        
    info(Ordem_Aluno)

#        
def listagemCurso(Ordem_Aluno):
    
    for x in range(1, len(Ordem_Aluno)):
        for y in range(len(Ordem_Aluno) -1 , 0 , -1):
            if Ordem_Aluno[y]["curso"] < Ordem_Aluno[y - 1]["curso"]:
                auxNome             = Ordem_Aluno[y]
                Ordem_Aluno[y]      = Ordem_Aluno[y -1 ]
                Ordem_Aluno[y -1 ]  = auxNome

    mensagemExibe("curso")
    
    info(Ordem_Aluno)

#
def listagemProfessor(Ordem_Aluno):
    
    for x in range(1, len(Ordem_Aluno)):
            for y in range(len(Ordem_Aluno) -1 , 0 , -1):
                if Ordem_Aluno[y]["Prof"] < Ordem_Aluno[y - 1]["Prof"]:
                    auxNome             = Ordem_Aluno[y]
                    Ordem_Aluno[y]      = Ordem_Aluno[y -1 ]
                    Ordem_Aluno[y -1 ]  = auxNome

    mensagemExibe("professor orientador")
    
    info(Ordem_Aluno)

#
def listagemAno(Ordem_Aluno):
    
    for x in range(1, len(Ordem_Aluno)):
            for y in range(len(Ordem_Aluno) -1 , 0 , -1):
                if Ordem_Aluno[y]["anoDes"] < Ordem_Aluno[y - 1]["anoDes"]:
                    auxNome             = Ordem_Aluno[y]
                    Ordem_Aluno[y]      = Ordem_Aluno[y -1 ]
                    Ordem_Aluno[y -1 ]  = auxNome

    mensagemExibe("ano de desenvolvimento")
    
    info(Ordem_Aluno)

#
def mensagem():
    
    print('Por favor informe uma opção válida!')

#
def mensagemExibe(por):
    
    print(f'Exibindo projetos por {por} em ordem alfabetica')
    
    print('Nome                   Projeto                    Curso                   Professor                   Ano de Desenvolvimento')
    
def info(Ordem_Aluno):

    for x in range(len(Ordem_Aluno)):
        print(f'{Ordem_Aluno[x]["nome"]:<20}', end='')
        print(f'{Ordem_Aluno[x]["projeto"]:>14}', end='')
        print(f'{Ordem_Aluno[x]["curso"]:>18}', end='')
        print(f'{Ordem_Aluno[x]["Prof"]:>28}', end='')
        print(f'{Ordem_Aluno[x]["anoDes"]:>26}')

#inicio do programa

projetos = list()

menu()



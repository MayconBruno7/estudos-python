"""
	AUTOR.....: Maycon Bruno
	DATA/HORA.: 19/11/2022 AS 12:44
	
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

import time
from datetime import datetime

def menu():
    
    global folha

    while True:

        print("MENU DE OPÇÕES:")
        print()
        print("1) Cadastrar")
        print("2) Listagem de funcionários")
        print("3) Busca de funcionários")
        print("4) O nome e função do funcionário que possui o menor salário")
        print("5) Funcionário mais velho")
        print("6) A média de salário de todos os funcionários")
        print("7) Sair")
        print()

        opc = int(input('Informe a opção desejada: '))
        
        if opc == 1:
            
            cadastrarFuncionario()
            
        elif opc == 2:
            
            print("SUB MENU LISTAGEM")
            print()
            print("1) Por Nome")
            print("2) Por Idade aposentadoria decrescente")
            print("3) Por Função ")
            print()

            subMenu = int(input("Informe a opção desejada: "))

            if subMenu == 1:

                listagemFuncionariosNome(folha)

            elif subMenu == 2:

                listagemAposentadoria(folha)

            elif subMenu == 3:

                listagemFuncao(folha)
                
            else:
                print('Por favor insira uma opção válida!')        
        elif opc == 3:
            
            print("SUB MENU BUSCA")
            print()
            print("1) Por Nome")
            print("2) Por Função ")
            print("")
            subMenu = int(input("Informe a opção desejada: "))

            if subMenu == 1 or subMenu == 2:

                buscaFuncionarios(folha, subMenu)
                
            else:
                print('Por favor insira uma opção válida!')
            
        elif opc == 4:
            
            menorSalario(folha)
            
        elif opc == 5:
            
            maisVelho(folha)
            
        elif opc == 6:
            
            mediaSalarios(folha)
            
        elif opc == 7:
            
            resp = input("Deseja realmente abandonar o sistema (S/N) ? ")

            if resp.upper() == "S":
                print('Você finalizou o programa!')
                break
                
        else:
            print('Favor informar um opção válida!')

def cadastrarFuncionario():
    
    listaFuncionarios = dict()
    
    global folha
    
    listaFuncionarios["nome"]           = input('Informe o nome do funcionário: ')
    listaFuncionarios["anoNasc"]        = int(input('Informe o ano de nascimento do funcionário: '))
    listaFuncionarios["sexo"]           = input('Informe o sexo do funcionário: ')
    listaFuncionarios["salario"]        = float(input('Informe o salário do funcionário: '))
    listaFuncionarios["funcao"]         = input('Informe a função do funcionário: ')
    listaFuncionarios["anoPEmprego"]    = int(input('Informe o ano de primeiro emprego do funcionário: '))
    
    time.sleep(3)
    
    if ( datetime.now().year - listaFuncionarios["anoNasc"] ) > 40:
        
        if listaFuncionarios["sexo"].upper() == 'F':
            listaFuncionarios["anoAposentadoria"] = listaFuncionarios["anoPEmprego"] + 30

        if listaFuncionarios["sexo"].upper() == 'M':
            listaFuncionarios["anoAposentadoria"] = listaFuncionarios["anoPEmprego"] + 35
            
    folha.append(listaFuncionarios.copy())
    
def listagemDados(folha):

	sexoDescricao = { "M": "MASCULINO" , "F": "FEMININO" }

	print(f"{folha['nome']:30}", end="  ")
	print(f"{folha['anoNasc']:>4.0f}", end="  ")
	print(f"{sexoDescricao[ folha['sexo'].upper() ]:9}", end="  ")
	print(f"{folha['salario']:>14.2f}", end="  ")
	print(f"{folha['funcao']:20}", end="  ")
	print(f"{folha['anoPEmprego']:>4.0f}", end="    ")

	if "anoAposentadoria" in folha:
		print(f"{folha['anoAposentadoria']:>4.0f}")
	else:
		print("")
  
def cabecalho():
    
	print("=" * 110)
	print("NOME                            NASC  SEXO       SALÁRIO         FUNÇÃO                1º EMP  APOSENTADORIA")
	print("=" * 110)
 
def listagem(folha):
    
    cabecalho()
    
    for pessoas in folha:
        listagemDados(pessoas)

def listagemFuncionariosNome(folha):

    for x in range(1, len(folha)):
        for y in range(len(folha) - 1, 0, -1):
            if folha["nome"][y] < folha["nome"][y - 1]:
                aux             = folha[y]
                folha[y]        = folha[y - 1]
                folha[y - 1]    = aux
                
    listagem(folha)
    print()
    

def listagemAposentadoria(folha):

    for x in range(1, len(folha)):
        for y in range(len(folha) - 1, 0, -1):
            if folha["AnoAposentadoria"][y] < folha["AnoAposentadoria"][y - 1]:
                aux             = folha[y]
                folha[y]        = folha[y - 1]
                folha[y - 1]    = aux
                
    listagem(folha)
    print()
    
def listagemFuncao(folha):

    for x in range(1, len(folha)):
        for y in range(len(folha) - 1, 0, -1):
            if folha["funcao"][y] < folha["funcao"][y - 1]:
                aux             = folha[y]
                folha[y]        = folha[y - 1]
                folha[y - 1]    = aux
                
    listagem(folha)
    print()
    
def buscaFuncionarios(listaDeFuncionarios, subMenu):
    
    buscaFuncionarios = input('Informe o texto que deseja buscar: ')
    achou = False
    
    print()    
    cabecalho()
    
    for pessoas in listaDeFuncionarios:
        
        exibe = False
        
        if subMenu == 1:
            if buscaFuncionarios.upper() == pessoas['nome'].upper():
                exibe = True

        elif subMenu == 2:

            if buscaFuncionarios.upper() == pessoas['funcao'].upper():
                exibe = True

        if exibe:

            achou = True

            listagemDados(pessoas)

    if not achou:
        print("Não foi possivel localizar funcionários para a expressão informada.")

        
def menorSalario(folha):
    
    menor = - 1
        
    for x in range(len(folha)):
        
        if x == 0:
            menor = x
            
        else:
            if folha[x]["salario"] < folha[menor]["salario"]:
                menor = x
                
    print()
    print(f"O funcionário com o menor salário é {folha[menor]['nome']} e trabalha na função {folha[menor]['funcao']}")
    print()
        
def maisVelho(folha):
    
    velho = - 1
    
    for x in range(len(folha)): 
        
        if x == 0:
            velho = x
            
        else:
            if folha[x]["anoNasc"] < folha[velho]["anoNasc"]:
                velho = x 
         
    print()
    print(f"O funcionário com o mais velho é {folha[velho]['nome']} e trabalha na função {folha[velho]['funcao']}")
    print()
    
def mediaSalarios(folha):
    
    soma = 0
    
    for salarios in folha:
        soma += salarios["salario"]
        
    print(f'A media de salario dos funcionarios é {(soma / len(folha))}')    
    

    
    
#inicio

folha = list()

menu()
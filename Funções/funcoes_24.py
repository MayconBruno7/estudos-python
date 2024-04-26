"""
	AUTOR.....: Maycon Bruno
	DATA/HORA.: 19/11/2022 AS 12:44
	
		24) Ler duas matrizes A e B do tipo lista com 10 números inteiros cada. Construir uma lista C do mesmo tipo, sendo esta a junção das duas outras listas. Desta forma , 
            C deverá ter o dobro de elementos de A e B.

		    Neste exercício deverá ser criada uma sub-rotina para cada tarefa do programa, ou seja serão quatro sub-rotinas, sendo 	duas para leituras das listas, uma para a junção
            e a última para apresentação dos dados. No final o programa principal deverá chamar as rotinas definidas.
            
"""

def criacaoLista():
    
    criaLista = list()
    
    for x in range(5):
        
        valores = int(input('Informe os valores que deseja adiciionar a lista: '))
        criaLista.append(valores)
        
    return criaLista

def criaListaC(listA, listB):
    
    criaListC = list()
    
    for valor in listA:
        criaListC.append(valor)
    
    for valor in listB:
        criaListC.append(valor)
        
    return criaListC

def exibeListas(listA, listB, listC):
    
    print("=" * 100)
    print("    A        B        C")

    for x in range(len(listC)):
        if (len(listC) / 2) > x:
            print(f"{listA[x]:>5.0f}", end="    ")
            print(f"{listB[x]:>5.0f}", end="    ")
        else:
            print(" " * 18, end="")

        print(f"{listC[x]:>5.0f}")

    print("=" * 100)
        
#inicio

listA = criacaoLista()
listB = criacaoLista()
listC = criaListaC(listA, listB)

lista = exibeListas(listA, listB, listC)
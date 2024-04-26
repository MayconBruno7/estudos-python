"""
AUTOR.....: Aldecir Fonseca 
DATA/HORA.: 08/08/2022 as 20:33
FINALIDADE: Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

#vetorList = []
 
#i = - 10

#while i < len(vetorList):

 #   i = i + 1

#for i in range(len(vetorList)):
	#print(f'{vetorList[i]}', end=' ')

listaNumerosReais = []

print ('Informe os 10 numeros reais')

for i in range(10):

	listaNumerosReais.append(int(input('Numero '+ str(i+1) + ':\n')))
listaNumerosReais.reverse()

print (listaNumerosReais) 
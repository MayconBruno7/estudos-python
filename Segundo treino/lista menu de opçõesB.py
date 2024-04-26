"""
AUTOR.....: Maycon Bruno
DATA/HORA.: 24/09/2022 as 13:06
FINALIDADE: 11) Digite 15 nomes de pessoas no final permita o usuário digitar um nome que deseja verificar se existe nos 15 nomes digitados,
				 caso exista exibir o nome e a posição na lista, caso contrário exibir mensagem de nome não localizado
"""


nome = list()

for x in range(15):

    nome.append(input('Informe o nome: '))

print()
buscaNome = input('Informe o nome para pesquisar: ')
print()

lAchou = False
    
for x in range(len(nome)):

    if buscaNome.upper() == nome[x].upper():
        print(f'O {nome[x]} está na posiçao {x}')
        lAchou = True
    if not lAchou:
        print(f'{buscaNome} não foi encontrado!')

    
        

    




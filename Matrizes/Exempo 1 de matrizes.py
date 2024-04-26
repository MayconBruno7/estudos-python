"""
Autor: Maycon Bruno
Data: 01/10/2022 ás 11:32

    Faça um programa que armazene o nome e a idade de 3 pessoas em uma matriz e depois mostre esssas pessoas na tela do usuario,
    após isso adicione mais uma pessoa, e print novamente a matriz.

"""

pessoas = [ ['Mariana', 19],
            ['Maycon', 19],
            ['Joana', 22]
        ]

print()
print('Exibindo a Matriz')

for x in range(len(pessoas)):
    print(f'{pessoas[x][0]} tem {pessoas[x][1]} ano(s)')

print()
print('Exibindo apenas a segunda pessoa da matriz')
print(f'{pessoas[1][0]} tem {pessoas[1][1]} ano(s)') 

pessoasLista = []

pessoasLista.append('Eduardo')
pessoasLista.append(25)

pessoas.append(pessoasLista)

print()
print('Exibindo as pessoas que estão na nova Matriz')
print()

for l in range(len(pessoas)):
    print(f'{pessoas[l][0]} tem {pessoas[l][1]} ano(s)')
print()
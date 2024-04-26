"""
AUTOR.....: Aldecir Fonseca 
DATA/HORA.: 18/10/2022 as 18:43
FINALIDADE: 16) A direção da FASM quer agora informatizar a biblioteca. Para começar ela quer que todos os livros que estão nas estantes sejam cadastrados no computador. Foi 
                decidido que as seguintes informações de cada livro deveram ser armazenadas no computador: Código, titulo, autor, ano de edição e quantidade. 
                Crie um programa com uma interface que irá receber os dados dos livros até o usuário informe o código de livro igual a ZERO, estes dados deverão ser armazenados em um 
                dicionário. Ao final determine e exiba os dados do livro que possui a maior quantidade de livros e o total de livros que a biblioteca possui.
"""

livros      = dict()
biblioteca  = list()

indMaiorQtd = -1

while True:

    print()
    print('Adicionando livros')
    print('Favor informar os dados do livro')

    livros['codigo'] = int(input('Informe o codigo do livro ou (0) para terminar o cadastramento de livros: '))

    totalLivros = 0

    if livros['codigo'] == 0:
        break

    else:

        livros['titulo']        = input('Informe o titulo do livro: ')
        livros['autor']         = input('Informe o nome do autor do livro: ')
        livros['anoEdicao']     = int(input('Informe o ano de edição do livro: '))
        livros['quantidade']    = int(input('Informe a quantidade de livros da edição: '))

        biblioteca.append(livros.copy())
        totalLivros += livros['quantidade']

        if len(biblioteca) == 1:
            indMaiorQtd = 0
        
        else:
            if biblioteca[len(biblioteca) - 1]['quantidade'] < biblioteca[indMaiorQtd]['quantidade']:
                indMaiorQtd = len(biblioteca) - 1
        
print()
print(f'O livro que possui maior quantidade é {biblioteca[indMaiorQtd]["titulo"]} do autor(a) {biblioteca[indMaiorQtd]["autor"]} com seu ano de edição {biblioteca[indMaiorQtd]["anoEdicao"]} e existem {biblioteca[indMaiorQtd]["quantidade"]} livros dessa edição.')
print()
print(f'O total de livros que estão cadastrados da biblioteca é {totalLivros}.')
print()
print('Apresentando a listagem dos livros')
print()
print('Código Titulo                Autor                 Ano Edição  Quantidade')
print()

for livros in biblioteca:
    print(f'{livros["codigo"]:<4.0f}', end='    ')
    print(f'{livros["titulo"]:<18}', end='  ')
    print(f'{livros["autor"]:<20}', end='   ')
    print(f'{livros["anoEdicao"]}', end='   ')
    print(f'{livros["quantidade"]:>10.0f}')
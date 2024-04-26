"""
    Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    a) o produto do dobro do primeiro com metade do segundo .
    b) a soma do triplo do primeiro com o terceiro.
    c) o terceiro elevado ao cubo.

"""

while True:

    print('Menu de opções')
    print('Pressione "1" digitar numeros.')
    print('2) o produto do dobro do primeiro com metade do segundo.')
    print('3) a soma do triplo do primeiro com o terceiro.')
    print('4) o terceiro elevado ao cubo.')
    print('Pressione "0" para sair')
    print()
    opcao = int(input('Informe a opção desejada: '))

    if opcao == 1: 
        print('Informando os numeros')
        inteiro1 = int(input('Informe o numero inteiro: '))
        inteiro2 = int(input('Informe o numero inteiro: '))
        real = float(input('Informe o numero real: '))
        print()

    elif opcao == 2:
        print('Exibindo a opção (a)')
        print(f'O produto do dobro do primeiro é {inteiro1 * 2} com a metade do segundo que é {inteiro2 / 2} assim esse calculo fica {(inteiro1 * 2) + (inteiro2 / 2)}.')
        print()

    elif opcao == 3:
        print('Exbibindo a opção (b)')
        print(f'O triplo do primeiro é {inteiro1 * 3} com o terceiro que é {real} essa conta fica {(inteiro1 * 3) + (real)}.')
        print()

    elif opcao == 4:
        print('Exibindo a opção (c)')
        print(f'O terceiro numero é {real} e elevado ao cubo fica {real ** 3}.')
        print()
    elif opcao == 0:
        break

    else:
        print('Opção informada inválida!')
        print()

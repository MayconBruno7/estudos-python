"""
-------------------------------------------------
DATA/HORA..: 22/07/2022 às 17:35
ESCRITO POR: Maycon Bruno
FINALIDADE.: 37) O cardápio de uma lancheira é o seguinte

                CODIGO  DESCRICAO                       PREÇO
                100     Cachorro Quente                  5,00
                101     Hamburger                       12,00
                102     xBurguer                        14,50
                103     xEggBurguer                     16,00
                104     Cachorrão de salsicha           11,50
                105     xTudo                           18,00

            Escrever um algoritmo que leia o código do item pedido, a 
            quantidade e calcule o valor a ser pago por aquele lanche. 
            O usuário poderá pedir quantos lanches desejar. Se informado 
            quantidade zero interrompe a execução e exibe o total do pedido.
-------------------------------------------------
"""

Lanches = 0 

while True:

    print(" CODIGO  DESCRICAO                      PREÇO")
    print("100       Cachorro Quente               5,00")
    print("101        Hamburger                    12,00")            
    print("102       xBurguer                     14,50")           
    print("103       xEggBurguer                  16,00")          
    print("104        Cachorrão de salsicha        11,50")            
    print("105        xTudo                        18,00")     

    print("=" * 50)

    codigo = int(input("Informe o codigo do produto:")) 

    if codigo == 0:
        break

    elif codigo >= 100 and codigo <= 105:
        qtdLanches = int(input("Informe a quantidade de lanches:"))

        valor = 0

        if codigo == 100:
            valor = qtdLanches * 5
        elif codigo == 101:
            valor = qtdLanches * 12
        elif codigo == 102:
            valor = qtdLanches * 14.5
        elif codigo == 103:
            valor = qtdLanches * 16
        elif codigo == 104:
            valor = qtdLanches * 11.5
        elif codigo == 105:
            valor = qtdLanches * 18

        print(f"Valor total do item é R$ {valor:<12.2f}")
        print("=" * 50)

        Lanches += valor

print("=" * 50)
print(f"O valor a ser pago pelos lanches é:{Lanches}")
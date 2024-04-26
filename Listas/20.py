"""
-------------------------------------------------
DATA/HORA..: 10/08/2022 às 15:12
ESCRITO POR: Maycon Bruno
FINALIDADE.: 20) Crie um programa para concessionária de pedágios. 
                O usuário deve digitar a quantidade de eixos (rodas)
                do veiculo, sabemos que nenhum veículo possui
                menos que 2 eixos (rodas), e para nosso
                exemplo não iremos aceitar mais de 9 (eixos) roda. 
                O valor do pedágio é de R$ 6.35 por eixo. 
                Exiba no final o valor a ser pago e a placa do veículo.
-------------------------------------------------
"""

qtdEixos = int(input("Informe a quantidade de eixos do veiculo:"))

if qtdEixos >= 2 and qtdEixos <= 9:
    placa = input("Nos informe a placa do veiculo:")

    valorPedagio = qtdEixos * 6.35

    print("")
    print("=" * 50)
    print(f"O valor do pedagio é de R$ 6.35")
    print(f"O valor a ser pago do pedagio é de {valorPedagio} para o veiculo de placa {placa}.")
    print("")
    print("=" * 50)

else:
    print("")
    print("=" * 50)
    print("Favor informar uma quantidade de eixos válida")
    print("")       
    print("=" * 50)



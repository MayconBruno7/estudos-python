"""
-------------------------------------------------
DATA/HORA..: 26/06/2022 às 14:41
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

qtdEixos = int(input("Informe a quantidade de eixos:.."))

if qtdEixos >= 2 and qtdEixos <= 9:

    placa = input("Informe a placa do veiculo:")
    
    total = qtdEixos * 6.35

    print("O valor do pedagio é R$ 6,35")
    print("=" * 50)
    print("Placa:...", placa)
    print("Com o veiculo com a quantidade de eixos igual á,", qtdEixos, "o valor total a ser pago é", total)


else:
    print("Quantidade de eixos inválida!")
    




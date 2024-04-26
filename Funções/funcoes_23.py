"""
	AUTOR.....: Maycon Bruno
	DATA/HORA.: 11/11/2022 AS 14:04
	
		23) Faça uma função que recebe o valor total das vendas do tipo real e a sigla de um estado da região sudeste. A função deverá calcular o valor de imposto e retornar o 
            imposto a ser pago sobre o valor das vendas seguindo a tabela de alíquotas por estado conforme abaixo:

            ESTADO 	ALIQUOTA
            ES 		7%
            MG 		18%
            SP		12%
            RJ		12%
            
"""

def calculaImposto(uf, valorVendas):
      
      valorImposto = 0
      
      if uf =='ES':
            valorImposto = (valorVendas * 7) / 100
      
      elif uf == 'MG':
            valorImposto = (valorVendas * 18) / 100
      
      elif uf == 'SP':
            valorImposto = (valorVendas * 12) / 100
            
      elif uf == 'RJ':
            valorImposto = (valorVendas * 12) / 100
            
      return valorImposto

vendas = float(input('Informe o valor das vendas: '))
estado = input('Informe a UF (ES/MG/SP/RJ) em que as vendas foram efetuadas: ')

impostos = calculaImposto(estado.upper(), vendas)
            
print("=" * 50 )
print(f'Valor dos impostos para R$ {impostos:>14.2f}')
print(f'Valor das vendas liquida...R$ {(vendas - impostos):>14.2f}')
print("=" * 50 )
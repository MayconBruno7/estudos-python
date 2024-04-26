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

def calculoImposto(uf, valor):
      
    valorImposto = 0 
      
    if uf == 'ES':
        valorImposto = (valor * 7) / 100
        
    elif uf == 'MG':
        valorImposto = (valor * 18) / 100
    
    elif uf == 'SP' or uf == 'RJ':
        valorImposto = (valor * 12)
        
    return valorImposto

def getUF():
    
    ufs = ('ES', 'MG', 'SP', 'RJ')
    
    while True:
        
        uf = input('Informe a UF (ES/MG/SP/RJ): ')
        
        if uf.upper() in ufs:
            break
        
    return uf

#inicio 

valor   = float(input('Informe o valor das vendas: '))
estado  = getUF()

print()
print(f'O valor das vendas foi: {valor}')
print()

imposto = calculoImposto(valor = valor, uf = estado.upper())

print('-' * 40)
print(f'O valor do imposto a ser pago no estado {estado.upper()} é: {imposto}')
print(f'O valor liquido a ser é de: {valor - imposto}')
print('-' * 40)



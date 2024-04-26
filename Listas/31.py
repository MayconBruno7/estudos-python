"""
-------------------------------------------------
DATA/HORA..: 12/08/2022 às 19:43
ESCRITO POR: Maycon Bruno
FINALIDADE.:  31) Solicite o Salário Bruto de um funcionário. 
                Considere como valor do salário mínimo: R$ 998,00. Calcule e exiba o 
                salário liquido descontando o imposto de renda conforme tabela abaixo. 
                Formula: Salário Liquido ← Salário Bruto – Imposto de Renda. 
                Os valores da alíquota para cálculo do imposto de renda são

                Salário Bruto               Alíquota
                -------------------------------------
                Até 2 salários mínimos      Isento
                2 a 3 salários mínimos      7,5%
                3 a 5 salários mínimos      15%
                5 a 7 salários mínimos      22,5%
                Acima de 7 sal. mínimos     30%
-------------------------------------------------
"""

salarioBruto = float(input("Informe o seu salario bruto:"))
salarioLiquido = 0 
iR = 0 
iRenda = 0
salarioMinimo = 998

if salarioBruto <= salarioMinimo * 2:
    print("Você esta insento de imposto de renda!")
elif salarioBruto <= salarioMinimo * 3:
    iR = (salarioBruto * 7.5) / 100 
    iRenda = (7.5)
elif salarioBruto <= salarioMinimo * 5:
    iR = (salarioBruto * 15) / 100
    iRenda = (15)
elif salarioBruto <= salarioMinimo * 7:
    iR = (salarioBruto * 22.5) / 100
    iRenda = (22.5)
else:
    iR = (salarioBruto * 30) / 100
    iRenda = (30) 

salarioLiquido = (salarioBruto - iR) 

print()
print("=" * 50)
print()
print(f"O seu salario bruto é de R$ {salarioBruto} e foi aplicado uma porcentagem de {iRenda}% de imposto de renda.")
print(f"Sendo assim o total descontado de imposto de renda é R$ {iR}.")
print(f"O seu salario liquido é de R$ {salarioLiquido}.")
print()
print()
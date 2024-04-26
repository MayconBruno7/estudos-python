"""
-------------------------------------------------
DATA/HORA..: 27/06/2022 às 13:54
ESCRITO POR: Maycon Bruno
FINALIDADE.: 31) Solicite o Salário Bruto de um funcionário. 
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
salarioBruto = float(input("Informe o seu salario Bruto:"))

salarioMinimo = 998.00
salarioLiquido = 0
descImp = 0

if salarioBruto <= (salarioMinimo * 2):
    print("Você está isento de imposto de renda!")
elif salarioBruto <= (salarioMinimo * 3):
    descImp = (salarioBruto * 7.5) / 100
elif salarioBruto <= (salarioMinimo * 5):
    descImp = (salarioBruto * 15) / 100
elif salarioBruto <= (salarioMinimo * 7):
    descImp = (salarioBruto * 22.5) / 100
else:
    descImp = (salarioBruto * 30) / 100

salarioLiquido = salarioBruto - descImp

print("=" * 50)
print("Salario Bruto: R$", salarioBruto)
print("Será descontado: R$", descImp)
print("O seu salário liquido é: R$", salarioLiquido )
 
 

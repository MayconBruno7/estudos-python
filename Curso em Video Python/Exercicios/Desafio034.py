salario_funcionario = float(input("Informe o salário do funcionário: "))

if salario_funcionario > 1250:
    print("Salário atual: {}".format(salario_funcionario))    
    print("Salário com aumento de 10%: {}".format(salario_funcionario + (salario_funcionario * 10) / 100))

else: 
    print("Salário atual: {}".format(salario_funcionario))    
    print("Salário com aumento de 15%: {}".format(salario_funcionario + (salario_funcionario * 15) / 100))
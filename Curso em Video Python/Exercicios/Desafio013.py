sal_funcionario = float(input('Informe o salário do funcionário: R$'))
sal_com_aumento = sal_funcionario + (sal_funcionario * 15) / 100

print('O salário do funcionário que era R$ {0} com o aumento de 15% é igual á: R$ {1}' . format(sal_funcionario, sal_com_aumento))
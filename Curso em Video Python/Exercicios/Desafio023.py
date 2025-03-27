

while True :
    
    num = str(input('Informe um número de 0 a 9999: '))
    
    if int(num) < 0 :
        print('Numero inválido') 
    elif int(num) > 9999:
        print('Nuemro invalido')
    
    break

print("Unidade: {}".format(num[3] if len(num) > 3 else "Nenhum número"))
print("Dezena: {}".format(num[2] if len(num) > 2 else "Nenhum número"))
print("Centena: {}".format(num[1] if len(num) > 1 else "Nenhum número"))
print("Milhar: {}".format(num[0] if len(num) > 0 else "Nenhum número"))


from math import sqrt

cat_oposto = float(input("Informe o comprimento do cateto oposto:  "))
cat_adjace = float(input("Informe o comprimento do cateto adjacente: "))

comprimento_hipote = round(sqrt(cat_oposto**2 + cat_adjace**2))

print("Comprimento da hipotenusa: {0}" . format(comprimento_hipote))
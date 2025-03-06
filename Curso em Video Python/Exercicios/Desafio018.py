from math import sin, cos,tan

angulo = int(input("Informe o angulo: "))

seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

print("Seno: {:.2f}".format(seno))
print("Cosseno: {:.2f}".format(cosseno))
print("Tangente: {:.2f}".format(tangente))
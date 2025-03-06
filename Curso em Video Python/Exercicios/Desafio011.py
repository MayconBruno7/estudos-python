larg_parede = float(input('Informe a largura da parede: '))
altu_parede = float(input('Informe a altura da parede: '))

print("Sua parede tem a dimensão {0} x {1} e a sua área é de {2}m2" . format(larg_parede, altu_parede, (larg_parede * altu_parede)))
print("Para pintar essa parede, você precisara de {0}l de tinta" . format((larg_parede * altu_parede) / 2))
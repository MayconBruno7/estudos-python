from datetime import date

ano = int(input("Informe o ano para a analise: "))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0) or ano:
    print("O ano informado é bissexto!")
else:
    print("O ano não é bissexto!")
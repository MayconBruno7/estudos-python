r1 = float(input("Informe a primeira reta: "))
r2 = float(input("Informe a segunda reta: "))
r3 = float(input("Informe a terceira reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("As retas podem formar um triangulo")
    
else: 
    print("As retas não podem formar um triangulo")
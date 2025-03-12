import os
os.system("clear")

morango = float(input("Digite quantos quilos de morango: "))
maca = float(input("Digite quantos quilos de maca: "))

if morango <= 5:
    valor = morango * 2.50
else:
    valor = morango * 2.20
if maca <= 5:
    valor = maca * 1.80
else:
    valor = maca * 1.5

if (morango + maca) > 10 or valor > 15:

    print(f"o valor a ser pago e R$ {valor:2 f} ")
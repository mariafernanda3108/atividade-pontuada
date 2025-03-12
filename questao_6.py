import os
os.system("clear")

nota_um = int(input("Digite sua primeira nota: "))
nota_dois = int(input("Digite sua segunda nota: "))

media = float

media = (nota_um+nota_dois) /2
if media >= 6 :
    print(f"{media}, parabéns, parovado! ")
if media > 4 and media <6 :
    print(f"{media}, recuperação")
if media < 4:
    print(f"{media}, reprovado")
import os
os.system("clear")

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))

if a == b:
    c = a + b
    print(f"C=A+B= {c}")
else:
    c = a*b
    print(f"C=A*B ={c}") 

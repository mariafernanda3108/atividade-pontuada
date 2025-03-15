import os 
os.system("clear")

cor = input("Digite a cor do cd:" )


if cor == "verde":
    print("o preco do cd e R$ 10")
elif cor == "azul":
    print ("o preco do cd e R$ 20")
elif cor == "amarelo":
    print ("o preco do cd e R$ 30")
elif cor == "vermelho":
    print ("o preco do cd e R$ 40")
else:
    print("cor invalida! por favor,digite uma cor valida:")
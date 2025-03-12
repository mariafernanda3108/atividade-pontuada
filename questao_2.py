import os
os.system("clear")

nome = input("Digite seu nome: ")
sexo = input("Digite seu genero: ")
estado = input("Digite seu estado:")
match sexo:
    case f:
        if estado == 'casada':
            tempo = str(input("Digite seu tempo de casada"))

print("nome")
print("sexo")
print("estado")

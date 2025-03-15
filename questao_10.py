import os
os.system("clear")

#preços dos combustíveis
preco_alcool = 3.79
preco_gasolina = 6.59

litros = float(input("Quantos litros foram vendidos? "))
combustivel = input("Álcool (A) ou Gasolina (G)? ").upper()

#estrutura para calcular o valor
if combustivel == 'A':  # Álcool
    if litros <= 25:
        valor = litros * preco_alcool * 0.98  # 2% de desconto
    else:
        valor = litros * preco_alcool * 0.96  # 4% de desconto
elif combustivel == 'G':  # Gasolina
    if litros <= 25:
        valor = litros * preco_gasolina * 0.97  # 3% de desconto
    else:
        valor = litros * preco_gasolina * 0.95  # 5% de desconto
else:
    print("Combustível inválido!")
    exit()

#valor a ser pago
print("O valor a ser pago é: R$", valor)

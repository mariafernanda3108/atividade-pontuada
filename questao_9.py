import os
os.system("clear")

renda = int(input("Digite a sua renda mensal (em reais): R$ "))
valor_emprestimo = int(input("Digite o valor do empréstimo solicitado (em reais): R$ "))
num_prestacoes = int(input("Digite o número de prestações desejadas: "))

#calcula o limite máximo de empréstimo (12 vezes a renda) e o valor máximo da prestação (30% da renda)
limite_emprestimo = renda * 12
prestacao_maxima = renda * 30 // 100  #calcula 30% da rende com divisão inteira

#estrutura usada pra verificar se o empréstimo pode ser aprovado ou não
if valor_emprestimo <= limite_emprestimo:
    if valor_emprestimo // num_prestacoes <= prestacao_maxima:
        print("Empréstimo pode ser concedido.")
    else:
        print("Empréstimo não pode ser concedido: valor da prestação é muito alto.")
else:
    print("Empréstimo não pode ser concedido: valor do empréstimo excede o limite.")
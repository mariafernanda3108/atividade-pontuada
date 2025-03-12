import os
os.system("clear")

numero1 = int(input("Digite um numero: ")) 
numero2 = int(input("Digite um numero: "))
operador = input("Digite a opercao que deseja (/ - * +): ") 

match operador:
    case "+":
        resultado = numero1 + numero2
    case "-":
        resultado = numero1 - numero2
    case "*":
        resultado = numero1 * numero2
    case "/":
        resultado = numero1 + numero2

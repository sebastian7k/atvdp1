import os
os.system("cls")

#solicitando a operção

operacao = input("Digite a operação (+, -, *, /): ")
# solicitando valores

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

#calculando o resultado com match case

match operacao:
    case "+":
        resultado = A + B
    case "-":
        resultado = A - B
    case "*":
        resultado = A * B
    case "/":
        if B != 0:
            resultado = A / B
        else:
            resultado = "Erro: Divisão por zero"
    case _:
        resultado = "Operação inválida"

print(f"O resultado é: {resultado}")
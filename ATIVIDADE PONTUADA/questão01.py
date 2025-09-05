import os 
os.system("cls")


#solicitando valor A B ou C

valrA = float(input("Digite o valor A: "))
valrB = float(input("Digite o valor B: "))
valrC = float(input("Digite o valor C: "))

#cauculando 

soma = valrA + valrB 

#verificando qual o maior valor
if soma < valrC:
    print(f" A soma de A + B({soma}) é maior que C: {valrC}")
else:
    print(f"A soma de A + B({soma}) não é maior que C: {valrC}")

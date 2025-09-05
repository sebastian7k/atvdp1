import os 
os.system("cls")

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if A == B:
    C = A + B #As somas são iguais 
else:
    C = A * B # Multiplica se diferente
#resultado 
print(f"O valor de C é: {C}")
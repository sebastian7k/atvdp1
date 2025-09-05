import os
os.system("cls")

#solicitando notas 
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

#calculando a média
media = (nota1 + nota2) / 2
print(f"A média é: {media:.2f}")
#verificando

if media >6:
    print(f"Aprovado com média {media:.2f}")
elif 4.1<= media  <=5.9:
    print(f"Recuperação com média {media:.2f}")
else: 
    print(f"Reprovado com média {media:.2f}")

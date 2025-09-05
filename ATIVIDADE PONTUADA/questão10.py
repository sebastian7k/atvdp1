import os 
os.system("cls")

preco_gasolina = 5.49
preco_alcool = 3.79

litros = float(input("Digite a quantidade de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

#cauculando

if tipo_combustivel == "A":
    preco_litro = preco_alcool
    if litros <= 25:
        desconto_pct = 0.10 
    else:
        desconto_pct = 0.20 
elif tipo_combustivel == "G":
    preco_litro = preco_gasolina
    if litros <= 25:
        desconto_pct = 0.15 
    else: 
        desconto_pct = 0.30
else:
    print("Tipo de combustível inválido.")
    exit()


    #cauculando valor com desconto 

preco_total = litros * preco_litro
desconto = preco_total * desconto_pct
valor_a_pagar = preco_total - desconto


#resultado$

print(f"Valor total sem desconto : {preco_total:.2f}")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
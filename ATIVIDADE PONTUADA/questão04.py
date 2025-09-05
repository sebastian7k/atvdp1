import os 
os.system("cls")

print("""
Frutas  \t Até 5 Kg \t Acima de 5 Kg
Morango \t R$ 2,50 \t R$ 2,20
Maçã    \t R$ 1,80 \t R$ 1,50
""")

# solicitando frutas     
morango_kg = float(input("Digite a quantidade de morangos (Kg): "))
maca_kg = float(input("Digite a quantidade de maçãs (Kg): "))

# calculando o preço/kg 
if morango_kg <= 5:
    preco_morango = morango_kg * 2.50
else: 
    preco_morango = morango_kg * 2.20

if maca_kg <= 5:
    preco_maca = maca_kg * 1.80
else:
    preco_maca = maca_kg * 1.50

# desconto 
total_kg  = morango_kg + maca_kg 
total_preco = preco_morango + preco_maca

if total_kg >= 10 or total_preco > 15:
    desconto = total_preco * 0.10  # desconto de 10%
else: 
    desconto = 0

# valor final 
valor_final = total_preco - desconto

print(f"O valor final a pagar é: R$ {valor_final:.2f}")

#solicitando furtas     

morango_kg = float(input("Digite a quantidade de morangos (Kg): "))
maca_kg = float(input("Digite a quantidade de maçãs (Kg): "))

#calculando o preço/kilos 

if morango_kg <=5 :
    preco_morango = morango_kg * 2.50
else: 
    preco_morango = morango_kg * 2.20

if maca_kg <=5 :
    preco_maca = maca_kg * 1.80
else:
    preco_maca = maca_kg * 1.50


#Desconto 
total_kg  = morango_kg + maca_kg 
total_preco = preco_morango + preco_maca

if total_kg >= 10 or total_preco > 15:
    desconto = total_preco * 0.10  # desconto de 10%
else: 
    desconto = 0


    #valor final 
valor_final = total_preco - desconto

print(f"O valor final a pagar é: R$ {valor_final:.2f}")
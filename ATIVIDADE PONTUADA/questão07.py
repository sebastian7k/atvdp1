import os 
os.system("cls")


nome = input("Digite a descrição do produto: ")
quantidade = int(input("Digite a quantidade comprada: "))
preco_unitario = float(input("Digite o preço unitário: R$ "))

#cauculando 
preco_total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = preco_total * 0.02 # desconto de 2%
elif 6 <= quantidade <= 10:
    desconto = preco_total * 0.03  #desoconto de 3%
else:
    desconto = preco_total * 0.05  #desconto de 5%

total_a_pagar = preco_total - desconto

#resultados 

print(f"\nProduto: {nome}")
print(f"\nQuantidade: {quantidade}")
print(f"\nPreço unitário: R$ {preco_unitario:.2f}")
print(f"\nPreço total: R$ {preco_total:.2f}")
print(f"\nDesconto: R$ {desconto:.2f}")
print(f"\nTotal a pagar: R$ {total_a_pagar:.2f}")


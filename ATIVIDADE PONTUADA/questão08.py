import os 
os.system("cls")

cor = input("Digite a cor do CD (Verde, Azul, Amarelo, Vermelho): ").strip().lower()


match cor:
    case "verde":
        preco = 10.00
    case "azul":
        preco = 20.00
    case "amarelo":
        preco = 30.00
    case "vermelho":
        preco = 40.00
    case _:
        preco = None
if preco is not None:
    print(f"O preço do CD de cor {cor.capitalize()} é: R$ {preco:.2f}")
else:
    print("Cor inválida. Por favor, escolha entre Verde, Azul, Amarelo ou Vermelho.")
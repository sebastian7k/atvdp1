import os 
os.system("cls")

#soclitando dados 

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (M/F): ").upper() #uper para deixar maiusculo
estado_civil = input("Digite seu estado civil:").upper() 

#variavel para o tempo de casada
tempo_casada = None

if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Digite o tempo de casada: "))

                              #exinbindo dados 

print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")
if tempo_casada is not None:
    print(f"Tempo de casada: {tempo_casada} anos")
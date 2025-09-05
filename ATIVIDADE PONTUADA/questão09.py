renda_mensal = float(input("Digite a sua renda mensal: "))
valor_emprestimo = float(input("Digite o valor do empréstimo: "))
numero_parcelas = int(input("Digite o número de parcelas: "))


parcelas = valor_emprestimo / numero_parcelas

#condições 

condicao1 = valor_emprestimo <= 10 * renda_mensal
condicao2 = parcelas <= 0.3 * renda_mensal

#verificando condições para aprovação do empréstimo

if condicao1 and condicao2:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo não aprovado.")
    

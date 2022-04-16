"""Enunciado: Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, 
o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. 
A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:

Nível / Porcentagem sobre o faturamento
Basic = 30%
Silver 20%
Gold = 10%
Platinum = 5% """

#Recebe o tipo de assinatura em STRING.
Assinatura = str(input("Digite o  tipo de sua assinatura: "))
Faturamento = float(input("Digite o valor do seu faturamento: "))
calcBasic = Faturamento * 30 / 100
calcSilver = Faturamento * 20 / 100
calcGold = Faturamento * 10 / 100
calcPlatinum = Faturamento * 5 / 100

#Capitalize padroniza o texto digitado em assinatura para entrar no IF
if Assinatura.capitalize() == "Basic":
    print(f"O valor do seu faturamento anual foi de R${Faturamento:.2f}, o seu plano é o Basic conforme contrato a comissão a ser paga é de 30% do seu faturamento anual, que será no valor de R${calcBasic:.2f}.")
if Assinatura.capitalize() == "Silver":
    print(f"O valor do seu faturamento anual foi de R${Faturamento:.2f}, o seu plano é o Silver conforme contrato a comissão a ser paga é de 20% do seu faturamento anual, que será no valor de R${calcSilver:.2f}.")
if Assinatura.capitalize() == "Gold":
    print(f"O valor do seu faturamento anual foi de R${Faturamento:.2f}, o seu plano é o Gold conforme contrato a comissão a ser paga é de 10% do seu faturamento anual, que será no valor de R${calcGold:.2f}.")
if Assinatura.capitalize() == "Platinum":
    print(f"O valor do seu faturamento anual foi de R${Faturamento:.2f}, o seu plano é o Platinum conforme contrato a comissão a ser paga é de 5% do seu faturamento anual, que será no valor de R${calcPlatinum:.2f}.")
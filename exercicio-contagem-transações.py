#Recebe a quantidade de transações que será realizada.

Qtdtransacao = int(input("Digite a quantidade de transações que foram realizadas em um dia: "))
ValorTransacao = 0.0
Qtdtransacao2 = Qtdtransacao

for x in range (0, Qtdtransacao):
    # Se for precisar imprimir o valor da media fora do FOR, ele precisa estar no começo dele, 
    # pois ao terminar o loop o valor do media "retorna" para o começo do for e sai para o print 
    # com o valor correto.
    media = ValorTransacao / Qtdtransacao 
    while (Qtdtransacao2 != 0):
        print(f"Transações restantes a serem informadas o valor: {Qtdtransacao2}")
        if Qtdtransacao2 !=0:
            valor_atual = float(input("Digite o valor da transação atual: "))
            print(f"Valor da transação atual {valor_atual}")
            ValorTransacao = ValorTransacao + valor_atual
            Qtdtransacao2 = Qtdtransacao2 - 1       
        elif Qtdtransacao2 == 0:
            media = ValorTransacao / Qtdtransacao 
print(f"O valor médio de cada transação foi de {media}")
print(f"O número de transações que foram realizadas foi de {Qtdtransacao}")
print(f"O valor de cada transação foi de {media}")
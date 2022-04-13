"""Viajar é bom demais! Uma agência de viagens está propondo uma estratégia para alavancar as vendas após os impactos da pandemia
do coronavírus. A empresa ofertará descontos progressivos na compra de pacotes, dependendo do número de viajantes 
que estão no mesmo grupo e moram na mesma residência. Para ajudar a tornar esse projeto real, você deve criar um algoritmo
que receba o VALOR BRUTO do pacote, a CATEGORIA DOS ASSENTOS no voo e a QUANTIDADE DE VIAJANTES que moram em uma mesma casa 
e calcule os descontos de acordo com a tabela abaixo: O programa deverá exibir o valor BRUTO DA VIAGEM (o mesmo que foi digitado), 
o VALOR DO DESCONTO, o VALOR LÍQUIDO DA VIAGEM (valor bruto menos os descontos) e o VALOR MÉDIO POR VIAJANTE."""

categoria = (input("Digite a categoria: "))
viajantes = int(input("Digite a quantidade de viajantes: "))
valorbruto = float(input("Digite o valor bruto: "))

if categoria == "Economica":
    if viajantes == 2:
        print("O valor bruto da sua viagem é: R${:.2f}".format(valorbruto))
        valordodesconto = float(valorbruto) * 0.03
        print("O valor do desconto que será aplicado é de: R${:.2f}".format(valordodesconto))
        valorliquido = float(valorbruto - valordodesconto)
        print("O valor líquido da viagem será: R${:.2f}".format(valorliquido))
        valormedio = valorliquido/viajantes
        print("O valor médio por viajante é de: R${:.2f}".format(valormedio))

    elif viajantes == 3:
            print("O valor bruto da sua viagem é: R${:.2f}".format(valorbruto))
            valordodesconto = float(valorbruto) * 0.04
            print("O valor do desconto que será aplicado é de: R${:.2f}".format(valordodesconto))
            valorliquido = float(valorbruto - valordodesconto)
            print("O valor líquido da viagem será: R${:.2f}".format(valorliquido))
            valormedio = valorliquido/viajantes
            print("O valor médio por viajante é de: R${:.2f}".format(valormedio))

    elif viajantes >= 4:
            print("O valor bruto da sua viagem é: R${:.2f}".format(valorbruto))
            valordodesconto = float(valorbruto) * 0.05
            print("O valor do desconto que será aplicado é de: R${:.2f}".format(valordodesconto))
            valorliquido = float(valorbruto - valordodesconto)
            print("O valor líquido da viagem será: R${:.2f}".format(valorliquido))
            valormedio = valorliquido/viajantes
            print("O valor médio por viajante é de: R${:.2f}".format(valormedio))     

if categoria == "Executiva":
    if viajantes == 2:
        print("O valor bruto da sua viagem é: R${:.2f}".format(valorbruto))
        valordodesconto = float(valorbruto) * 0.05
        print("O valor do desconto que será aplicado é de: R${:.2f}".format(valordodesconto))
        valorliquido = float(valorbruto - valordodesconto)
        print("O valor líquido da viagem será: R${:.2f}".format(valorliquido))
        valormedio = valorliquido/viajantes
        print("O valor médio por viajante é de: R${:.2f}".format(valormedio))

    elif viajantes == 3:
            print("O valor bruto da sua viagem é: R${:.2f}".format(valorbruto))
            valordodesconto = float(valorbruto) * 0.07
            print("O valor do desconto que será aplicado é de: R${:.2f}".format(valordodesconto))
            valorliquido = float(valorbruto - valordodesconto)
            print("O valor líquido da viagem será: R${:.2f}".format(valorliquido))
            valormedio = valorliquido/viajantes
            print("O valor médio por viajante é de: R${:.2f}".format(valormedio))

    elif viajantes >= 4:
            print("O valor bruto da sua viagem é: R${:.2f}".format(valorbruto))
            valordodesconto = float(valorbruto) * 0.08
            print("O valor do desconto que será aplicado é de: R${:.2f}".format(valordodesconto))
            valorliquido = float(valorbruto - valordodesconto)
            print("O valor líquido da viagem será: R${:.2f}".format(valorliquido))
            valormedio = valorliquido/viajantes
            print("O valor médio por viajante é de: R${:.2f}".format(valormedio))     

if categoria == "Primeira classe":
    if viajantes == 2:
        print("O valor bruto da sua viagem é: R${:.2f}".format(valorbruto))
        valordodesconto = float(valorbruto) * 0.10
        print("O valor do desconto que será aplicado é de: R${:.2f}".format(valordodesconto))
        valorliquido = float(valorbruto - valordodesconto)
        print("O valor líquido da viagem será: R${:.2f}".format(valorliquido))
        valormedio = valorliquido/viajantes
        print("O valor médio por viajante é de: R${:.2f}".format(valormedio))

    elif viajantes == 3:
            print("O valor bruto da sua viagem é: R${:.2f}".format(valorbruto))
            valordodesconto = float(valorbruto) * 0.15
            print("O valor do desconto que será aplicado é de: R${:.2f}".format(valordodesconto))
            valorliquido = float(valorbruto - valordodesconto)
            print("O valor líquido da viagem será: R${:.2f}".format(valorliquido))
            valormedio = valorliquido/viajantes
            print("O valor médio por viajante é de: R${:.2f}".format(valormedio))

    elif viajantes >= 4:
            print("O valor bruto da sua viagem é: R${:.2f}".format(valorbruto))
            valordodesconto = float(valorbruto) * 0.20
            print("O valor do desconto que será aplicado é de: R${:.2f}".format(valordodesconto))
            valorliquido = float(valorbruto - valordodesconto)
            print("O valor líquido da viagem será: R${:.2f}".format(valorliquido))
            valormedio = valorliquido/viajantes
            print("O valor médio por viajante é de: R${:.2f}".format(valormedio))     
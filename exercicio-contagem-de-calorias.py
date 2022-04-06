#Define a quantidade de alimentos que devera ser contada no for

alimentos = int(input("Insira quantos alimentos você consumiu no dia de hoje: "))

#O Valor inicial do total de calorias
calorias_total = 0

for x in range (0, alimentos):
    #Enquanto alimentos for diferente de 0 continuara nesse loop.
    while (alimentos != 0):
        #Imprime a quantidade de alimentos que restam ser digitados a quantidade de caloria
        print(f"Alimento: {alimentos}")
        if alimentos !=0:
            calorias_atual = int(input(f"Digite a quantidade de calorias do alimento: "))
            calorias_total = calorias_total + calorias_atual
            alimentos = alimentos -1
print(f"O total de calorias foi de: {calorias_total}")            
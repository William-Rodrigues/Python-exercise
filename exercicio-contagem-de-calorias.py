"""Enunciado: Você deve elaborar um algoritmo implementado em Python em que o usuário informe quantos alimentos consumiu 
naquele dia e depois possa informar o número de calorias de cada um dos alimentos. 
Como não estudamos listas neste capítulo, você não deve se preocupar em armazenar todas as calorias digitadas, 
mas deve exibir o total de calorias no final."""

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
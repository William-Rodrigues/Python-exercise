"""Enunciado: Hora de decidir! Os colaboradores da sua equipe foram sorteados para ganhar um console de última geração,
cada um, em razão do bom desempenho que tiveram nos últimos projetos. Por uma questão de logística, porém, a empresa pede que
todos os cinco membros da equipe recebam o mesmo aparelho. Crie um algoritmo onde o usuário possa digitar o voto de cada um
dos 5 membros da equipe e, ao final, exiba qual foi o console escolhido e com quantos votos. 
As opções são: PLAYSTATION, XBOX e NINTENDO."""

print("A empresa pediu para que vocês 5 votem qual console vocês desejam ganhar, o mais votado será o que todos vão receber.")
print("As Opções de console são: Playstation, Xbox e Nintendo. Por favor escreva o nome conforme foi exibido nesta frase. ")

# Recebendo os votos #

Funcionario1 = input("Funcionário 1 Digite qual console você gostaria de receber: ")
Funcionario2 = input("Funcionário 2 Digita qual console você gostaria de receber: ")
Funcionario3 = input("Funcionário 3 Digita qual console você gostaria de receber: ")
Funcionario4 = input("Funcionário 4 Digita qual console você gostaria de receber: ")
Funcionario5 = input("Funcionário 5 Digita qual console você gostaria de receber: ")
Consoles = Funcionario1, Funcionario2, Funcionario3, Funcionario4, Funcionario5

# Contagem dos votos #

Total_de_votos_Playstation = Consoles.count('Playstation')
Total_de_votos_Xbox = Consoles.count('Xbox')
Total_de_votos_Nintendo = Consoles.count('Nintendo')

# Impressao da quantidade de funcionários que gostariam de receber tal console. #

print(f"A quantidade de funcionários que gostariam de receber um Playstation é de: {Total_de_votos_Playstation}")
print(f"A quantidade de funcionários que gostariam de receber um Xbox é de: {Total_de_votos_Xbox}")
print(f"A quantidade de funcionários que gostariam de receber um Nintendo é de: {Total_de_votos_Nintendo}")

# Contagem de votos Playstation #

if Total_de_votos_Playstation == Total_de_votos_Nintendo:
    print("Houve um empate entre Playstation e Nintendo, será feita outra votação considerando apenas Playstation e Nintendo para realizarmos o desempate.")

if Total_de_votos_Playstation == Total_de_votos_Xbox:
    print("Houve um empate entre Playstation e Xbox, será feita outra votação considerando apenas Playstation e Xbox para realizarmos o desempate.")

if Total_de_votos_Playstation > Total_de_votos_Nintendo:
    print("O Console que todos irão receber será o Playstation")

if Total_de_votos_Playstation > Total_de_votos_Xbox:
    print("O Console que todos irão receber será o Playstation")

# Contagem de Votos Xbox #

if Total_de_votos_Xbox == Total_de_votos_Nintendo:
    print("Houve um empate entre Xbox e Nintendo, será feita outra votação considerando apenas Playstation e Nintendo para realizarmos o desempate.")

if Total_de_votos_Xbox == Total_de_votos_Playstation:
    print("Houve um empate entre Playstation e Xbox, será feita outra votação considerando apenas Playstation e Xbox para realizarmos o desempate.")

if Total_de_votos_Xbox > Total_de_votos_Nintendo:
    print("O Console que todos irão receber será o Xbox")

if Total_de_votos_Xbox > Total_de_votos_Playstation:
    print("O Console que todos irão receber será o Xbox")

 # Contagem de Votos Nintendo #
if Total_de_votos_Nintendo == Total_de_votos_Nintendo:
    print("Houve um empate entre Nintendo e Playstation, será feita outra votação considerando apenas Playstation e Nintendo para realizarmos o desempate.")

if Total_de_votos_Nintendo == Total_de_votos_Playstation:
    print("Houve um empate entre Nintendo e Playstation, será feita outra votação considerando apenas Playstation e Xbox para realizarmos o desempate.")

if Total_de_votos_Nintendo > Total_de_votos_Nintendo:
    print("O Console que todos irão receber será o Nintendo")

if Total_de_votos_Nintendo > Total_de_votos_Playstation:
    print("O Console que todos irão receber será o Nintendo")        
"""Enunciado: Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives. 
Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana
(segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido."""

#Recebe a quantidade de pessoas que votaram em cada dia da semana
Segunda = int(input("Informe a quantidade de pessoas que votaram na segunda-feira: "))
Terca = int(input("Informe a quantidade de pessoas que votaram na terça-feira: "))
Quarta = int(input("Informe a quantidade de pessoas que votaram na quarta-feira: "))
Quinta = int(input("Informe a quantidade de pessoas que votaram na quinta-feira: "))
Sexta = int(input("Informe a quantidade de pessoas que votaram na sexta-feira: "))

if Segunda > Terca and Segunda > Quarta and Segunda > Quinta and Segunda > Sexta:
    print("O dia escolhido para realização das lives foi Segunda-feira")

if Terca > Segunda and Terca > Quarta and Terca > Quinta and Terca > Sexta:
    print("O dia escolhido para realização das lives foi Terça-feira")
    
if Quarta > Segunda and Quarta > Terca and Quarta > Quinta and Quarta > Sexta:
    print("O dia escolhido para realização das lives foi Quarta-feira")

if Quinta > Segunda and Quinta > Terca and Quinta > Quarta and Quinta > Sexta:
    print("O dia escolhido para realização das lives foi Quinta-feira")
    
if Sexta > Segunda and Sexta > Terca and Sexta > Quarta and Sexta > Quinta:
    print("O dia escolhido para realização das lives foi Sexta-feira")
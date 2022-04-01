from timeit import repeat


bpm = int(input("Digite os batimentos: "))
idade = int(input("Digite a idade: "))


if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Os batimentos do bebê estão dentro da normalidade: {}".format(bpm))
    elif bpm >140:
        print("Os batimentos do bebê estão acima da normalidade: {}".format(bpm))
    elif bpm <120:
        print("Os batimentos do bebê estão abaixo da normalidade: {}".format(bpm))
        
elif idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print("Os batimentos do adolescente estão dentro da normalidade: {}".format(bpm))
    elif bpm > 100:
        print("Os batimentos do adolescente estão acima da normalidade: {}".format(bpm))
    elif bpm <80:
        print("Os batimentos do adolescente estão abaixo da normalidade: {}".format(bpm))

elif idade >= 18 and idade <= 59:
    if bpm >= 70 and bpm <= 80:
        print("Os batimentos do adulto estão dentro da normalidade: {}".format(bpm))
    elif bpm > 80:
        print("Os batimentos do adulto  estão acima da normalidade: {}".format(bpm))
    elif bpm <70:
        print("Os batimentos do adulto  estão abaixo da normalidade: {}".format(bpm))

elif idade >= 60:
    if bpm >= 50 and bpm <= 60:
        print("Os batimentos do idoso  estão dentro da normalidade: {}".format(bpm))
    elif bpm > 60:
        print("Os batimentos do idoso estão acima da normalidade: {}".format(bpm))
    elif bpm <50:
        print("Os batimentos do idoso estão abaixo da normalidade: {}".format(bpm))
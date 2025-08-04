import random

dezenas = []



def preencherDezena():

    while len(dezenas) < 6:
        entrada = int(input("Digite uma dezena: "))

        if entrada < 1 or entrada > 60:
            print("Número inválido! Digite novamente ")

        else:
            dezenas.append(entrada)
    dezenas.sort()


    print("Obrigado! Seu jogo foi registrado e preenchido.")
    print(f"Jogo registrado: {dezenas}")
    return(dezenas)

def sorteio(jogo):
    acertos = 0


    for i in range(6):
        sorteado = random.sample(range(1,61),6)
        print(f"{(i+1)}° -  {sorteado}")


        for i in range(len(jogo)):

            if jogo[i] == sorteado:
                acertos =+ 1

    print(f"Você acertou {acertos} de {len(jogo)}.")

#Sistema

jogo = preencherDezena()

if len(jogo) == 6:
    sorteio(jogo)

#Exercício 2 - Jogo de Dados

print(" JOGO DE DADOS ")
print("Vamos sortear dois dados e somar seus valores!")
print("-------------------------------")
num = int(input("Digite o valor da soma: "))
soma = 0

match num:
    case 2 | 12:
      print(f"A probabilidade de acerto é {(1 / 36) * 100:.2f}%")
    case 3 | 10:
        print(f"A probabilidade de acerto é {(2 / 36) * 100:.2f}%")
    case 4 | 10:
        print(f"A probabilidade de acerto é {(3 / 36) * 100:.2f}%")
    case 5 | 9:
        print(f"A probabilidade de acerto é {(4 / 36) * 100:.2f}%")
    case 6 | 8:
        print(f"A probabilidade de acerto é {(5 / 36) * 100:.2f}%")
    case 7:
        print(f"A probabilidade de acerto é {(6 / 36) * 100:.2f}%")

for i in range(2):
    sorteio1 = random.randint(1,6)
    sorteio2 = random.randint(1,6)
    soma = sorteio1 + sorteio2

if soma == num:
    print(f"Parabéns! Você acertou o valor da soma dos sorteios {soma}.")
else:
    print(f"Que pena! Não foi dessa vez, o resultado da soma dos sorteios é {soma}.")

dois = 0
tres = 0
quatro = 0
cinco = 0
seis = 0
sete = 0
oito = 0
nove = 0
dez = 0
onze = 0
doze = 0

print("Extra")
for i in range(40):
    sorteio1 = random.randint(1,6)
    sorteio2 = random.randint(1,6)
    soma = sorteio1 + sorteio2
    print(soma)

    match soma:
        case 2:
            dois += 1
        case 3:
            tres += 1
        case 4:
            quatro += 1
        case 5:
            cinco += 1
        case 6:
            seis += 1
        case 7:
            sete += 1
        case 8:
            oito += 1
        case 9:
            nove += 1
        case 10:
            dez += 1
        case 11:
            onze += 1
        case 12:
            doze += 1













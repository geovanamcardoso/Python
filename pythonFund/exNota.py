print("CADASTRO DE ALUNO")
print("--------------------------------------")
nomeCad = input("Informe seu nome: ")
rmCad = input("Informe seu RM (apenas números): ")
senhaCad = input("Cadastre sua senha : ")
print("----------------------------------------")
print("ACESSO AO BOLETIM ")
print("----------------------------------------")

tentativa = 0
for cont in range(0,3):
    senha = input("Informe sua senha cadastrada: ")
    if senha == senhaCad:
        break
    else:
        print("Senha incorreta!")
        tentativa += 1
        if tentativa == 3:
            print("Senha incorreta 3 vezes consecutivas. Realize seu cadastro novamente!")
cp1 = 0
cp1 = float(input("Informe a nota do seu 1° CP (0 a 10): "))

while cp1 > 10 or cp1 < 0:
    cp1 = float(input("Nota inválida. Digite sua nota (CP 1) de 0 a 10: "))

cp2 = float(input("Informe a nota do seu 2° CP (0 a 10): "))
while cp2 > 10 or cp2 < 0:
    cp2 = float(input("Nota inválida. Digite sua nota (CP 2) de 0 a 10: "))

cp3 = float(input("Informe a nota do seu 3° CP (0 a 10): "))
while cp3 > 10 or cp3 < 0:
    cp3 = float(input("Nota inválida. Digite sua nota (CP 3) de 0 a 10: "))

mediacp = 0
if cp1 < cp2 and cp1 < cp3:
    mediacp = (cp2 + cp3)/2
elif cp2 < cp1 and cp2 < cp3:
    mediacp = (cp1 + cp3)/2
elif cp3 < cp1 and cp3 < cp2:
    mediacp = (cp1 + cp2)/2

sprint1 = float(input("Informe a nota do seu 1° Sprint (0 a 10): "))
while sprint1 > 10 or sprint1 < 0:
    sprint1 = float(input("Nota inválida. Digite sua nota (Sprint 1) de 0 a 10: "))

sprint2 = float(input("Informe a nota do seu 2° Sprint (0 a 10): "))
while sprint1 > 10 or sprint1 < 0:
    sprint1 = float(input("Nota inválida. Digite sua nota (Sprint 2) de 0 a 10: "))

sprints = sprint1 + sprint2/2

peso_cp = 0.2
peso_spr = 0.2
peso_gs = 0.6

mediaParc = mediacp * peso_cp + sprints * peso_spr

gs = (6.0 - mediaParc)/peso_gs


print(f"Você precisa tirar, no mínimo, {gs} na GS para ser aprovado!")






















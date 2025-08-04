'''While => serve para situações em que não sabemos quantas repetições são
necessárias;

For => serve para situações em que sabemos quantas vezes a estrutura precisa ser repetida;

Função => conjunto de instruções que pode ser utilizado em diferentes ocasiões

Parâmetro/Argumento => valores/informações que a função precisa

range(start, stop, step)
imprime o start, o stop não
stop - parar quando o valor for esse
i = index
só aceita números inteiros como parâmetro


array unidimensional = vetor
array bidimensional = matriz (tabela)

for var in range(start, stop, step)

break => interrompe o loop caso uma condição seja satisfeita

continue => se a condição for satisfeita, ele ignora as instruções e passa para o próximo loop

for tbm consegue varrer string, string é um vetor de caracteres
cont = 0
texto = "Texto simples"
ex: for caractere in texto:
        cont += 1


par = 0

for cont in range(1,11):
    num = int(input(f"Digite o {cont}° número: "))
    if num % 2 == 0:
       par += 1
print(f"Você digitou {par} números pares!")


num1 = 0

while num1 <= 0 or num1 > 10:
    num1 = int(input("Digite um número de 1 a 10: "))

for cont in range(1,11):
    print(cont)
    if cont == num1:
        break
print(f"O número escolhido foi {cont}")


for cont in range(10):
    if cont % 3 == 0:
        continue
    print(cont)


cont = 0
texto = "Esse é um texto exemplo"
for caractere in texto:
        cont += 1
print(cont)
'''














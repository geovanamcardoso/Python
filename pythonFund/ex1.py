def soma(num):
    if num == 1:
        return 1
    else:
        return num + soma(num - 1)

somaIn = soma(int(input("Digite um número: ")))

print(somaIn)
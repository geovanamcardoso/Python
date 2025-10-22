def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, (expoente - 1))
    # 4 ^ 4
    #4 * potencia(4, 3)
    # 4 * potencia(4, 2)...

a = int(input("Digite a base: "))
b = int(input("Digite o expoente: "))
print(potencia(a,b))
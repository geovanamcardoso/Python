def mdc(a, b):
    if a >= b and a % b == 0: #Se 'A' for maior ou igual a B e se 'A' for divisível por B
        return b #Retorna o mesmo número B, pois é o maior número que ele é divisível e o A também é divísivel

    elif a < b: #Se 'A' for menor, refaz a função com os números trocados e cai no primeiro IF
        return mdc(b,a)
    else: # ????
        return mdc(b, a % b)

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print(mdc(a,b))
'''Recursividade: Resolver um problema complexo com função chamando função até chegar na solução (problema mínimo) '''

"""
somatório de todos os números inteiros no intervalo de 1 a N

n = 5
somatorio = 5+4+3+2+1

somatorio(5) = 5 + somatorio(4)
somatorio(4) = 4 + somatorio(3)
somatorio(3) = 3 + somatorio(2)
somatorio(2) = 2 + somatorio(1)
somatorio(1) = 1
"""

def somatorio(n):
    if n == 1:
        return 1
    else:
        return n + somatorio(n-1)

n = int(input('Numero: '))
print(somatorio(n))
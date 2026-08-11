def fatorial_it(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(fatorial_it(10))
'''%time fatorial_it(1500)
CPU times: total: 0 ns
Wall time: 363 μs'''


def fatorial(n):
    # Caso base / condição de parada
    if n == 0:
        return 1

    # Passo recursivo
    return n * fatorial(n - 1)

print(fatorial(10))
'''%time fatorial(1500)
CPU times: total: 0 ns
Wall time: 497 μs'''

def potencia(base, expoente):
    # Caso base / condição de parada
    if expoente == 0:
        return 1
    # Passo recursivo
    return base * (potencia(base, expoente - 1))

print(potencia(3,5))

#Fibonacci
def fib_it(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
        return b

print(fib_it(6))

def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

#Inverter string

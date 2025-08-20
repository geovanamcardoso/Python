'''Boas práticas de desenvolvimento em Python

Type hint -> Escrever o tipo da variável (interpretador não lê) -> nome_var : tipo
função = def nome_fun (arg1 : tipo, arg2 : tipo) -> tipo_retorno (pode ser None:)

Docstring são as três aspas para criar comentários de mais de 1 linha


nome : str = "Fábio"
idade: int = 30
salario : float = 3000.00

def exibir_dados(nome: str, idade: int, salario: float) -> None:
    print(f"Nome: {nome}, Idade: {idade}, Salário: R${salario}")

exibir_dados(nome,idade,salario)
'''

#Exercício 1
def somar(val1: int, val2:int) -> int:
    '''A função 'somar' recebe dois valores e retorna a soma deles'''
    return val1 + val2

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro valor: '))
print(f'A soma dos valores {num1} e {num2} é {somar(num1,num2)}.')

#Exercício 2
def quadrado(val1: int) -> int:
    '''A função 'quadrado' recebe um valor e retorna o quadrado desse número '''
    return(val1**2)

print(f'O quadrado do número {num1} é {quadrado(num1)}.')

#Exercício 3
def soma_dos_quadrados(val1: int, val2: int) -> int:
    '''A função 'soma_dos_quadrados' recebe dois valores e retorna a soma dos quadrados desses
    valores'''
    return (val1**2) + (val2**2)

print(f'A soma dos quadrados do números {num1} e {num2} é {soma_dos_quadrados(num1,num2)}.')

#Exercício 4
def media(val1: int, val2: int, val3: int) -> float:
    '''A função 'media' recebe 3 valores e retorna a média aritmética desses valores'''
    return( (val1+val2+val3)/3 )

num3 = int(input("Digite o terceiro valor: "))
print(f'A média aritmética dos valores {num1}, {num2} e {num3} é {media(num1,num2,num3):.2f}.')

#Exercício 5
def calcular_salario(salario: float) -> float:
    '''A função 'calcular_salario' recebe o salário atual de um funcionário e retorna o
novo salário com reajuste de aumento. Se o salário seja maior que 2000, a aumento será
de 7%, caso contrário, será de 15%'''
    if(salario > 2000):
        aumento: float = 0.07
    else:
        aumento: float = 0.15

    return(salario + (salario*aumento))

salAtual = float(input("Insira seu salário atual (R$): "))
print(f'Seu salário atual é R${salAtual}. Seu novo salário é R${calcular_salario(salAtual):.2f}')

#Exercício 6
def soma_divisores(val1: int) -> int:
    '''A função 'soma_divisores' recebe um valor inteiro positivo e retorna a soma de todos os divisores desse número.'''
    divisor : int = 1
    soma: int = 0

    while divisor <= val1:
        if (val1 % divisor == 0):
            soma += divisor
        divisor += 1
    return(soma)

print(f'A soma dos divisores do número {num1} é igual a {soma_divisores(num1)}.')







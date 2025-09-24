def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Erro de divisão por zero.')

while True:
    try:
        print('1 - Soma')
        print('2 - Subtração')
        print('3 - Divisão')
        opcao = int(input('Escolha uma opção: '))

        if opcao < 1 or opcao > 3:
            raise TypeError
    except TypeError:
        print("Opção inválida! Insira um valor de 1 a 3!")
        
    except ValueError:
        print('O valor informado deve ser inteiro')
    else:
        try:
            a = int(input('Primeiro numero: '))
            b = int(input('Segundo numero: '))
        except ValueError:
            print('Os numeros informados devem ser inteiro')
        else:
            match opcao:
                case 1:
                    print(somar(a, b))
                case 2:
                    print(subtrair(a, b))
                case 3:
                   print(dividir(a, b))
                case _:
                    print('Opção inválida')
            break


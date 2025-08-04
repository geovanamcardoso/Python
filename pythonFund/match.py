'''
letra = input("Digite uma letra: ")
match letra:
    case "a" | "e" | "i" | "o" | "u":
        print(f"A letra {letra} é uma vogal!")
    case _:
        print(f"A letra {letra} é uma consoante!")
'''

print("Calculadora")
print("1. Soma\n 2.Subtração\n 3.Multiplicação\n 4.Divisão\n")
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
op = int(input("Digite o número correspondente a operação: "))
match op:
    case 1:
        print(f"{num1} + {num2} = {(num1 + num2):.2f}")
    case 2:
        print(f"{num1} - {num2} = {(num1 - num2):2f}")
    case 3 :
        print(f"{num1} x {num2} = {(num1 * num2):.2f}")
    case 4:
        if num2 == 0:
            print("O segundo número é inválido para essa operação!")
        else:
            print(f"{num1} / {num2} = {(num1 / num2):.2f}")
    case _:
        print("Número inserido inválido!")


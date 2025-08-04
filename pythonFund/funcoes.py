'''
Função: bloco/conjunto de comandos que realiza uma função específica da solução

parâmetro: dados de entrada para a função funcionar

Toda função que tiver retorno, deve ter o retorno armazenado ou imprimir direto

o retorno pode ser uma bool, str, int, etc.
passagem de parâmetro por valor: tenho uma cópia do valor, parâmetro tbm, endereços diferentes com
o valor passado

passagem de parâmetro  por referência: parâmetro recebe o endereço de memória da variável, acompanha
alterações

definir funções no começo
quando printar a função não precisa chamar ela
mais de um parâmetro é separado por vírgula


def par_ou_impar():
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        return ("Par")
    else:
        return ("Ímpar")

print(f"O número digitado é {par_ou_impar()}!")


raio = float(input("Informe o raio do círculo (cm): "))

def area(r):
    area = (r**2) * 3.14
    return area

def perimetro(r):
    perimetro = 3.14 * r * 2
    return perimetro

print(f" A área do círculo é {area(raio):.2f} cm² e o perímetro é {perimetro(raio):.2f} cm!")
'''

vinhos = ['Luara Tempranillo' , 2]
def boas_vindas():
    print("---------------------")
    print("Bem-vindo à Vinheira Agnello!")
    print("-------------------------------")

def escolha():
    escolha = int(input("Você deseja cadastrar vinhos?\n 1.Cadastrar \n 2.Sair \n"))

    if escolha != 1 and escolha != 2:
        print("Resposta inválida!")
    return escolha

def cad_vinho():

    cad = input("Informe o nome do vinho: ")
    vinhos.append(cad)
    quant = int(input("Informe a quantidade desse vinho: "))
    vinhos.append(quant)

def exibir_menu():
    print("Vinhos cadastrados e suas quantidades: \n")

    for i in range(len(vinhos)):
        if i % 2 == 0:
            print(vinhos[i], " | " ,vinhos[(i+1)])


boas_vindas()
resp = escolha()

while resp == 1:
    cad_vinho()
    resp = escolha()

exibir_menu()



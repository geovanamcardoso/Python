'''Matriz -> m,n -> linhas por colunas, é um vetor bidimensional
Em python, matriz é uma lista de listas. É uma tabela horizontal: cada posição (linhas)
tem uma lista dentro (com colunas dentro -> elementos)
Não criar a posição na lista dá erro sistêmico, temos que criar a posição (com append) e preenchê-lo
com null
len retorna o número de linhas (listas) da matriz, para as colunas, precisamos informar o índice
da linha
Criar uma lista matriz (tabela) vazia, criar outra lista (linha) vazia e preenchê-la de acordo com numero de
colunas. Adicionar essa lista completa (linha) na matriz. Repetir o processo de acordo com numero de
linhas.
Percorrer matriz: for linha in matriz: print(linha)
Percorrer itens na matriz -> for linha in matriz: for item in linha: print(item)

Create (inserção), Read (Leitura), Update (Edições), Delete (Exclusão)

Percorrer matriz existente:
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
    print(matriz[linha][coluna])

Formato tabela:
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        print(matriz[linha][coluna], end="\t")
    print()

end é um parâmetro do print, \t = tab
'''

#Preencher matriz 3x5 com números inteiros inseridos pelo usuário e exibi-lá
'''
matriz = []

for linhas in range(3):
    linha = []
    for colunas in range(5):
        num = int(input("Insira um número inteiro: "))
        linha.append(num)
    matriz.append(linha)

print(matriz)
'''
#Pedir 12 valores e armazenar em uma matriz 3x4 e exibi-la. Depois, trocar todos maiores que 100 por 0 e exibir.
'''
matriz = []

for linhas in range(3):
    linha = []
    for colunas in range(4):
        num = int(input("Insira um número inteiro: "))
        linha.append(num)
    matriz.append(linha)
print(matriz)

for l in range(len(matriz)):
    for c in range(len(matriz[0])):
        if matriz[l][c] > 100:
            matriz[l][c] = 0
print(matriz)
'''

#Preencher matriz 5x5 com números aleatórios e exibir. Mostrar a soma da diagonal.
'''
import random

matriz = []
soma = 0
menor = 0

for linhas in range(5):
    linha = []
    for colunas in range(5):
        num = random.randrange(10)
        linha.append(num)
    matriz.append(linha)

for l in range(len(matriz)):
    for c in range(len(matriz[0])):

        if matriz[l][c] < menor:
            menor = matriz[l][c]

        print(matriz[l][c], end="\t")
    print()


for l in range(len(matriz)):
    for c in range(len(matriz[0])):
        if (l == 0 and c == 0) or (l == 1 and c == 1) or (l == 2 and c == 2) or (l == 3 and c == 3) or (l == 4 and c == 4):
            soma += matriz[l][c]

print(f"A soma da diagonal é {soma}!")
print(f"O menor número é {menor}!")
'''

#Matriz 5x4 por usuário; exibir; solicitar número e buscar por ele na matriz e guardar a posição dele; Guardar todas as posições que ele foi encontrado.

matriz = []

for linhas in range(5):
    linha = []
    for colunas in range(4):
        num = int(input("Insira um número: "))
        linha.append(num)
    matriz.append(linha)

for l in range(len(matriz)):
    for c in range(len(matriz[0])):
        print(matriz[l][c], end="\t")
    print()

numEsc = int(input("Escolha um número para encontrar na matriz: "))
vezes = 0


#ÍMPAR = COLUNA \ PAR = ÍMPAR
print(f"O número {numEsc} foi encontrado nas posições: ")

for l in range(len(matriz)):
    for c in range(len(matriz[0])):
        if matriz[l][c] == numEsc:
            vezes += 1
            print(f"[{l}],[{c}]; ")

print()
print(f"O número {numEsc} foi encontrado {vezes} vezes.")













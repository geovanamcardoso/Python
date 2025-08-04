'''
Endereço do vetor = index (índice de identificação)

Na memória, os espaços do vetor não ficam um ao lado do outro, são criados espaços em lugares
aleatórios, com endereço de memória diferente.
Um setor da memória não cabe todas as casas do vetor.
A memória encontra as casas por meio de ponteiros**

Vetor estático = declaro o n° de casas
Dinâmico = casas são adicionadas conforme a necessidade, são vetores encadeados

Listas são vetores dinâmicos
cada espaço com valor é um item

Lista vazia é só uma representação lógica, não cria espaço na memória

Tudo que é digitado dentro dos parênteses de uma função é parâmetro/argumento

append não sobrescreve, só adiciona
pop vazio apaga o último valor/espaço
len retorna o tamanho, seu valor deve ser armazenado em uma variável, não existe o index len, só
len - 1
insert cria um espaço entre os espaços da lista, insert(index, item), coloca um item no meio da
lista, os outros são empurrados
remove tira a primeira ocorrência de um item
para remover todos = while item in lista


num = [2,0,4,18,13]
soma = 0

for i in range(len(num)):
    soma += num[i]

if (len(num) != 0):
 media = soma/(len(num))
 print(f"A média do aluno é {media}")

n = 0
n2 = 0

for i in range(len(num)):
    if num[i] > n:
        n = num[i]

    if num[i] <= n2:
        n2 = num[i]

print(f"O maior número é {n} e o menor número é {n2}!")

for i in range(len(num) - 1): #Pega o último da lista
    for y in range(len(num) - 1 - i):
        if num[y] > num[y + 1]:
            n = num[y]
            num[y] = num[y + 1]
            num[y + 1] = n

print(num)'''

num = [2,0,4,18,13]
minimo = min(num)

maximoImpar = 0
ParMinimo = 0

if minimo % 2 == 0:
    ParMinimo = minimo


maximo = max(num)

if maximo :
    maximoImpar = maximo

print(f"{maximoImpar} é o maior valor ímpar e {ParMinimo} é o menor número par!")














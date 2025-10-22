'''def busca(lista, item):
    if item in lista:
        return True
    else:
        return False

listaNum = [0,1,2,3]
a = int(input("Digite um número: "))
buscaRes = busca(listaNum,a)

if not(buscaRes):
    print("Número não encontrado!")
else:
    print("Número encontrado!")'''

def busca(lista, item):
    if len(lista) == 0:
        return False
    if lista[0] == item:
        return True
    else:
        return busca(lista[1:], item)

listaNum = [0,1,2,3]
print(busca(listaNum,3))


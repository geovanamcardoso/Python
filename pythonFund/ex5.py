'''def contagem(lista, num):
    if len(lista) == 0:
        return ("Essa lista está vazia!")
    else:
        return lista.count(num)

listaNum = [0,1,2,3,3,3]

print(contagem(listaNum, 3))'''

def contagem(lista, num):
    if len(lista) == 0:
        return 0
    if lista[0] == num:
        return 1 + contagem(lista[1:], num)
    else:
        return contagem(lista[1:], num)

listaNum = [0,1,2,3,3,3]
print(contagem(listaNum, 3))
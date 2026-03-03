# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Ordenação Ex.1
lista = [5, 2, 1, 7, 6]
lista.sort()
print(lista)

#Ex.2
lista.sort(reverse=True)
print(lista)

#Ex.3
lista = [5, 2, 1, 7, 6]
lista_ordenada = sorted(lista)
print(lista_ordenada)

#Ex.4
lista = [5, 2, 1, 7, 6]
lista_ordenada = sorted(lista, reverse=True)
print(lista_ordenada)

#Ex.5
lista1 = [('maça', 3), ('banana', 1), ('laranja', 2)]
lista_ordenada = sorted(lista1, key=lambda x: x[1]) #está ordenando pelo segundo valor da tupla (index =1)
print(lista_ordenada)

#ALGORITMO DE BUSCA BINÁRIA
def busca_binaria(lista, alvo):
    
    l = 0
    h = len(lista) - 1
    iteracao = 0
     
    while l <= h:
        
        iteracao += 1
        m = (l + h) // 2
        
        print(f'Iteração {iteracao} : l{l}, h{h}, m{m}')
        
        if lista[m] == alvo:
            return m
        elif lista[m] < alvo:
            l = m + 1
        else:
            h = m - 1
            
    return -100         

lista1 = [11, 17, 18, 45, 50, 71, 95]
target = 50

resultado = (busca_binaria(lista1, target))
print(f"Indíce do alvo: {resultado}")
             
#Tentativa de resposta
 '''
 #lista.sort()
 while(lista[m] != alvo):
     
     if(lista[m] < alvo):
         l = m + 1
         m = (l + h) // 2
         iteracao += 1
         
     elif(lista[m] > alvo):
         h = m - 1
         m = (l + h) // 2
         iteracao += 1
     else:
         break
 return'''

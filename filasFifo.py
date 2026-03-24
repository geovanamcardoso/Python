# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# Ex.1 
print(" -- EXERCÍCIO 1 --")
fila = ['cliente1', 'cliente2','cliente3', 'cliente4','cliente5']
print(fila)

print(fila[0])
print(fila[1])
print(fila[2])
print(fila[3])
print(fila[4])

cliente = fila.pop(0)
print(cliente)
print(fila)

#---------------------------

#Ex.2 - Estrutura de repetição
print(" -- EXERCÍCIO 2 --")

fila = ['cliente1', 'cliente2','cliente3', 'cliente4','cliente5']

while fila:
    cliente = fila.pop(0)
    print(f"Atendendo {cliente}")
    
#Ex. 3 - Loja de atendimento

print(" -- EXERCÍCIO 3 --")

fila = []
    
while True:
    cliente = input('Digite o nome do cliente ou fim para a estrutura:')
        
    if cliente == 'fim':
         break
    fila.append(cliente)
     
print(f'Fila atual: {fila}')

while fila:
    cliente = fila.pop(0)
    print(f"Atendendo {cliente}!")
    
print("Todos foram atendidos!")    

#Ex. 4 - Algortimo para adicionar e remover cliente em uma fila FIFO

fila = []

while True:
    print(' -- SISTEMA DE ATENDIMENTO -- ')
    
    print('1 - Adicionar cliente')
    print('2 - Atender cliente')
    print('3 - Mostrar fila')
    print('4 - Sair')
    
    
    opcao = input("Digite a ação que deseja realizar:")
    match opcao:
        case '1':
            cliente = input("Digite o nome do cliente:")
            fila.append(cliente)
        case '2': 
            if fila:
                cliente = fila.pop(0)
                print(f"Atendendo {cliente}!")
        case '3':
            print(f'Fila atual: {fila}')
        case '4':
            break
        case _:
            print("Número inválido!")
        
                
            

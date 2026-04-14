# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

''' Ex1. Mostre um exemplo de uma estrutura com fila e pilha utilizando estrutura de repetição while
e for para solicitar e atender 8 clientes.

Ex.2 Mostre um exemplo de uma estrutura com fila utilizando estrutura de repetição while e for para 
solicitar nome e idade para 5 clientes. Atenda os clientes por ordem de chegada.

Ex.3 Mostre um exemplo de uma estrutura com fila utilizando estrutura de repetição while ou for para
solicitar nome e idade para 5 clientes. Atenda os clientes por ordem de idade (maior idade
                                                                               maior prioridade, 
                                                                               menor idade, 
                                                                               menor prioridade)
Ex.4 Crie uma estrutura para solicitar 4 informações do cliente (nome, idade, cpf e prioridade)
insira estas sublistas em uma lista. Após isso, ordene as sublistas por ordem de prioridade e atenda 
pela ordem de prioridade.

Ex.5 Utilizando a biblioteca heapq, crie um sistema de cadastro de pessoas e carros. Onde 1. cadastrar
2. atender cliente 3. sair da estrutura.
solicite nome, carro, tipo de serviço, prioridade
atender os clientes com prioridade de serviço
sair da estrutura.



Ex1. Mostre um exemplo de uma estrutura com fila e pilha utilizando estrutura de repetição while
e for para solicitar e atender 8 clientes.

lista_cliente = []
i = 0

while i < 8:
    nome =  input("Digite seu nome:")
    lista_cliente.append(nome)
    i += 1
    print(lista_cliente)
    
while lista_cliente:
    cliente = lista_cliente.pop(0)
    print(f"Atendendo cliente {cliente}!")

Ex.2 Mostre um exemplo de uma estrutura com fila utilizando estrutura de repetição while e for para 
solicitar nome e idade para 5 clientes. Atenda os clientes por ordem de chegada.

lista_comp = []

for i in range(5):
    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade:"))

    nome_idade = [nome, idade]
    lista_comp.append(nome_idade)
    print(lista_comp)
    
lista_comp.sort(key = lambda x: -x[1])
print(lista_comp)

lista_ordenada = sorted(lista_comp, key = lambda x: -x[1])
print(lista_ordenada)
    
while lista_ordenada:
    print(f"Atendendo {lista_ordenada[0]}")
    lista_ordenada.pop(0)

print("Todos os clientes foram atendidos!")'''



'''Ex.3 Mostre um exemplo de uma estrutura com fila utilizando estrutura de repetição while ou for para
solicitar nome e idade para 5 clientes. Atenda os clientes por ordem de idade (maior idade
                                                                               maior prioridade, 
                                                                               menor idade, 
                                                                               menor prioridade)'''

fila = []

for i in range(5):
    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade:"))
    
    fila.append((nome,idade))
    fila_org = sorted(fila, key = lambda x: -x[1])
    print("Fila organizada:")
    
while fila_org:
    print(f"Atendendo {fila[0]}")
    fila_org.pop(0)
    
    

'''Ex.4'''

lista_completa = []

for i in range(4):
    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade:"))
    cpf = input("Digite CPF:")
    prioridade = int(input("Digite a prioridade:"))
    
    var_completa = [nome, idade, cpf, prioridade]
    lista_completa.append(var_completa)
    print(lista_completa)

lista_ordenada = sorted(lista_completa, key = lambda x: -x[3])
print(lista_ordenada)
    
while lista_ordenada:
    print(f"Atendendo {lista_ordenada[0]}")
    lista_ordenada.pop(0)


'''Ex.5'''
import heapq


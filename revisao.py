# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


#Exercício 1 - FOR

lista_nome = []
lista_idade = []
lista_nascimento = []

for i in range(5):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    nascimento = input("Digite a sigla do seu estado de nascimento (ex: SP,RJ...)")
    
    lista_nome.append(nome)
    lista_idade.append(idade)
    lista_nascimento.append(nascimento)
    print("-------------------------")
    
for i in range(5):
    print(f"Nome: {lista_nome[i]} ")
    print(f"Idade: {lista_idade[i]} ")
    print(f"Estado: {lista_nascimento[i]}")
    print("-------------------------")
    
#Exercício 1 - While
lista_nome = []
lista_idade = []
lista_nascimento = []
    
while len(lista_nome) < 5:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    nascimento = input("Digite a sigla do seu estado de nascimento (ex: SP,RJ...) :")
        
    lista_nome.append(nome)
    lista_idade.append(idade)
    lista_nascimento.append(nascimento)
    print("-------------------------")
        
i = 0
while i < 5:
    print(f"Nome: {lista_nome[i]} ")
    print(f"Idade: {lista_idade[i]} ")
    print(f"Estado: {lista_nascimento[i]}")
    print("-------------------------")
    i += 1 """
    
    
def busca_linear(lista, alvo):
    
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -100
    
lista = [2, 3, 4, 10, 40]
alvo = 3

resultado = busca_linear(lista, alvo)

if resultado != -100:
    print(f"Elemento encontrado no índice {resultado}")
else:
    print("Elemento não encontrado")

        

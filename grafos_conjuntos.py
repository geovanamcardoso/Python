# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Ex. 1 - Estrutura de árvore binária do ex1 da lousa

vestuario = {
    "categoria_principal": ["eletronicos", "vestuario"],
    "eletronicos": ["celulares", "TVs"],
    "celulares": ["android", "IOS"],
    "android": [],
    "IOS": [],
    "TVs": [],
    "vestuario": ["Masc", "Fem"],
    "Masc": [],
    "Fem": []
    }

print(vestuario)

#-----------------------------------------------------

amizades = {
    "Alice": ["Bob", "Charlie"], 
    "Bob": ["Alice", "Diana"], 
    "Charlie": ["Alice", "Diana"], 
    "Diana": ["Bob", "Charlie", "Eve"], 
    "Eve": ["Diana"], 
    }

print(amizades)

#Operações com conjunto
#Descobrir amigos em comum entre Bob e Charlie
amigos_bob = set(amizades["Bob"]) # -> permite utilizar simbolos e calculos com conjuntos
amigos_charlie = set(amizades["Charlie"])
amigos_comuns = amigos_bob & amigos_charlie
print("Amigos em comum: ", amigos_comuns)

# Quem são os amigos diferentes entre Alice e Diana
amigos_alice = set(amizades["Alice"])
amigos_diana = set(amizades["Diana"])
amigos_diferentes = amigos_diana - amigos_alice #Conjunto com mais elementos deve vir primeiro
print("Amigos diferentes", amigos_diferentes)

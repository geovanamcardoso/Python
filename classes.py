# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}")
        

p1 = Pessoa("Ana", 15)
p2 = Pessoa("Paula", 23)

p1.apresentar()
p2.apresentar()


pessoas = [ 
    Pessoa("Ana", 15),
    Pessoa("Paula", 26),
    Pessoa("Maria", 56),
    Pessoa("Larissa", 12),
    Pessoa("Yasmin", 20)
    ]

for i in pessoas:
    i.apresentar()
    

'''Ex. 3 Crie um algoritmo com a função class para calcular área de um retângulo. Crie as 
duas variáveis (base, altura). Crie a função área, crie a função perímetro e teste os respectivos
valores: 
    V1 
    base = 4, altura = 5
    
    V2
    base = 7, altura = 3'''
    
class Area:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        area = self.base * self.altura
        
        print(f"A área do retângulo é {area:.2f}")
        
    def perimetro(self):
        perimetro = (2*self.base) + (2* self.altura)
        
        print(f"O perímetro do retângulo é {perimetro:.2f}")
        
a1 = Area(5 , 5)

a1.area()
a1.perimetro()

v1 = Area(4, 5)
v1.area()
v1.perimetro()

v2 = Area(7, 3)
v2.area()
v2.perimetro()


'''Ex.4 Crie um algoritmo para mostrar o carro e armazenar em uma lista. Crie as características
Marca, Ano, Cor, etc. Após isso, crie uma estrutura para mostrar as características de cada carro.

Ex.5 Crie um algoritmo com os atributos Nome, nota1, nota2. Adicione um método Média, que retorne
a media das notas. Depois crie uma estrutura para mostrar todas as informações.'''

class Carro:
    def __init__(self, marca, ano, cor):
        self.marca = marca
        self.ano = ano
        self.cor = cor
        
    def mostrar_carro(self):
        print(f" -- CARRO -- \nMarca = {self.marca} \nAno = {self.ano} \nCor = {self.cor}")
        
c1 = Carro("Teste", "2006", "Azul")
c1.mostrar_carro()

class Media:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        
    def media(self):
        media = (self.nota1 + self.nota2) / 2
        
        print(f"Nome: {self.nome} \nMédia: {media:.2f}")
        
aluno1 = Media("Anna", 10, 6)
aluno1.media()
    

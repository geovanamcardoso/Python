# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Ex.1
class Carrinho:
    def __init__(self):
        self.produtos = []
        
    def adicionar_produtos(self, produto):
        self.produtos.append(produto)
        print(f"Produto {produto} adicionado!")
       
    def remover_produtos(self, produto):
       if produto in self.produtos:
           self.produtos.remove(produto)
           print(f"Produto {produto} removido!")
       else:
           print("Produto não está no carrinho!")
          
    def exibir_produtos(self):
        if self.produtos:
            for produto in self.produtos:
                print(produto)
        else:
            print("Carrinho está vazio!")
            
carrinho =  Carrinho()

carrinho.adicionar_produtos('notebook')
carrinho.adicionar_produtos('pc')
carrinho.adicionar_produtos('teclado')
carrinho.exibir_produtos()

carrinho.remover_produtos('teclado')
carrinho.exibir_produtos() 

#Ex. 2
class Agenda:
    def __init__(self):
        self.contatos = {}
        
    def adicionar_contatos(self, nome, telefone):
        self.contatos[nome] = telefone
        print(f"Contato {nome} - {telefone} adicionado!")
        
    def buscar_contatos(self, nome):
        if nome in self.contatos:
            print(f"{nome} está na Agenda.")
        else:
            print(f"{nome} não está na Agenda.")
            
    def remover_contatos(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"contato {nome} removido!")
        else:
            print(f"{nome} não está na Agenda")
            
agenda = Agenda()

agenda.adicionar_contatos("Ana", "444444")
agenda.adicionar_contatos("Maria", "555555")
agenda.buscar_contatos("Ana")
agenda.remover_contatos("Ana")

#Ex. 3
class Calculadora:
    def __init__(self):
        self.operacoes = []

    def soma(self, num1, num2):
        soma = num1 + num2 
        print(f"{num1} + {num2} = {soma} ")
        self.operacoes.append(soma)

    def subtracao(self, num1, num2):
        subtracao = num1 - num2
        print(f"{num1} - {num2} = {subtracao} ")
        self.operacoes.append(subtracao)

    def multiplicacao(self, num1, num2):          
        multiplicacao = num1 * num2
        print(f"{num1} x {num2} = {multiplicacao} ")
        self.operacoes.append(multiplicacao)
        
    def divisao(self, num1, num2):
        divisao = num1 / num2
        print(f"{num1} / {num2} = {divisao} ")
        self.operacoes.append(divisao)
    
    def exibir_operacoes(self):
        print(self.operacoes)

calculadora = Calculadora()
calculadora.soma(5, 5)
calculadora.subtracao(5, 5)
calculadora.multiplicacao(5, 5)
calculadora.divisao(5, 5)
calculadora.exibir_operacoes()
        
        
#Ex. 4
class Turma:
    def __init__(self):
        self.alunos = {}
        
    def adicionar_alunos(self, nome, nota):
        self.alunos[nome] = nota
        print(f"Aluno(a) {nome} - {nota} adicionado(a)!")
        
    def calcular_média(self):
        if not self.alunos:
            return 0
        else:
            sum(self.alunos.values() ) / len(self.alunos)
            
    def listas_aprovados(self):
        for nome, nota in self.alunos.items():
            if nota >= 7:
                print(f"")
       
        

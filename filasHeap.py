# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Ex.1
import heapq

fila = []

heapq.heappush(fila,(1, "Emergência"))
heapq.heappush(fila,(3, "Consulta"))
heapq.heappush(fila,(1, "Exame"))

print(fila)

while fila:
    print(heapq.heappop(fila))
    
# ------------------------------------------------------    
    
#Ex.2 
import heapq

fila = []

heapq.heappush(fila,("Emergência", 1))
heapq.heappush(fila,("Consulta", 3))
heapq.heappush(fila,("Exame", 1))

# Converter para heap correto

fila_corrigida = [(prioridade, nome) for nome, prioridade in fila]
print(fila_corrigida)

while fila_corrigida:
    prioridade, nome = heapq.heappop(fila_corrigida)
    print(nome, prioridade)
    
# ------------------------------------------------------------------

'''Ex.3 - Crie um algoritmo para solicitar 5 informações para o usuário:
    nome, cpf e prioridade. Após isso, deixe a informação na seguinte ordem: 
    prioridade, nome e cpf. Finalmente, atenda a lista por ordem de prioridade.
   
    
usuarios = []

while True:
    op = input("1 - CADASTRAR | 2 - ATENDER |3- SAIR")
    
    match op:
        case op == "1":
            nome = input("Nome:")
            cpf = input("CPF:")
            prioridade = int(input("Prioridade (1 a 5):"))
            
            heapq.heappush(usuarios, (nome, cpf, prioridade))
            
        case op == "2":
            usuarios_org = [(prioridade, nome, cpf) for nome, cpf, prioridade in usuarios]
            print(f"Atendendo usuário {usuarios_org[1] - Prioridade {usuario_org[0]}}")
            usuarios_org.pop(0)
            
       case op == "3":  
           print(f"Usuários desorganizadas: {usuarios}")
           usuarios_org = [(prioridade, nome, cpf) for nome, cpf, prioridade in usuarios]
           print(f"USUÁRIOS CADASTRADOS: {usuarios_org} ")
           break
   '''          
  
 # CORREÇÃO EX.1 
lista_completa = []

for i in range(5):
    nome = input("Nome:")
    cpf = input("CPF:")
    priori = int(input("Prioridade (1 a 5):"))

    lista_nome_priori = [nome, cpf, priori]
    lista_completa.append(lista_nome_priori)
    print(lista_completa)

    
    
''' Ex.4 - Crie uma estrutura para solicitar a quantidade de informações que o usuário quiser
para inserir clientes de uma loja e serviços de carros (troca de óleo, pneus,
troca de paleta, etc). Crie uma estrutura para incluir as informações dos clientes (nome, 
carro, tipo de serviço) e atenda por ordem de chegada. Utilize a biblioteca heapq para 
resolver o problema.                                                                                   
'''    

'''Ex.5 - Crie uma estrutura para atender clientes de uma loja de roupas, solicite informações
como nome, cpf, tipo de presente e se é para presente ou não. Deixe as informações em uma lista
dentro de lista. Finalmente, atenda os clientes por ordem de chegada.
'''



    

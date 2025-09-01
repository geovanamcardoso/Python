'''Strings não são um tipo de dado primitivo, char é. Strings são listas de char(caractere), podemos ler e manipulá-la ccom as funções de lista. '''

nome = " Geovana Maria "

#Imprime cada letra do início ao fim em cada linha
for i in range(len(nome)):
    print(nome[i])
print('')    

#Imprime cada letra de trás para frente em cada linha
for i in range(len(nome),0,-1):
    print(nome[i-1])
print('')    

#Imprime em uma linha de trás para frente
for i in range(len(nome),0,-1):
    print(nome[i-1], end="\t")
print('')    

#Imprime em uma linha do início ao fim
for i in range(len(nome)):
    print(nome[i], end="\t")
print('')    

#Separa a string a partir do parâmetro, que por padrão é espaço. Retorna sub-strings
print(nome.split())

#Separa a string a partir do a
print(nome.split('a'))

#Remove os espaços em branco do início e do final da String, podendo remover outro caractere se for inserido como parâmetro
print(nome.strip())

#Remove o G do início e do fim
nome_strip = nome.strip()
print(nome_strip.strip('G'))

#Retorna o index do char
print(nome.index('e'))

#Converte os caracteres para maiúsculo
print(nome.upper())
#Converte os caracteres para minúsculo
print(nome.lower())

#Junta as strings de uma lista em uma só, a str é usada no meio das strings da lista como separador
sobrenomes = ['da','Silva','Cardoso']
sobrenome = ' '.join(sobrenomes)
print(sobrenome)

#Usando 10 como separador ao invés de espaço
# sobrenomes = ['da','Silva','Cardoso']
# sobrenome = '10'.join(sobrenomes)
# print(sobrenome)

#Substituindo strings, primeiro a antiga e depois a nova
print(nome.replace('Maria', 'Cardoso'))

#Inserindo variáveis na string
completo = 'Meu nome completo é {}{} '.format(nome,sobrenome)
print(completo)

#Fatiamento de string
print(nome[0:len(nome)]) #Começo ao fim
print(nome[:]) #Também começo ao fim, mesma coisa que print(nome[])
print(nome[-11]) #Começa dos últimos 11 caracteres
print(nome[::-1]) #Reverte a string completa
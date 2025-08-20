#Exercício 1
def mostrar_informacoes(nome: str, idade: int, cidade: str) -> str:
    '''Essa função recebe 3 parâmetros nomeados e imprime na tela as informações recebidas'''
    exibe: str  = f'Seu nome é {nome},tem {idade} anos de idade e mora em {cidade}.'
    return exibe

print(mostrar_informacoes(cidade='SP',nome='Geovana', idade=19))

#Exercício 2
def calcular_area_retangulo(base: int = 1, altura: int = 1) -> float:
    '''Essa função recebe o valor da base e altura de um retângulo e retorna sua área'''
    area: float = base * altura
    return area

print(f'A área padrão do retângulo é {calcular_area_retangulo()}')
inBase = int(input('Digite a base do retângulo: '))
inAltura = int(input("Digite a altura do retângulo: "))
print(f'A área do retângulo é {calcular_area_retangulo(inBase,inAltura)}')

#Exercício 3
def soma(a: float, b:float) -> float:
    '''Essa função recebe dois valores e retorna a soma entre eles'''
    return a + b

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

print(f'A soma dos números {num1} e {num2} é {soma(num1,num2):.2f}')

#Exercício 4
def enviar_email(destinatario: str, assunto: str = 'Sem assunto', corpo: str = ''):
    '''Essa função recebe 3 informações: Destinatário, Assunto e Corpo (da mensagem), o Assunto é, por padrão, Sem assunto e o Corpo, vazio. Ela retorna as informações recebidas. '''
    email: str = f'Destinatário: {destinatario}\nAssunto:{assunto}\nCorpo:{corpo}\n'
    return email

print(enviar_email('Maria'))

#Exercício 5
def concatenar_strings(str1: str, str2: str, separador: str = ' ', ) -> str:
    '''Essa função recebe duas strings e retorna ambas com um separador(espaço) entre elas'''
    return str1 + separador + str2

print('Geovana', 'Maria')

#Exercício 6
def comprar_produto(produto: str = 'Produto desconhecido', quantidade: int = 1) -> str:
    '''Essa função recebe o nome do produto e sua quantidade. Exibe o nome do produto escolhido e sua quantidade.'''
    return(f'Produto:{produto}\nQuantidade:{quantidade}\n')

print(comprar_produto())
print(comprar_produto(quantidade=5, produto='Caneta'))

#Exercício 7
def lista(itens: []) -> str:
    '''Essa função recebe uma lista de strings e exibe cada item em linhas separadas.'''
    for i in range(len(itens)):
        print(f'{itens[i]}\n')

lista1 = ['A', 'B','C', 'D']

lista(lista1)




'''Ao criar um arquivo no python, ele já vem padrão utf-8, não precisamos colocar o encoding
no open
arquivos criados no diretório, precisa do encoding
a variável arquivo funciona como ponteiro, guarda o endereço do arquivo
para  windows, tem que colocar \\ no caminho'''

arquivo = open('exterminador.txt', 'r')

for linha in arquivo:
    print(linha, end='')

arquivo.close()

'''
arquivo = open('exterminador.txt', 'w')

arquivo.write('Exterminador é o nome da calopsita do Gustavo.')

arquivo.close()

arquivo = open('geovana.txt', 'a')

texto = input('Digite um texto: ')

arquivo.write('\n' + texto + '\n')

arquivo.close()
'''





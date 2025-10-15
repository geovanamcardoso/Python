"""
ATENÇÃO: necessário instalar o pacote requests (Python package manager -> requests -> ver 2.32.5)
"""
import requests #Importar a biblioteca

try:
    cep = input('Digite o cep: ')
    response = requests.get(f'http://viacep.com.br/ws/{cep}/json/') #essa variavel (response) recebe o conteúdo do arquivo json em string

    if response.status_code == 200: #status_code verifica se a estrutura do json está correta e retorna um código de status, 200 é ok
        dicionario = response.json() #essa variavel (dicionario) recebe o texto da variavel response (que possui uma str com a estrutura de json)

        if 'erro' in dicionario: #recebeu o texto json mas possui erro
            print('CEP inexistente')
        else:
            print(f"Rua: {dicionario['logradouro']}")
            print(f"Bairro: {dicionario['bairro']}")
            print(f"Cidade: {dicionario['localidade']}")
            print(f"Estado: {dicionario['uf']}")
    else:
        print(f'Erro de requisição: {response.status_code}') #se o status_code retornar algum código diferente de 200
except requests.exceptions.ConnectionError as erro: #se houver erro de conexão com a API
    print('Erro. Erro de Conexão com API')
except Exception as erro: #qualquer outro erro na execução do código
    print(f'Erro: {erro}')

# print(dicionario) #essa variável é uma dicionário (string)!

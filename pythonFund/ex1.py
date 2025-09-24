while True:
    try:
        a = int(input('Digite um numero: '))
        b = int(input('Digite um outro numero: '))
        if a <= 0 or b <= 0:
            raise TypeError('O numero informado deve ser positivo')   # gera uma exceção
        c = a / b
        print(f'Resultado: {c}')
    except ZeroDivisionError:
        print('ERRO: ocorreu uma divisão por zero')
    except ValueError:
        print('ERRO: O numero informado deve ser inteiro')
    except TypeError as mensagem:
        print(f'ERRO: {mensagem}')
    except Exception as mensagem:
        print(f'ERRO Inesperado: {mensagem}')
    else:                       # EXECUTA SE NAO HOUVER EXCEÇÃO
        print('Operação realizada com sucesso.')
        break
    #finally:
print('Fim do programa')
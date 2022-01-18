
lista = [1, 10]

#Tratamento de erro
try:

    #Forçando erro de divisão
    #Mude a divisão para 0
    devisao = 10 / 1
    #forçando erro de lista
    #acesse um index invalido
    numero = lista[1]

#Existe uma arvore de erro BaseException e o primeiro
#Entao fazendo esse comando os erro cai no base e joga em ex
#ex retorna a mensagem (erro desconhecido) e format traz a mensagem de erro
except BaseException as ex:
    print('Erro desconhecido. {}'.format(ex))

#Tratando erro de divisão
except ZeroDivisionError:
    #mensagem que vai ser enviada
    print('Não é possivel fazer uma divisão por 0')
#Tratando erro da lista
except IndexError:
    #mensagem de erro enviada
    print('Erro ao acessar um index invalido da lista')
#Executa quando não existe exceção
else:
    print('Executa quando não ocorrer exceção')
print('-'*30)

#Trando erros
try:
    arquivo = open('teste.txt', 'r')
    arquivo.read()
    divisao = 10/0

#Mostrando erro
except Exception as ex:
    print('Ouve um erro. {}'.format(ex))
#Finally mesmo com erro ele vai executa
#arquivo.close
finally:
    print('Executa sempre')
    print('fechando arquivo')
    arquivo.close()
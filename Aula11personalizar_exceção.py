#Tratamento de erros
#Classe erda Exception
class Error(Exception):
    pass
#Subclasse de expeption
class InputError(Error):
    #método retorna uma mensagem
    def __int__(self, message):
        self.message = message

#quando (a) não for verdade
while True:
    try:
        a = int(input('Entre com um número:'))
        print(a)
        #se número for maior que 10
        if a > 10:
            raise InputError('Número não pode ser maior que 10')
        #se número for menor que 0
        elif a < 10:
            raise InputError('Número não pode ser menor que 0')
        #se input for verdadeira sai do loop
        break
    except ValueError:
        #se digitar caracteres
        print('Digite apenas números')

    #retorna mensagem raise inputerror personalizadas
    except InputError as ex:
        print(ex)

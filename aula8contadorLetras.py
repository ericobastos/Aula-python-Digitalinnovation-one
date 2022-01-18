
#Método contador letras
def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

if __name__ == '__main__':

    #contador recebe os valores novos
    #x erda parametro
    #quantidade lê x
    #contador adiciona o valor que quantida leu
    #e retorna a variavel contador com os valores

    #passo a lista que vai ser contada
    lista = ['erico','bastos']
    #chamo o método e passo a lista e imprimo
    print(contador_letras(lista))

    #Usando lambda para contador de letras
    contador_letras1 = lambda palavras: [len(a)for a in palavras]
    #variavel receba o lambda
    #parametro de lambda é palavras
    #laço recebe (a) que erda parametro palavras
    #len lê (a) que erdou parametro

    #passo a lista e chamo variavel que recebeu a função
    lista1 = ['erico']
    print(contador_letras1(lista1))

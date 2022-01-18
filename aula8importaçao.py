#importação de arquivo e usando funções deles
from aula7televisao import Televisao
from aula7_calculadora1_usando_init import Calculadora
from aula8contadorLetras import contador_letras

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora (5 , 1)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_de_letras = (contador_letras(lista))
    print('total de letras por palavra: {}'.format(total_de_letras))




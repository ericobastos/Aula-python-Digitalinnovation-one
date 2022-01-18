#Classe calculadora
class Calculadora:
    #métodos passando dois parametros
    def soma(self,valor1 , valor2):
        return valor1 + valor2

    def subtraçao(self, valor1, valor2):
        return valor1 - valor2

    def multiplicaçao(self, valor1, valor2):
        return valor1 * valor2

    def divisao(self, valor1, valor2):
        return valor1 / valor2

    def potencia(self, valor1, valor2):
        return valor1 ** valor2

if __name__ == '__main__':

    #Instanciando classe calculadora
    calculadora = Calculadora()
    #Chamo classe e o método
    #e passo dois objetos
    print(calculadora.soma(10,5))
    print(calculadora.subtraçao(10,5))
    print(calculadora.multiplicaçao(10,5))
    print(calculadora.divisao(10,5))
    print(calculadora.potencia(10,5))
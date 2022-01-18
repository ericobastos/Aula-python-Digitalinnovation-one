#Função tudo aquilo que retorna um valor
#Método é aquilo que não retorna

#Classe
class Calculadora:
    #iniciando classe, com dois objetos
    def __init__(self, num1, num2):
        self.valor1 = num1
        self.valor2 = num2
    #método soma
    def soma(self):
        return self.valor1 + self.valor2
    #método subtração
    def subtraçao(self):
        return self.valor1 - self.valor2
    #método divisão
    def divisao(self):
        return self.valor1 / self.valor2
    #método multiplicação
    def multiplicaçao(self):
        return self.valor1 * self.valor2
    #método potencia
    def potencia(self):
        return self.valor1 ** self.valor2

if __name__ == '__main__':

    #instanciando classe calculadora
    #passando 2 valores == (valor1,valor2)
    calculadora = Calculadora(10,5)
    #Chamando classe e método
    print(calculadora.soma())
    print(calculadora.subtraçao())
    print(calculadora.divisao())
    print(calculadora.multiplicaçao())
    print(calculadora.potencia())

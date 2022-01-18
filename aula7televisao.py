#Classe televisão
class Televisao:
    #iniciando classe
    def __init__(self):
        self.ligada = False
        self.canal = 5
    #métodos da classe
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

if __name__ == '__main__':


    #instanciando classe
    televisao = Televisao()
    #Chama métodos e objetos
    print(televisao.ligada)
    print(televisao.canal)
    televisao.power()
    print(televisao.ligada)
    televisao.aumenta_canal()
    print(televisao.canal)
    televisao.diminui_canal()
    print(televisao.canal)

#Usando python console para manipular o arquivo
#Só fazer import aula7televisao
#e instacia a classe
#assim televisao = aula7televisao.Televisao()
#e chama os métodos
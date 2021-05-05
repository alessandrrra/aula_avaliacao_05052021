from periferico import Periferico

class Mouse (Periferico):
    def __init__(self, marca = "", cor = "", preco, tipoconexao):
        self.marca = marca
        self.cor = cor
        if preco >= 0:
            self.preco = preco
        else:
            self.preco = 0
        self.__tipoconexao = tipoconexao

    @property
    def marca(self):
        return self.marca

    @property
    def cor(self):
        return self.cor

    @property
    def preco(self):
        return self.preco

    @property
    def tipoconexao(self):
        return self.__tipoconexao

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @preco.setter
    def preco(self, preco):
        if preco >= 0 :
            self.preco = preco
        else:
            print("Insira um valor correto.")

    @tipoconexao.setter
    def tipoconexao(self, tipoconexao):
        self.__tipoconexao = tipoconexao

    def getinformacoes(self):
        return print("Marca: ", self.marca, "\nCor: ", self.cor, "\nPreço: ", self.preco, "\nTipo de conexão: ", self.__tipoconexao)

    def cadastrar(self):
        return print("Teclado cadastrado.")
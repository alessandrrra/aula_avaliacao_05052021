from periferico import Periferico

class Teclado (Periferico):
    def __init__(self, marca = "", cor = "", preco, layout):
        self.marca = marca
        self.cor = cor
        if preco >= 0:
            self.preco = preco
        else:
            self.preco = 0
        self._layout = layout

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
    def layout(self):
        return self._layout

    @marca.setter
    def marca(self, marca):
        self.marca = marca

    @cor.setter
    def cor(self, cor):
        self.cor = cor

    @preco.setter
    def preco(self, preco):
        if preco >= 0 :
            self.preco = preco
        else:
            print("Insira um valor correto.")

    @layout.setter
    def layout(self, layout):
        self._layout = layout

    def getinformacoes(self):
        return print("Marca: ", self.marca, "\nCor: ", self.cor, "\nPreço: ", self.preco, "\nLayout: ", self._layout)

    def cadastrar(self):
        return print("Teclado cadastrado.")
from abc import ABCMeta, abstractmethod

class Periferico(metaclass=ABCMeta):
    @property
    def marca(self):
        pass

    @property
    def cor(self):
        pass

    @property
    def preco(self):
        pass

    @marca.setter
    @cor.setter
    @preco.setter

    @abstractmethod
    def cadastrar(self):
        pass

    def getInformacoes(self, marca, cor, preco):
        pass


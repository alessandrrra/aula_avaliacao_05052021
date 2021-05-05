from periferico import Periferico
from teclado import Teclado
from mouse import Mouse

divisao = "-----------------"

mouse = Mouse()
mouse.cadastrar()
mouse.marca = "Redragon"
mouse.cor = "Preto"
mouse.preco = 70.00
mouse.tipoconexao = "USB"
mouse.getInformacoes

print(divisao)

teclado = Teclado()
teclado.cadastrar()
teclado.marca = "Multilaser"
teclado.cor = "Preto"
teclado.preco = 50.00
teclado.layout = "ABNT"
teclado.getInformacoes

print(divisao)
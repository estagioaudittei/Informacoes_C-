class ICliente():
    def validar(self):
        print("vai sobre-escrever?")

class Cliente(ICliente):
    def validar(self):
        print("Sobre-escreveu")

clienteTeste = Cliente()
clienteTeste.validar()
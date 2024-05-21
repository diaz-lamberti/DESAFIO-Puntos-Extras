import random

# Definir clase Dado, con atributos como valor y cara actual
class Dado():
    valor = []
    def tirar(self, cantidad):
        self.cantidad = cantidad
        for i in range(cantidad):
            self.valor.append(random.randint(1, 6))
    
dado = Dado()
dado.tirar(5)
print(dado.valor)

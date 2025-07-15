import random
from objetos import Objeto


class Entorno:
    def __init__(self, ancho=5, alto=5):
        self.ancho = ancho
        self.alto = alto
        self.matriz = [[None for _ in range(ancho)] for _ in range(alto)]

    def colocar_objetos(self, objeto):
        if not isinstance(objeto, Objeto):
            raise ValueError(
                "El objeto debe ser una instancia de la clase Objeto")

        while True:
            x = random.randint(0, self.alto - 1)
            y = random.randint(0, self.ancho - 1)

            if self.matriz[x][y] is None:
                self.matriz[x][y] = objeto
                print(
                    f"🧩 Objeto '{objeto.nombre}' colocado en la posición ({x}, {y})")
                break

    def get_objeto(self, posicion):
        x, y = posicion
        return self.matriz[x][y]

    def mostrar(self):
        print("🌐 Entorno:")
        for fila in self.matriz:
            print(["🔲" if obj is None else "🧩" for obj in fila])

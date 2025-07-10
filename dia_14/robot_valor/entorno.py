import random
from objetos import Objeto


class Entorno:
    def __init__(self, ancho, alto, cantidad_objetos):
        self.ancho = ancho
        self.alto = alto
        self.matriz = [[None for _ in range(ancho)] for _ in range(alto)]
        self.colocar_objetos(cantidad_objetos)

    def colocar_objetos(self, cantidad):
        for _ in range(cantidad):
            x = random.randint(0, self.alto - 1)
            y = random.randint(0, self.ancho - 1)
            peso = random.randint(1, 10)
            nombre = f"Obj{peso}"
            self.matriz[x][y] = Objeto(nombre, "Tipo", peso)

    def mostrar(self):
        for fila in self.matriz:
            print(" | ".join(["🧩" if obj else "🔲" for obj in fila]))

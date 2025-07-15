# dia_15/robot_sensor_realista/entorno.py

import random


class Entorno:
    def __init__(self, ancho=5, alto=5, cantidad_objetos=5):
        self.ancho = ancho
        self.alto = alto
        self.matriz = [[None for _ in range(ancho)] for _ in range(alto)]
        self.objetos_disponibles = ["💎", "🔋", "📦", "🔧", "⚙️"]
        self.repartir_objetos(cantidad_objetos)

    def repartir_objetos(self, cantidad):
        disponibles = [(i, j) for i in range(self.alto)
                       for j in range(self.ancho)]
        random.shuffle(disponibles)

        for _ in range(min(cantidad, len(disponibles))):
            x, y = disponibles.pop()
            objeto = random.choice(self.objetos_disponibles)
            self.matriz[x][y] = objeto

    def mostrar(self):
        for fila in self.matriz:
            print(" ".join(obj if obj else "⬜" for obj in fila))

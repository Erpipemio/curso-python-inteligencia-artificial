import random


class Entorno:
    def __init__(self, ancho=5, alto=5, cantidad_objetos=5, cantidad_obstaculos=3):
        self.ancho = ancho
        self.alto = alto
        self.matriz = [[None for _ in range(ancho)] for _ in range(alto)]
        self.objetos_disponibles = ["💎", "🔋", "📦", "🔧", "⚙️"]
        self.obstaculos = ["⬛"]
        self.repartir_objetos(cantidad_objetos)
        self.repartir_obstaculos(cantidad_obstaculos)

    def posiciones_libres(self):
        return [(i, j) for i in range(self.alto)
                for j in range(self.ancho) if self.matriz[i][j] is None]

    def repartir_obstaculos(self, cantidad):

        disponibles = self.posiciones_libres()
        random.shuffle(disponibles)

        for _ in range(min(cantidad, len(disponibles))):
            x, y = disponibles.pop()
            obstaculo = random.choice(self.obstaculos)
            self.matriz[x][y] = obstaculo

    def repartir_objetos(self, cantidad):
        disponibles = self.posiciones_libres()
        random.shuffle(disponibles)

        for _ in range(min(cantidad, len(disponibles))):
            x, y = disponibles.pop()
            objeto = random.choice(self.objetos_disponibles)
            self.matriz[x][y] = objeto

    def mostrar(self):
        for fila in self.matriz:
            print(" ".join(obj if obj else "⬜" for obj in fila))

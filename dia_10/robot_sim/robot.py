from entorno import Entorno
from objetos import Objeto


class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = (0, 0)
        self.bolsa = []

    def mover(self, direccion):
        x, y = self.posicion
        if direccion == "norte":
            x -= 1
        elif direccion == "sur":
            x += 1
        elif direccion == "este":
            y += 1
        elif direccion == "oeste":
            y -= 1

        # Limitar dentro de un mapa de 5x5
        x = max(0, min(x, 4))
        y = max(0, min(y, 4))

        self.posicion = (x, y)
        print(f"🤖 {self.nombre} se movió a {self.posicion}")

    def recoger_objeto(self, objeto):
        if objeto not in self.bolsa:
            self.bolsa.append(objeto)
            print(f"🤖 {self.nombre} recogió el objeto: {objeto}")
        else:
            print(f"🤖 {self.nombre} ya tiene el objeto: {objeto}")

    def detectar(self, entorno):
        objeto = entorno.get_objeto(self.posicion)
        if objeto:
            print(f"🔍 {self.nombre} detectó un objeto: {objeto}")
            return objeto
        else:
            print(f"🔍 {self.nombre} no detectó nada.")
            return None


def recolectar(self, objeto, entorno):
    if objeto:
        self.bolsa.append(objeto)
        x, y = self.posicion
        entorno.matriz[x][y] = None  # Se retira el objeto del entorno
        print(f"✅ {self.nombre} recolectó: {objeto}")

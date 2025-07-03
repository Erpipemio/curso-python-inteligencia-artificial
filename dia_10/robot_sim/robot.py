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

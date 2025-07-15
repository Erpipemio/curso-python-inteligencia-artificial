class Objeto:
    def __init__(self, nombre, tipo, peso):
        self.nombre = nombre
        self.tipo = tipo
        self.peso = peso

    def __str__(self):
        return f"{self.nombre} ({self.tipo}, {self.peso}kg)"

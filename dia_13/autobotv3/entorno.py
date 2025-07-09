import random
from objetos import Objeto


class Entorno:
    def __init__(self, ancho=5, alto=5):
        self.ancho = ancho
        self.alto = alto
        self.matriz = [[None for _ in range(ancho)] for _ in range(alto)]
        self.objetos_disponibles = []  # Para seguimiento de objetos

    def colocar_objetos(self, objeto, x=None, y=None):
        """Coloca un objeto en una posición específica o aleatoria"""
        if not isinstance(objeto, Objeto):
            raise ValueError(
                "El objeto debe ser una instancia de la clase Objeto")

        if x is not None and y is not None:
            # Posición específica
            if self.matriz[x][y] is None:
                self.matriz[x][y] = objeto
                self.objetos_disponibles.append(objeto)
                print(f"🧩 Objeto '{objeto.nombre}' colocado en ({x}, {y})")
                return True
            return False
        else:
            # Posición aleatoria
            for _ in range(100):  # Intentos máximos
                x = random.randint(0, self.alto - 1)
                y = random.randint(0, self.ancho - 1)
                if self.matriz[x][y] is None:
                    self.matriz[x][y] = objeto
                    self.objetos_disponibles.append(objeto)
                    print(f"🧩 Objeto '{objeto.nombre}' colocado en ({x}, {y})")
                    return True
            print(f"⚠️ No se pudo colocar el objeto '{objeto.nombre}'")
            return False

    def get_objeto(self, posicion):
        x, y = posicion
        if 0 <= x < self.alto and 0 <= y < self.ancho:
            return self.matriz[x][y]
        return None

    def remover_objeto(self, posicion):
        x, y = posicion
        if 0 <= x < self.alto and 0 <= y < self.ancho:
            obj = self.matriz[x][y]
            if obj:
                self.matriz[x][y] = None
                if obj in self.objetos_disponibles:
                    self.objetos_disponibles.remove(obj)
                return obj
        return None

    def mostrar(self):
        """Muestra el entorno con formato mejorado"""
        print("\n" + "=" * (self.ancho * 3 + 4))
        print("🌐 Mapa del Entorno ({}x{})".format(self.ancho, self.alto))
        print("=" * (self.ancho * 3 + 4))

        # Encabezado de columnas
        print("   " + " ".join(f"{i:^3}" for i in range(self.ancho)))

        for i, fila in enumerate(self.matriz):
            # Fila con bordes
            print(
                f"{i} |" + "".join(f"{'🔲' if obj is None else '🧩':^3}" for obj in fila) + "|")

        print("=" * (self.ancho * 3 + 4))
        print(f"Objetos restantes: {len(self.objetos_disponibles)}\n")

    def obtener_posiciones_objetos(self):
        """Devuelve lista de posiciones (x,y) donde hay objetos"""
        return [(x, y) for x in range(self.alto) for y in range(self.ancho) if self.matriz[x][y] is not None]

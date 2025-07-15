import random


class Robot:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion  # (x, y)
        self.energia = 30
        self.log = []
        self.memoria = set()  # Guarda las posiciones visitadas

    def mover(self, direccion):
        x, y = self.posicion
        nueva_pos = {
            "norte": (x - 1, y),
            "sur": (x + 1, y),
            "este": (x, y + 1),
            "oeste": (x, y - 1)
        }.get(direccion, self.posicion)

        # Validar que no salga del mapa
        if 0 <= nueva_pos[0] < 5 and 0 <= nueva_pos[1] < 5:
            self.posicion = nueva_pos
            self.energia -= 1
            self.memoria.add(nueva_pos)
            self.log.append(
                f"🚶 Movido a {nueva_pos} ({direccion}) – Energía: {self.energia}")
        else:
            self.log.append(
                f"❌ Movimiento fallido hacia {direccion}. Posición fuera de límites.")

    def recolectar(self, objeto, entorno):
        x, y = self.posicion
        entorno.matriz[x][y] = None
        self.energia += 2
        self.log.append(
            f"✅ Recolectado {objeto} en ({x},{y}) – Energía: {self.energia}")

    def escanear_entorno(self, entorno):
        x, y = self.posicion
        visibles = []

        direcciones = {
            "norte": (x - 1, y),
            "sur":   (x + 1, y),
            "este":  (x, y + 1),
            "oeste": (x, y - 1)
        }

        for dir, (i, j) in direcciones.items():
            if 0 <= i < entorno.alto and 0 <= j < entorno.ancho:
                objeto = entorno.matriz[i][j]
                if objeto:
                    visibles.append((dir, objeto))
                    self.log.append(f"👀 Detectado {objeto} en {dir} ({i},{j})")
        return visibles

    def decidir_direccion_exploratoria(self):
        # Intenta moverse a direcciones que no ha visitado
        x, y = self.posicion
        opciones = {
            "norte": (x - 1, y),
            "sur":   (x + 1, y),
            "este":  (x, y + 1),
            "oeste": (x, y - 1)
        }

        no_visitadas = [dir for dir, pos in opciones.items()
                        if 0 <= pos[0] < 5 and 0 <= pos[1] < 5 and pos not in self.memoria]

        if no_visitadas:
            return random.choice(no_visitadas)
        else:
            return random.choice(list(opciones.keys()))

    def resumen_final(self):
        self.log.append("\n--- RESUMEN FINAL ---")
        self.log.append(f"Posición final: {self.posicion}")
        self.log.append(f"Energía restante: {self.energia}")
        self.log.append(f"Celdas exploradas: {len(self.memoria)}")
        print("\n".join(self.log))

    def exportar_log(self, ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("\n".join(self.log))

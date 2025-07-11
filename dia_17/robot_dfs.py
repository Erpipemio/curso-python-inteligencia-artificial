import random


class RobotDFS:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion
        self.energia = 30
        self.log = []
        self.memoria = set()
        self.obstaculos_memoria = set()
        self.stack = []  # Para el backtracking (DFS)

    def mover(self, nueva_pos, entorno):

        if (0 <= nueva_pos[0] < entorno.alto and
            0 <= nueva_pos[1] < entorno.ancho and
                entorno.matriz[nueva_pos[0]][nueva_pos[1]] != entorno.obstaculos):
            self.posicion = nueva_pos
            self.energia -= 1
            self.memoria.add(nueva_pos)
            self.log.append(
                f"🚶 Movido a {nueva_pos} – Energía: {self.energia}")
            return True
        else:
            self.log.append(f"❌ Movimiento bloqueado a {nueva_pos}")
            return False

    def recolectar(self, entorno):
        x, y = self.posicion
        objeto = entorno.matriz[x][y]
        if objeto and objeto != entorno.obstaculos:
            entorno.matriz[x][y] = None
            self.energia += 2
            self.log.append(
                f"✅ Recolectado {objeto} en ({x},{y}) – Energía: {self.energia}")

    def vecinos(self, entorno, pos):
        x, y = pos
        direcciones = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # N, S, E, O
        vecinos = []
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if (0 <= nx < entorno.alto and 0 <= ny < entorno.ancho and
                entorno.matriz[nx][ny] != entorno.obstaculos and
                    (nx, ny) not in self.memoria):
                vecinos.append((nx, ny))
        return vecinos

    def explorar_dfs(self, entorno):
        self.stack.append(self.posicion)
        self.memoria.add(self.posicion)
        while self.stack and self.energia > 0:
            actual = self.stack[-1]
            self.posicion = actual
            self.recolectar(entorno)
            vecinos_nuevos = self.vecinos(entorno, actual)
            if vecinos_nuevos:
                next_pos = random.choice(vecinos_nuevos)
                self.stack.append(next_pos)
                self.mover(next_pos, entorno)
            else:
                self.stack.pop()  # Backtrack (retrocede)

    def resumen_final(self):
        self.log.append("\n--- RESUMEN FINAL ---")
        self.log.append(f"Posición final: {self.posicion}")
        self.log.append(f"Energía restante: {self.energia}")
        self.log.append(f"Celdas exploradas: {len(self.memoria)}")
        print("\n".join(self.log))

    def exportar_log(self, ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("\n".join(self.log))

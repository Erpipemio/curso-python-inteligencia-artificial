import matplotlib.pyplot as plt
import numpy as np
import imageio
import os
from collections import deque


class RobotBFS:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion
        self.energia = 30
        self.log = []
        self.memoria = set()
        self.obstaculos_memoria = set()  # Celdas con obstáculos
        self.objetos_recolectados = 0
        self.camino = []
        self.celdas_recolectadas = set()

    def mover(self, nueva_pos, entorno):
        if not (0 <= nueva_pos[0] < entorno.alto and 0 <= nueva_pos[1] < entorno.ancho):
            self.log.append(
                f"❌ Movimiento inválido a {nueva_pos} – Fuera de límites")
            return False
        celda = entorno.matriz[nueva_pos[0]][nueva_pos[1]]
        if celda == entorno.simbolo_obstaculos:
            self.log.append(
                f"❌ Movimiento inválido a {nueva_pos} – Obstáculo encontrado")
            self.obstaculos_memoria.add(nueva_pos)
            return False

        self.posicion = nueva_pos
        self.energia -= 1
        self.memoria.add(nueva_pos)
        self.camino.append(nueva_pos)
        self.log.append(f"🚶 Movido a {nueva_pos} – Energía: {self.energia}")
        return True

    def recolectar(self, entorno):
        x, y = self.posicion
        objeto = entorno.matriz[x][y]

        # Solo recolectar si es un objeto válido (no obstáculo, no vacío)
        if objeto and objeto not in entorno.simbolo_obstaculos and objeto in entorno.objetos_disponibles:
            entorno.matriz[x][y] = None  # Eliminar objeto del entorno
            self.energia += 2
            self.objetos_recolectados += 1
            self.celdas_recolectadas.add((x, y))
            self.log.append(
                f"✅ Recolectado {objeto} en ({x},{y}) – Energía: {self.energia}")
            return True
        elif objeto in entorno.simbolo_obstaculos:
            self.obstaculos_memoria.add((x, y))
            self.log.append(
                f"🧱 ¡No se puede recolectar el obstáculo en ({x},{y})!")
        else:
            self.log.append(f"⬜ No hay nada para recolectar en ({x},{y})")
        return False

    def vecinos(self, entorno, pos):
        x, y = pos
        direcciones = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # N, S, E, O
        vecinos = []
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            nueva_pos = (nx, ny)
            # Verificar que esté dentro del entorno
            if not (0 <= nx < entorno.alto and 0 <= ny < entorno.ancho):
                continue

            # Evitar obstáculos (tanto conocidos como actuales)
            if (entorno.matriz[nx][ny] in entorno.simbolo_obstaculos or nueva_pos in self.obstaculos_memoria):
                continue

            # Si no ha sido visitado o contiene un objeto
            if nueva_pos not in self.memoria or entorno.matriz[nx][ny] in entorno.objetos_disponibles:
                vecinos.append(nueva_pos)
        return vecinos

    def explorar_bfs(self, entorno):
        queue = deque()
        queue.append(self.posicion)
        self.memoria.add(self.posicion)
        self.camino.append(self.posicion)
        while queue and self.energia > 0:
            actual = queue.popleft()
            self.posicion = actual
            self.recolectar(entorno)
            for vecino in self.vecinos(entorno, actual):
                if vecino not in self.memoria:
                    self.memoria.add(vecino)
                    queue.append(vecino)
                    self.camino.append(vecino)
                    self.mover(vecino, entorno)
                    if self.energia <= 0:
                        break

    def resumen_final(self):
        self.log.append("\n--- RESUMEN FINAL ---")
        self.log.append(f"Posición final: {self.posicion}")
        self.log.append(f"Energía restante: {self.energia}")
        self.log.append(f"Celdas exploradas: {len(self.memoria)}")
        print("\n".join(self.log))

    def exportar_log(self, ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("\n".join(self.log))

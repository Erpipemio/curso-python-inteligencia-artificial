import random
import matplotlib.pyplot as plt
import numpy as np
import imageio
import os


class RobotDFS:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion
        self.energia = 30
        self.log = []
        self.memoria = set()  # Todas las celdas visitadas
        self.obstaculos_memoria = set()  # Celdas con obstáculos
        self.stack = []  # Para el backtracking (DFS)
        self.objetos_recolectados = 0
        self.camino = []  # Para guardar el orden de las posiciones visitadas
        self.celdas_recolectadas = set()  # Para las celdas donde recolectó objeto

    def mover(self, nueva_pos, entorno):
        """Intenta moverse a una nueva posición"""
        # Verificar límites del entorno
        if not (0 <= nueva_pos[0] < entorno.alto and 0 <= nueva_pos[1] < entorno.ancho):
            self.log.append(
                f"❌ Movimiento bloqueado a {nueva_pos} (fuera de límites)")
            return False

        # Verificar obstáculos (tanto en memoria como en el entorno actual)
        celda = entorno.matriz[nueva_pos[0]][nueva_pos[1]]
        if celda in entorno.simbolo_obstaculos or nueva_pos in self.obstaculos_memoria:
            self.obstaculos_memoria.add(nueva_pos)
            self.log.append(
                f"🧱 Movimiento bloqueado a {nueva_pos} (obstáculo)")
            return False

        # Movimiento válido
        self.posicion = nueva_pos
        self.camino.append(nueva_pos)
        self.energia -= 1
        self.memoria.add(nueva_pos)
        self.log.append(f"🚶 Movido a {nueva_pos} – Energía: {self.energia}")
        return True

    def recolectar(self, entorno):
        """Intenta recolectar un objeto en la posición actual"""
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

    def vecinos_validos(self, entorno, pos):
        """Obtiene vecinos no visitados y sin obstáculos"""
        x, y = pos
        # Norte, Sur, Este, Oeste
        direcciones = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        vecinos = []

        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            nueva_pos = (nx, ny)

            # Verificar que esté dentro del entorno
            if not (0 <= nx < entorno.alto and 0 <= ny < entorno.ancho):
                continue

            # Evitar obstáculos (tanto conocidos como actuales)
            if (entorno.matriz[nx][ny] in entorno.simbolo_obstaculos or
                    nueva_pos in self.obstaculos_memoria):
                continue

            # Si no ha sido visitado o contiene un objeto
            if nueva_pos not in self.memoria or entorno.matriz[nx][ny] in entorno.objetos_disponibles:
                vecinos.append(nueva_pos)

        return vecinos

    def explorar_dfs(self, entorno):
        self.stack.append(self.posicion)  # Inicia con posición actual

        while self.stack and self.energia > 0:
            actual = self.stack[-1]  # Mira el tope de la pila

            # Intenta recolectar
            if entorno.matriz[actual[0]][actual[1]] in entorno.objetos_disponibles:
                self.recolectar(entorno)

            # Busca vecinos válidos
            vecinos = self.vecinos_validos(entorno, actual)

            if vecinos:
                # Expande hacia un vecino aleatorio
                siguiente = random.choice(vecinos)
                self.stack.append(siguiente)
                self.mover(siguiente, entorno)
            else:
                # Backtracking
                self.stack.pop()
                if self.stack:
                    self.mover(self.stack[-1], entorno)  # Retrocede

    def resumen_final(self):
        self.log.append("\n--- RESUMEN FINAL ---")
        self.log.append(f"Posición final: {self.posicion}")
        self.log.append(f"Energía restante: {self.energia}")
        self.log.append(f"Celdas exploradas: {len(self.memoria)}")
        self.log.append(
            f"Obstáculos detectados: {len(self.obstaculos_memoria)}")
        self.log.append(f"Objetos recolectados: {self.objetos_recolectados}")
        print("\n".join(self.log))

    def exportar_log(self, ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("\n".join(self.log))

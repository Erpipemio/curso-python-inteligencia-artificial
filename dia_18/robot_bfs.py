import random
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
        if celda == entorno.simbolo_obstaculo:
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
        if objeto and objeto not in entorno.simbolo_obstaculo and objeto in entorno.objetos_disponibles:
            entorno.matriz[x][y] = None  # Eliminar objeto del entorno
            self.energia += 2
            self.objetos_recolectados += 1
            self.celdas_recolectadas.add((x, y))
            self.log.append(
                f"✅ Recolectado {objeto} en ({x},{y}) – Energía: {self.energia}")
            return True
        elif objeto in entorno.simbolo_obstaculo:
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
            if (entorno.matriz[nx][ny] in entorno.simbolo_obstaculo or nueva_pos in self.obstaculos_memoria):
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

    def visualizar_recorrido(self, entorno):
        grid = np.zeros((entorno.alto, entorno.ancho))
        annotations = [["" for _ in range(entorno.ancho)]
                       for _ in range(entorno.alto)]

        # Obstáculos y objetos restantes
        for i in range(entorno.alto):
            for j in range(entorno.ancho):
                if entorno.matriz[i][j] == entorno.simbolo_obstaculos:
                    grid[i, j] = -1
                    annotations[i][j] = "X"
                elif entorno.matriz[i][j]:
                    grid[i, j] = 0.3
                    annotations[i][j] = "O"

        # Camino recorrido (excepto inicio)
        for idx, (i, j) in enumerate(self.camino):
            if grid[i, j] == 0:
                grid[i, j] = 0.6
                if (i, j) not in self.celdas_recolectadas:
                    annotations[i][j] = "·"

        # Celdas donde recolectó objeto
        for (i, j) in self.celdas_recolectadas:
            annotations[i][j] = "R"
            grid[i, j] = 0.7

        # Inicio y fin
        inicio = self.camino[0] if self.camino else self.posicion
        fin = self.camino[-1] if self.camino else self.posicion
        annotations[inicio[0]][inicio[1]] = "INICIO"
        grid[inicio[0], inicio[1]] = 0.9
        annotations[fin[0]][fin[1]] = "FIN"
        grid[fin[0], fin[1]] = 1.0

        plt.figure(figsize=(7, 7))
        plt.imshow(grid, cmap="YlGnBu", origin="upper")

        # Dibuja las letras/símbolos
        for i in range(entorno.alto):
            for j in range(entorno.ancho):
                txt = annotations[i][j]
                if txt:
                    color = "red" if txt == "X" else "black"
                    if txt == "R":
                        color = "orange"
                    elif txt == "INICIO":
                        color = "green"
                    elif txt == "FIN":
                        color = "blue"
                    plt.text(j, i, txt, va='center', ha='center',
                             fontsize=14, color=color, weight="bold")

        # Dibuja el recorrido con flechas
        if len(self.camino) > 1:
            for idx in range(len(self.camino) - 1):
                y0, x0 = self.camino[idx][1], self.camino[idx][0]  # (j,i)
                y1, x1 = self.camino[idx+1][1], self.camino[idx+1][0]
                plt.arrow(
                    y0, x0,  # origen
                    y1 - y0, x1 - x0,  # desplazamiento
                    length_includes_head=True,
                    head_width=0.15,
                    head_length=0.15,
                    fc="purple", ec="purple", alpha=0.7
                )

        plt.title("Recorrido y recolección del robot (DFS)")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.grid(False)
        plt.xticks(np.arange(entorno.ancho))
        plt.yticks(np.arange(entorno.alto))
        plt.tight_layout()
        plt.show()

    def animar_recorrido(self, entorno, ruta_gif="recorrido_robot.gif", ruta_mp4="recorrido_robot.mp4"):
        grid = np.zeros((entorno.alto, entorno.ancho))
        images = []

        # Carpeta temporal para los frames
        temp_dir = "frames_temp"
        os.makedirs(temp_dir, exist_ok=True)

        for paso, (i, j) in enumerate(self.camino):
            grid_step = np.zeros_like(grid)
            # Marca obstáculos y objetos
            for x in range(entorno.alto):
                for y in range(entorno.ancho):
                    if entorno.matriz[x][y] == entorno.simbolo_obstaculo:
                        grid_step[x, y] = -1
                    elif entorno.matriz[x][y]:
                        grid_step[x, y] = 0.3

            # Camino hasta el paso actual
            for idx in range(paso + 1):
                xi, yj = self.camino[idx]
                grid_step[xi, yj] = 0.6

            # INICIO y posición actual
            ini = self.camino[0]
            grid_step[ini[0], ini[1]] = 0.9
            grid_step[i, j] = 1.0

            fig, ax = plt.subplots(figsize=(6, 6))
            ax.imshow(grid_step, cmap="YlGnBu", origin="upper")
            for x in range(entorno.alto):
                for y in range(entorno.ancho):
                    if entorno.matriz[x][y] == entorno.simbolo_obstaculo:
                        ax.text(y, x, "X", ha='center', va='center',
                                color='red', fontsize=14)
                    elif entorno.matriz[x][y]:
                        ax.text(y, x, "O", ha='center', va='center',
                                color='black', fontsize=14)
            ax.text(ini[1], ini[0], "INICIO", ha='center', va='center',
                    color='green', fontsize=12, weight='bold')
            ax.text(j, i, str(paso + 1), ha='center', va='center',
                    color='purple', fontsize=12, weight='bold')
            ax.set_title(f"Paso {paso+1}")
            plt.axis("off")
            frame_path = os.path.join(temp_dir, f"frame_{paso:03d}.png")
            plt.savefig(frame_path)
            plt.close(fig)
            images.append(imageio.imread(frame_path))

        # Crea el GIF
        imageio.mimsave(ruta_gif, images, duration=0.5)
        print(f"✅ GIF guardado como: {ruta_gif}")

        # Crea el video MP4
        imageio.mimsave(ruta_mp4, images, fps=2)
        print(f"✅ Video MP4 guardado como: {ruta_mp4}")

        # Limpia los frames temporales
        for img in os.listdir(temp_dir):
            os.remove(os.path.join(temp_dir, img))
        os.rmdir(temp_dir)

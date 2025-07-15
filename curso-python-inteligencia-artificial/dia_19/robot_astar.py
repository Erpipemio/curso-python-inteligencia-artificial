import heapq
import matplotlib.pyplot as plt
import numpy as np
import imageio
import os
from collections import deque
# Asegúrate de que este módulo esté definido correctamente
# Importa tu clase Entorno desde el módulo correspondiente
from entorno import Entorno

import heapq
import matplotlib.pyplot as plt
import numpy as np
import imageio
import os
from collections import deque
from entorno import Entorno  # Asegúrate que esta importación es correcta


class RobotAStar:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion
        self.energia = 30
        self.log = []
        self.memoria = set()  # Todas las celdas visitadas
        self.obstaculos_memoria = set()  # Celdas con obstáculos
        self.objetos_recolectados = 0
        self.camino = []  # Historial completo de posiciones
        self.celdas_recolectadas = set()  # Celdas donde recolectó objetos
        self.caminos_astar = []  # Para visualizar cada camino A* individual

    def mover(self, nueva_pos, entorno):
        """Intenta moverse a una nueva posición verificando obstáculos y límites"""
        # Verificar límites del entorno
        if not (0 <= nueva_pos[0] < entorno.alto and 0 <= nueva_pos[1] < entorno.ancho):
            self.log.append(
                f"❌ Movimiento inválido a {nueva_pos} – Fuera de límites")
            return False

        # Verificar obstáculos
        celda = entorno.matriz[nueva_pos[0]][nueva_pos[1]]
        if celda in entorno.simbolo_obstaculos or nueva_pos in self.obstaculos_memoria:
            self.obstaculos_memoria.add(nueva_pos)
            self.log.append(
                f"❌ Movimiento inválido a {nueva_pos} – Obstáculo encontrado")
            return False

        # Movimiento válido
        self.posicion = nueva_pos
        self.energia -= 1
        self.memoria.add(nueva_pos)
        self.camino.append(nueva_pos)
        self.log.append(f"🚶 Movido a {nueva_pos} – Energía: {self.energia}")
        return True

    def recolectar(self, entorno):
        """Intenta recolectar un objeto en la posición actual"""
        x, y = self.posicion
        objeto = entorno.matriz[x][y]

        # Verificación triple de objeto válido
        if objeto and objeto not in entorno.simbolo_obstaculos and objeto in entorno.objetos_disponibles:
            entorno.matriz[x][y] = None  # Eliminar objeto del entorno
            self.energia += 2  # Recompensa por recolectar
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
        """Obtiene vecinos transitables no visitados o con objetos"""
        x, y = pos
        # Norte, Sur, Este, Oeste
        direcciones = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        vecinos = []

        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            nueva_pos = (nx, ny)

            # Verificar límites
            if not (0 <= nx < entorno.alto and 0 <= ny < entorno.ancho):
                continue

            # Evitar obstáculos
            if (entorno.matriz[nx][ny] in entorno.simbolo_obstaculos or
                    nueva_pos in self.obstaculos_memoria):
                continue

            # Priorizar celdas no visitadas o con objetos
            if nueva_pos not in self.memoria or entorno.matriz[nx][ny] in entorno.objetos_disponibles:
                vecinos.append(nueva_pos)

        return vecinos

    def heuristica(self, a, b):
        """Distancia Manhattan para el A*"""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def buscar_objeto_cercano(self, entorno):
        """Encuentra el objeto alcanzable más cercano usando BFS"""
        cola = deque([self.posicion])
        visitados = set([self.posicion])

        while cola:
            actual = cola.popleft()

            # Si encontramos un objeto
            if entorno.matriz[actual[0]][actual[1]] in entorno.objetos_disponibles:
                return actual

            # Explorar vecinos
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = actual[0] + dx, actual[1] + dy
                nueva_pos = (nx, ny)

                if (0 <= nx < entorno.alto and 0 <= ny < entorno.ancho and
                    nueva_pos not in visitados and
                        entorno.matriz[nx][ny] not in entorno.simbolo_obstaculos):

                    visitados.add(nueva_pos)
                    cola.append(nueva_pos)

        return None  # No hay objetos alcanzables

    def a_star(self, entorno, objetivo):
        """Implementación del algoritmo A* para encontrar camino óptimo"""
        open_set = []
        heapq.heappush(open_set, (0, self.posicion))
        came_from = {}
        g_score = {self.posicion: 0}  # Costo real desde inicio
        f_score = {self.posicion: self.heuristica(
            self.posicion, objetivo)}  # Costo estimado total

        while open_set:
            _, actual = heapq.heappop(open_set)

            # Llegamos al objetivo
            if actual == objetivo:
                # Reconstruir camino
                path = [actual]
                while actual in came_from:
                    actual = came_from[actual]
                    path.append(actual)
                path.reverse()
                self.caminos_astar.append(path)  # Guardar para visualización
                return path

            # Explorar vecinos
            for vecino in self.vecinos_validos(entorno, actual):
                tentative_g = g_score[actual] + 1  # Costo uniforme

                if vecino not in g_score or tentative_g < g_score[vecino]:
                    came_from[vecino] = actual
                    g_score[vecino] = tentative_g
                    f_score[vecino] = tentative_g + \
                        self.heuristica(vecino, objetivo)
                    heapq.heappush(open_set, (f_score[vecino], vecino))

        return None  # No hay camino

    def explorar_astar(self, entorno):
        """Algoritmo principal de exploración con A*"""
        while self.energia > 0:
            # Buscar objeto más cercano alcanzable
            objetivo = self.buscar_objeto_cercano(entorno)
            if objetivo is None:
                self.log.append("🎉 ¡No quedan objetos alcanzables!")
                break

            # Encontrar camino con A*
            path = self.a_star(entorno, objetivo)
            if not path:
                self.log.append("🚧 No hay camino válido al objetivo")
                break

            # Mover según el camino encontrado
            for paso in path[1:]:  # Saltar primera posición (actual)
                if self.energia <= 0:
                    break
                if not self.mover(paso, entorno):
                    break  # Si el movimiento falla

            # Intentar recolectar al llegar
            self.recolectar(entorno)

    def visualizar_recorrido(self, entorno):
        """Visualización mejorada del recorrido"""
        grid = np.zeros((entorno.alto, entorno.ancho))
        annotations = [["" for _ in range(entorno.ancho)]
                       for _ in range(entorno.alto)]

        # Mapear elementos del entorno
        for i in range(entorno.alto):
            for j in range(entorno.ancho):
                if entorno.matriz[i][j] in entorno.simbolo_obstaculos:
                    grid[i, j] = -1
                    annotations[i][j] = "X"
                elif entorno.matriz[i][j] in entorno.objetos_disponibles:
                    grid[i, j] = 0.3
                    annotations[i][j] = "O"

        # Dibujar caminos A* individuales
        for path in self.caminos_astar:
            for (i, j) in path:
                if grid[i, j] == 0:  # Solo si no es obstáculo/objeto
                    grid[i, j] = 0.5
                    annotations[i][j] = "·"

        # Destacar celdas recolectadas
        for (i, j) in self.celdas_recolectadas:
            grid[i, j] = 0.8
            annotations[i][j] = "R"

        # Marcar inicio y fin
        if self.camino:
            inicio = self.camino[0]
            fin = self.camino[-1]
            grid[inicio[0], inicio[1]] = 0.9
            annotations[inicio[0]][inicio[1]] = "INICIO"
            grid[fin[0], fin[1]] = 1.0
            annotations[fin[0]][fin[1]] = "FIN"

        # Configurar gráfico
        plt.figure(figsize=(8, 8))
        plt.imshow(grid, cmap="YlGnBu", origin="upper")

        # Añadir anotaciones
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
                    plt.text(j, i, txt, ha='center', va='center',
                             fontsize=12, color=color, weight="bold")

        # Dibujar flechas para el camino principal
        if len(self.camino) > 1:
            for idx in range(len(self.camino)-1):
                y0, x0 = self.camino[idx][1], self.camino[idx][0]
                y1, x1 = self.camino[idx+1][1], self.camino[idx+1][0]
                plt.arrow(y0, x0, y1-y0, x1-x0,
                          head_width=0.2, head_length=0.2,
                          fc="purple", ec="purple", alpha=0.5)

        plt.title(f"Recorrido del {self.nombre} (A*)")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.xticks(np.arange(entorno.ancho))
        plt.yticks(np.arange(entorno.alto))
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    def animar_recorrido(self, entorno, ruta_gif="recorrido_astar.gif", ruta_mp4="recorrido_robot.mp4"):
        """Genera una animación del recorrido"""
        images = []
        temp_dir = "temp_frames"
        os.makedirs(temp_dir, exist_ok=True)

        # Crear frames individuales
        for paso in range(len(self.camino)):
            fig, ax = plt.subplots(figsize=(8, 8))

            # Dibujar entorno base
            grid = np.zeros((entorno.alto, entorno.ancho))
            for i in range(entorno.alto):
                for j in range(entorno.ancho):
                    if entorno.matriz[i][j] in entorno.simbolo_obstaculos:
                        grid[i, j] = -1
                        ax.text(j, i, "X", ha='center', va='center',
                                color='red', fontsize=12)
                    elif entorno.matriz[i][j] in entorno.objetos_disponibles:
                        grid[i, j] = 0.3
                        ax.text(j, i, "O", ha='center', va='center',
                                color='black', fontsize=12)

            # Dibujar camino recorrido hasta este paso
            for idx in range(paso + 1):
                i, j = self.camino[idx]
                if grid[i, j] == 0:
                    grid[i, j] = 0.6
                    if (i, j) in self.celdas_recolectadas:
                        ax.text(j, i, "R", ha='center', va='center',
                                color='orange', fontsize=12)
                    else:
                        ax.text(j, i, "·", ha='center', va='center',
                                color='black', fontsize=10)

            # Dibujar posición actual
            i, j = self.camino[paso]
            grid[i, j] = 1.0
            ax.text(j, i, str(paso+1), ha='center', va='center',
                    color='purple', fontsize=12, weight='bold')

            # Dibujar inicio
            if paso == 0:
                inicio = self.camino[0]
                ax.text(inicio[1], inicio[0], "INICIO", ha='center', va='center',
                        color='green', fontsize=10, weight='bold')

            ax.imshow(grid, cmap="YlGnBu", origin="upper")
            ax.set_title(
                f"Paso {paso+1} - Energía: {self.energia - paso if paso < self.energia else 0}")
            ax.set_xticks(np.arange(entorno.ancho))
            ax.set_yticks(np.arange(entorno.alto))
            ax.grid(True, alpha=0.3)

            # Guardar frame
            frame_path = os.path.join(temp_dir, f"frame_{paso:03d}.png")
            plt.savefig(frame_path)
            plt.close()
            images.append(imageio.imread(frame_path))

        # Crear GIF
        imageio.mimsave(ruta_gif, images, duration=0.5)
        print(f"✅ GIF guardado como: {ruta_gif}")

        # Crear video MP4
        imageio.mimsave(ruta_mp4, images, format='mp4', fps=2)
        print(f"✅ Video MP4 guardado como: {ruta_mp4}")

        # Limpiar frames temporales
        for img in os.listdir(temp_dir):
            os.remove(os.path.join(temp_dir, img))
        os.rmdir(temp_dir)

    def resumen_final(self):
        """Muestra un resumen estadístico de la ejecución"""
        self.log.append("\n=== RESUMEN FINAL ===")
        self.log.append(f"Posición final: {self.posicion}")
        self.log.append(f"Energía restante: {self.energia}")
        self.log.append(f"Celdas exploradas: {len(self.memoria)}")
        self.log.append(
            f"Obstáculos detectados: {len(self.obstaculos_memoria)}")
        self.log.append(f"Objetos recolectados: {self.objetos_recolectados}")
        print("\n".join(self.log))

    def exportar_log(self, ruta):
        """Exporta el registro de acciones a un archivo"""
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("\n".join(self.log))

import matplotlib.pyplot as plt
import imageio
import os
import numpy as np


class Graficador:
    def __init__(self):
        pass

    def graficar_barra_comparativa(self, nombres, pasos, energia, objetos):
        plt.figure(figsize=(10, 5))

        # Pasos dados
        plt.subplot(1, 2, 1)
        plt.bar(nombres, pasos, color=['purple', 'blue', 'orange'])
        plt.title("Pasos dados por algoritmo")
        plt.ylabel("Cantidad de pasos")
        for i, v in enumerate(pasos):
            plt.text(i, v+0.5, str(v), ha='center')

        # Objetos recolectados
        plt.subplot(1, 2, 2)
        plt.bar(nombres, objetos, color=['purple', 'blue', 'orange'])
        plt.title("Objetos recolectados por algoritmo")
        plt.ylabel("Objetos recolectados")
        for i, v in enumerate(objetos):
            plt.text(i, v+0.5, str(v), ha='center')

        plt.tight_layout()
        plt.show()

    def mostrar_mapa(self, entorno, camino=None, titulo="Mapa del entorno"):
        grid = np.zeros((entorno.alto, entorno.ancho))
        # Marca obstáculos y objetos
        for i in range(entorno.alto):
            for j in range(entorno.ancho):
                if entorno.matriz[i][j] == entorno.simbolo_obstaculos:
                    grid[i, j] = -1
                elif entorno.matriz[i][j] == entorno.objetos_disponibles:
                    grid[i, j] = 0.5
        plt.figure(figsize=(6, 6))
        plt.imshow(grid, cmap="YlGnBu", origin="upper")
        if camino:
            for idx, (i, j) in enumerate(camino):
                plt.text(j, i, str(idx+1), va='center', ha='center',
                         color='orange', fontsize=12, weight='bold')
        plt.title(titulo)
        plt.show()

    def crear_gif(self, camino, entorno, ruta_gif, color_camino="purple"):
        images = []
        temp_dir = "frames_temp"
        os.makedirs(temp_dir, exist_ok=True)
        for paso, (i, j) in enumerate(camino):
            grid = np.zeros((entorno.alto, entorno.ancho))
            # Obstáculos y objetos
            for x in range(entorno.alto):
                for y in range(entorno.ancho):
                    if entorno.matriz[x][y] == entorno.simbolo_obstaculos:
                        grid[x, y] = -1
                    elif entorno.matriz[x][y] == entorno.objetos_disponibles:
                        grid[x, y] = 0.3
            # Camino
            for idx in range(paso + 1):
                xi, yj = camino[idx]
                grid[xi, yj] = 0.6
            ini = camino[0]
            grid[ini[0], ini[1]] = 0.9
            grid[i, j] = 1.0
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.imshow(grid, cmap="YlGnBu", origin="upper")
            for x in range(entorno.alto):
                for y in range(entorno.ancho):
                    if entorno.matriz[x][y] == entorno.simbolo_obstaculos:
                        ax.text(y, x, "X", ha='center', va='center',
                                color='red', fontsize=14)
                    elif entorno.matriz[x][y]:
                        ax.text(y, x, "O", ha='center', va='center',
                                color='black', fontsize=14)
            ax.text(ini[1], ini[0], "INICIO", ha='center',
                    va='center', color='green', fontsize=12, weight='bold')
            ax.text(j, i, str(paso + 1), ha='center', va='center',
                    color=color_camino, fontsize=12, weight='bold')
            ax.set_title(f"Paso {paso+1}")
            plt.axis("off")
            frame_path = os.path.join(temp_dir, f"frame_{paso:03d}.png")
            plt.savefig(frame_path)
            plt.close(fig)
            images.append(imageio.imread(frame_path))
        imageio.mimsave(ruta_gif, images, duration=0.5)
        for img in os.listdir(temp_dir):
            os.remove(os.path.join(temp_dir, img))
        os.rmdir(temp_dir)
        print(f"✅ GIF guardado como: {ruta_gif}")


# Ejemplo de uso en main.py:
if __name__ == "__main__":
    # Suponiendo que ya tienes los resultados:
    nombres = ["DFS", "BFS", "A*"]
    pasos = [40, 67, 9]
    energia = [0, 17, 29]
    objetos = [5, 10, 4]
    graficador = Graficador()
    graficador.graficar_barra_comparativa(nombres, pasos, energia, objetos)
    # graficador.mostrar_mapa(entorno, robot_astar.camino, titulo="Recorrido A*")
    # graficador.crear_gif(robot_astar.camino, entorno, "astar.gif", color_camino="orange")

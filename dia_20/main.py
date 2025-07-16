import copy
import random
import time
from entorno import Entorno
from robot_dfs import RobotDFS
from robot_bfs import RobotBFS
from robot_astar import RobotAStar
from graficar import Graficador

# 1. Fijar semilla y crear entornos idénticos para todos
random.seed(42)
entorno_base = Entorno(
    ancho=7, alto=7, cantidad_objetos=10, cantidad_obstaculos=12)
entorno1 = copy.deepcopy(entorno_base)
entorno2 = copy.deepcopy(entorno_base)
entorno3 = copy.deepcopy(entorno_base)

robots = [
    ("DFS", RobotDFS("DFS", posicion=(2, 2)), entorno1, "purple"),
    ("BFS", RobotBFS("BFS", posicion=(2, 2)), entorno2, "blue"),
    ("A*", RobotAStar("A*", posicion=(2, 2)), entorno3, "orange")
]

graficador = Graficador()
resultados = []

for nombre, robot, entorno, color in robots:
    print(f"Ejecutando {nombre}...")
    start = time.time()
    if nombre == "DFS":
        robot.explorar_dfs(entorno)
    elif nombre == "BFS":
        robot.explorar_bfs(entorno)
    else:
        robot.explorar_astar(entorno)
    tiempo = time.time() - start

    # Guardar el GIF del recorrido
    nombre_archivo = nombre.lower().replace("*", "star")
    ruta_gif = f"dia_20/recorrido_{nombre_archivo}.gif"
    graficador.crear_gif(robot.camino, entorno, ruta_gif, color_camino=color)

    resultados.append({
        "Algoritmo": nombre,
        "Pasos": len(robot.camino),
        "Energía": robot.energia,
        "Recolectados": len(robot.celdas_recolectadas),
        "Tiempo": f"{tiempo:.3f}s"
    })

# Crear la gráfica comparativa
nombres = [r['Algoritmo'] for r in resultados]
pasos = [r['Pasos'] for r in resultados]
energia = [r['Energía'] for r in resultados]
objetos = [r['Recolectados'] for r in resultados]
graficador.graficar_barra_comparativa(nombres, pasos, energia, objetos)

# Imprimir y guardar la tabla comparativa
print("\n| Algoritmo | Pasos | Energía | Objetos recolectados | Tiempo |")
print("|-----------|-------|---------|----------------------|--------|")
with open("dia_20/comparativa_algoritmos.md", "w") as f:
    f.write("| Algoritmo | Pasos | Energía | Objetos recolectados | Tiempo |\n")
    f.write("|-----------|-------|---------|----------------------|--------|\n")
    for r in resultados:
        print(
            f"| {r['Algoritmo']} | {r['Pasos']} | {r['Energía']} | {r['Recolectados']} | {r['Tiempo']} |")
        f.write(
            f"| {r['Algoritmo']} | {r['Pasos']} | {r['Energía']} | {r['Recolectados']} | {r['Tiempo']} |\n")

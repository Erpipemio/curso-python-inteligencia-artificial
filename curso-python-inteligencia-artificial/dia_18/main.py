from entorno import Entorno
from robot_bfs import RobotBFS
import os
import matplotlib.pyplot as plt

entorno = Entorno(ancho=5, alto=5, cantidad_objetos=7, cantidad_obstaculos=7)
robot = RobotBFS("RoboBFS", posicion=(2, 2))
entorno.mostrar()

robot.explorar_bfs(entorno)

robot.resumen_final()
entorno.mostrar()
robot.animar_recorrido(
    entorno,
    ruta_gif="dia_18/multimedia/recorrido_robot.gif",
    ruta_mp4="dia_18/multimedia/recorrido_robot.mp4"
)
os.makedirs("dia_18/log", exist_ok=True)
robot.exportar_log("dia_18/log/log_robot_bfs.txt")

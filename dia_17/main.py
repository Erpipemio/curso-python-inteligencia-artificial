from entorno import Entorno
from robot_dfs import RobotDFS
import os
import matplotlib.pyplot as plt

entorno = Entorno(ancho=5, alto=5, cantidad_objetos=7, cantidad_obstaculos=7)
robot = RobotDFS("RoboDFS", posicion=(2, 2))
entorno.mostrar()

robot.explorar_dfs(entorno)

robot.resumen_final()
robot.visualizar_recorrido(entorno)
robot.animar_recorrido(
    entorno,
    ruta_gif="dia_17/multimedia/recorrido_robot.gif",
    ruta_mp4="dia_17/multimedia/recorrido_robot.mp4"
)
entorno.mostrar()
os.makedirs("dia_17/log", exist_ok=True)
robot.exportar_log("dia_17/log/log_robot_dfs.txt")

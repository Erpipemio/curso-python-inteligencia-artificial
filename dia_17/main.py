from entorno import Entorno
from robot_dfs import RobotDFS
import os

entorno = Entorno(ancho=5, alto=5, cantidad_objetos=7, cantidad_obstaculos=7)
robot = RobotDFS("RoboDFS", posicion=(2, 2))
entorno.mostrar()

robot.explorar_dfs(entorno)

robot.resumen_final()
entorno.mostrar()
os.makedirs("dia_17/log", exist_ok=True)
robot.exportar_log("dia_17/log/log_robot_dfs.txt")

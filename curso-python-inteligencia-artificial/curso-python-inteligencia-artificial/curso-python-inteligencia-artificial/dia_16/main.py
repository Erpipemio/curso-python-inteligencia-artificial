from entorno import Entorno
from robot import Robot
import os

entorno = Entorno(ancho=5, alto=5, cantidad_objetos=6, cantidad_obstaculos=6)
robot = Robot("RoboObstaculos", posicion=(2, 2))
entorno.mostrar()
while robot.energia > 0:
    direccion = robot.decidir_movimiento(entorno)
    if direccion:
        robot.mover(direccion, entorno)

        # Recolectar automáticamente si hay objeto
        if entorno.matriz[robot.posicion[0]][robot.posicion[1]] in entorno.objetos_disponibles:
            robot.recolectar(entorno)
    else:
        print("¡No hay movimientos posibles!")
        break
robot.resumen_final()
entorno.mostrar()
os.makedirs("dia_16/log", exist_ok=True)
robot.exportar_log(
    "dia_16/log/log_robot_sensor_realista.txt")

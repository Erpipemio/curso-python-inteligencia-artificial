# dia_15/robot_sensor_realista/main.py

from entorno import Entorno
from robot import Robot
import os

# Crear entorno y robot
entorno = Entorno(ancho=5, alto=5, cantidad_objetos=7)
robot = Robot("RoboSensor", posicion=(2, 2))
entorno.mostrar()

# Simulación de exploración
while robot.energia > 0:
    visibles = robot.escanear_entorno(entorno)

    if visibles:
        # Si ve objetos cerca, elige el primero
        direccion, objeto = visibles[0]
        robot.mover(direccion)
        robot.recolectar(objeto, entorno)
    else:
        # Si no ve nada, explora inteligentemente
        direccion = robot.decidir_direccion_exploratoria()
        robot.mover(direccion)

# Mostrar resumen y guardar log

robot.resumen_final()
entorno.mostrar()
os.makedirs("dia_15/log/log", exist_ok=True)
robot.exportar_log(
    "dia_15/log/log_robot_sensor_realista.txt")

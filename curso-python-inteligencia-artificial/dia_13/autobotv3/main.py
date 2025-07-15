from objetos import Objeto
from robot import Robot
from entorno import Entorno
import random


def main():
    # Crear entorno
    entorno = Entorno(5, 5)

    # Crear objetos
    objetos = [
        Objeto("Batería", "Herramienta", 1.8),
        Objeto("Cable", "Repuesto", 0.5),
        Objeto("Sensor", "Componente", 1.5),
        Objeto("Tornillo", "Accesorio", 1.0),
        Objeto("Motor", "Repuesto", 2.0)
    ]

    # Colocar objetos en el entorno (aleatorio)
    for obj in objetos:
        entorno.colocar_objetos(obj)

    # Crear robot
    robot = Robot("DiegoBot", entorno)

    # Ejecutar simulación
    robot.ejecutar_ciclo()


if __name__ == "__main__":
    print("🚀 Iniciando simulación de robot inteligente...")
    main()
    print("🏁 Simulación completada.")

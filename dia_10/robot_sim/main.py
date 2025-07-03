from robot import Robot


def main():
    # Crear un robot
    robot = Robot("Robo1")

    # Mover el robot en diferentes direcciones
    robot.mover("norte")
    robot.mover("este")
    robot.mover("sur")
    robot.mover("oeste")

    # Mostrar la posición final del robot
    print(f"Posición final de {robot.nombre}: {robot.posicion}")


if __name__ == "__main__":
    main()
# Ejecutar el programa principal

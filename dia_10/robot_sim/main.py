from robot import Robot
from objetos import Objeto
from entorno import Entorno


def main():
    # Crear un robot
    robot = Robot("DiegoBot")

    # Crear algunos objetos
    objeto1 = Objeto("Batería", "Herramienta", 1)
    objeto2 = Objeto("Cable", "Repuesto", 0.5)
    objeto3 = Objeto("Sensor", "Componente", 0.2)
    objeto4 = Objeto("Tornillo", "Accesorio", 0.1)
    objeto5 = Objeto("Motor", "Repuesto", 2)

    # Crear un entorno y añadir objetos
    entorno = Entorno()
    entorno.colocar_objetos(objeto1)
    entorno.colocar_objetos(objeto2)
    entorno.colocar_objetos(objeto3)
    entorno.colocar_objetos(objeto4)
    entorno.colocar_objetos(objeto5)
    entorno.mostrar()

    # Simulación de movimientos y detección
    movimientos = ["norte", "este", "este", "sur", "oeste", "norte"]
    for movimiento in movimientos:
        robot.mover(movimiento)
        objeto_detectado = robot.detectar(entorno)
        if objeto_detectado:
            robot.recoger_objeto(objeto_detectado)
            entorno.mostrar()


print("🚀 Simulación de Robot Iniciada")
main()

from entorno import Entorno
from robot import Robot


def contar_objetos(entorno):
    total = 0
    for fila in entorno.matriz:
        for obj in fila:
            if obj:
                total += 1
    return total


entorno = Entorno(ancho=5, alto=5, cantidad_objetos=7)
robot = Robot("RoboLoto", posicion=(2, 2))

while robot.energia > 0:
    entorno.mostrar()
    print(f"🔋 Energía actual: {robot.energia:.1f}")
    print(f"🎯 Objetos restantes: {contar_objetos(entorno)}")

    objetivo = robot.decidir_objetivo(entorno)

    if not objetivo:
        print("✅ ¡No quedan objetos por recolectar!")
        break

    while robot.posicion != objetivo and robot.energia > 0:
        x_robot, y_robot = robot.posicion
        x_obj, y_obj = objetivo

        if x_robot < x_obj:
            robot.mover("sur")
        elif x_robot > x_obj:
            robot.mover("norte")
        elif y_robot < y_obj:
            robot.mover("este")
        elif y_robot > y_obj:
            robot.mover("oeste")

    if robot.posicion == objetivo:
        objeto = robot.detectar(entorno)
        if objeto:
            robot.recolectar(objeto, entorno)
    print("-" * 30)

robot.mostrar_bolsa()
print(f"⚡ Energía final: {robot.energia:.1f}")

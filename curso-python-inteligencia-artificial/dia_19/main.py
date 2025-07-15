from entorno import Entorno
from robot_astar import RobotAStar
import os
from datetime import datetime


def main():
    # Configuración inicial
    ancho, alto = 7, 7
    num_objetos, num_obstaculos = 7, 10
    pos_inicial = (0, 0)
    nombre_robot = "RoboAStar"

    # Directorios para guardar resultados
    base_dir = "curso-python-inteligencia-artificial/dia_19"
    log_dir = os.path.join(base_dir, "log")
    multimedia_dir = os.path.join(base_dir, "multimedia")

    # Crear directorios si no existen
    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(multimedia_dir, exist_ok=True)

    # Timestamp para nombres de archivo únicos
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    try:
        # 1. Inicialización del entorno y robot
        entorno = Entorno(
            ancho=ancho,
            alto=alto,
            cantidad_objetos=num_objetos,
            cantidad_obstaculos=num_obstaculos
        )
        robot = RobotAStar(nombre_robot, posicion=pos_inicial)

        print("\n=== ENTORNO INICIAL ===")
        entorno.mostrar()

        # 2. Ejecución de la exploración
        print("\n=== INICIANDO EXPLORACIÓN ===")
        robot.explorar_astar(entorno)

        # 3. Resultados finales
        print("\n=== RESULTADOS FINALES ===")
        robot.resumen_final()
        print("\n=== ENTORNO FINAL ===")
        entorno.mostrar()

        # 4. Guardado de logs
        log_path = os.path.join(log_dir, f"log_robot_astar_{timestamp}.txt")
        robot.exportar_log(log_path)
        print(f"\nLog guardado en: {log_path}")

        # 5. Visualización
        print("\nGenerando visualizaciones...")
        robot.visualizar_recorrido(entorno)

        # 6. Animación
        gif_path = os.path.join(
            multimedia_dir, f"recorrido_robot_{timestamp}.gif")
        mp4_path = os.path.join(
            multimedia_dir, f"recorrido_robot_{timestamp}.mp4")

        robot.animar_recorrido(
            entorno,
            ruta_gif=gif_path,
            ruta_mp4=mp4_path
        )
        print(f"Animaciones guardadas en:\n- {gif_path}\n- {mp4_path}")

    except Exception as e:
        print(f"\n❌ Error durante la ejecución: {str(e)}")
    finally:
        print("\n=== EJECUCIÓN COMPLETADA ===")


if __name__ == "__main__":
    main()

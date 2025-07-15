import datetime
import math
from objetos import Objeto


class Robot:
    def __init__(self, nombre, entorno):
        self.nombre = nombre
        self.entorno = entorno
        self.posicion = (0, 0)
        self.bolsa = []
        self.energia = 30.0  # Energía inicial suficiente
        self.visitados = set()  # Para evitar repetir celdas
        self.log = []
        self.pasos = 0

    def verificar_energia(self, consumo):
        if self.energia < consumo:
            print(f"❌ {self.nombre} no tiene suficiente energía para esta acción.")
            self.log.append(
                f"{self.nombre} no tiene suficiente energía para esta acción.")
            return False
        return True

    def decidir_objetivo(self):
        """Selecciona el objeto más cercano (distancia Manhattan)"""
        objetivos = self.entorno.obtener_posiciones_objetos()
        if not objetivos:
            return None

        # Calcular distancias desde la posición actual
        distancias = []
        for obj_pos in objetivos:
            dist = abs(obj_pos[0] - self.posicion[0]) + \
                abs(obj_pos[1] - self.posicion[1])
            distancias.append((dist, obj_pos))

        # Ordenar por distancia (más cercano primero)
        distancias.sort()
        return distancias[0][1]

    def mover_hacia(self, destino):
        """Mueve el robot paso a paso hacia el destino"""
        x_robot, y_robot = self.posicion
        x_dest, y_dest = destino

        # Determinar dirección
        dx = x_dest - x_robot
        dy = y_dest - y_robot

        # Mover en la dirección de mayor diferencia primero
        if abs(dx) > abs(dy):
            direccion = "sur" if dx > 0 else "norte"
        else:
            direccion = "este" if dy > 0 else "oeste"

        self.mover(direccion)

    def mover(self, direccion):
        if not self.verificar_energia(1.0):
            return False

        x, y = self.posicion
        if direccion == "norte":
            x -= 1
        elif direccion == "sur":
            x += 1
        elif direccion == "este":
            y += 1
        elif direccion == "oeste":
            y -= 1

        # Asegurar que no salga del entorno
        x = max(0, min(x, self.entorno.alto - 1))
        y = max(0, min(y, self.entorno.ancho - 1))

        # Actualizar posición
        self.posicion = (x, y)
        self.visitados.add(self.posicion)
        self.energia -= 1.0
        self.pasos += 1
        print(
            f"🦾 {self.nombre} se movió a {self.posicion}. Energía restante: {self.energia:.1f}")
        self.log.append(
            f"{self.nombre} se movió a {self.posicion} en dirección {direccion}")
        return True

    def detectar(self):
        if not self.verificar_energia(0.5):
            return None

        objeto = self.entorno.get_objeto(self.posicion)
        self.energia -= 0.5
        if objeto:
            print(f"🔍 {self.nombre} detectó un objeto: {objeto}")
            self.log.append(f"{self.nombre} detectó un objeto: {objeto}")
            return objeto
        else:
            print(f"🔍 {self.nombre} no detectó nada en {self.posicion}")
            self.log.append(
                f"{self.nombre} no detectó nada en {self.posicion}")
            return None

    def recolectar(self):
        if not self.verificar_energia(2.0):
            return None

        objeto = self.entorno.get_objeto(self.posicion)
        if objeto:
            self.bolsa.append(objeto)
            self.entorno.remover_objeto(self.posicion)
            self.energia -= 3.0
            print(f"✅ {self.nombre} recolectó: {objeto}")
            self.log.append(f"{self.nombre} recolectó: {objeto}")
            return objeto
        return None

    def ejecutar_ciclo(self):
        """Ejecuta el ciclo principal de operación del robot"""
        while self.energia > 2.0 and self.entorno.objetos_disponibles:
            self.entorno.mostrar()
            objetivo = self.decidir_objetivo()

            if objetivo is None:
                print("🎉 ¡No quedan objetos por recolectar!")
                break

            # Mover hacia el objetivo hasta alcanzarlo
            while self.posicion != objetivo and self.energia > 2.0:
                self.mover_hacia(objetivo)

            # Si llegamos al objetivo y tenemos energía
            if self.posicion == objetivo and self.energia > 2.0:
                objeto_detectado = self.detectar()
                if objeto_detectado:
                    self.recolectar()

        # Mostrar resultados finales
        self.mostrar_bolsa()

    def mostrar_bolsa(self):
        print("\n=== Resumen final de la bolsa ===")

        # Usamos un diccionario para contar los objetos
        conteo = {}
        for item in self.bolsa:
            # Creamos una representación única de cadena para cada objeto
            clave = f"{item.nombre}|{item.tipo}|{item.peso}"
            conteo[clave] = conteo.get(clave, 0) + 1

        if not conteo:
            print("La bolsa está vacía.")
        else:
            for clave, cantidad in conteo.items():
                nombre, tipo, peso = clave.split("|")
                print(f"- {nombre} ({tipo}, {peso}kg): {cantidad} unidad(es)")

        print(f"Total de ítems: {len(self.bolsa)}")
        print(f"⚡ Energía final: {self.energia:.1f}")
        self.log.append("Resumen final de la bolsa")

    def resumen_final(self):
        total_valor = sum(obj.peso for obj in self.bolsa)
        self.log.append("\n📦 Resumen Final:")
        self.log.append(f"Objetos recolectados: {len(self.bolsa)}")
        self.log.append(f"Valor total (peso acumulado): {total_valor}")
        self.log.append(f"Pasos dados: {self.pasos}")
        self.log.append(f"Energía restante: {self.energia}")

    def exportar_log(self, nombre_archivo="log_robot.txt"):
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            for linea in self.log:
                f.write(linea + "\n")
        print(f"📝 Log exportado a {nombre_archivo}")

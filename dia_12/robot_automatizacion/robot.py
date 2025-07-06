from entorno import Entorno
from objetos import Objeto
import datetime
import random


class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = (0, 0)
        self.bolsa = []
        self.log_file = "dia_12/robot_automatizacion/log.txt"
        self._init_log()
        self.energia = 10.0

    def _init_log(self):
        with open(self.log_file, "w") as f:
            f.write(
                f"=== Simulación iniciada: {datetime.datetime.now()} ===\n")
            f.write(f"Mapa inicial:\n{Entorno}\n\n")

    def _log_action(self, action):
        with open(self.log_file, "a") as f:
            f.write(f"{datetime.datetime.now()} - {action}\n")
            f.write(
                f"Posición: {self.posicion} | Energia: {self.energia} | Bolsa: {self.bolsa}\n")
            f.write(f"Mapa actual:\n{Entorno}\n\n")

    def verificar_energia(self, consumo):
        if self.energia < consumo:
            print(f"❌ {self.nombre} no tiene suficiente energía para esta acción.")
            self._log_action(
                f"{self.nombre} no tiene suficiente energía para esta acción.")
            return False
        return True

    def decidir_direccion(self, entorno):
        direcciones = {
            "norte": (-1, 0),
            "sur": (1, 0),
            "este": (0, 1),
            "oeste": (0, -1)
        }
        x, y = self.posicion
        for dir, (dx, dy) in direcciones.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < entorno.alto and 0 <= ny < entorno.ancho:
                objeto = entorno.matriz[nx][ny]
                if objeto:  # Si hay objeto en la celda vecina
                    print(
                        f"🎯 {self.nombre} decidió ir al {dir} porque detectó un objeto.")
                    self._log_action(
                        f"{self.nombre} decidió ir al {dir} porque detectó un objeto.")
                    return dir
        # Si no hay objetos alrededor, moverse aleatoriamente
        return random.choice(list(direcciones.keys()))
        self._log_action(
            f"{self.nombre} no encontró objetos cercanos, se moverá a una dirección aleatoria.")

    def mover(self, direccion):
        if not self.verificar_energia(1):
            return
        x, y = self.posicion
        if direccion == "norte":
            x -= 1
        elif direccion == "sur":
            x += 1
        elif direccion == "este":
            y += 1
        elif direccion == "oeste":
            y -= 1
        x = max(0, min(x, 4))
        y = max(0, min(y, 4))
        self.posicion = (x, y)
        self.energia -= 1
        print(
            f"🦾 {self.nombre} se movió a {self.posicion}. Energía restante: {self.energia:.1f}")
        self._log_action(
            f"{self.nombre} se movió a {self.posicion} energía restante: {self.energia:.1f}")

    def detectar(self, entorno):
        if not self.verificar_energia(0.5):
            return None
        self.energia -= 0.5
        objeto = entorno.get_objeto(self.posicion)
        if objeto:
            print(f"🔍 {self.nombre} detectó un objeto: {objeto}")
            self._log_action(f"{self.nombre} detectó un objeto: {objeto}")
            return objeto
        else:
            print(f"🔍 {self.nombre} no detectó nada.")
            print(f"⚡ Energía restante: {self.energia:.1f}")
            self._log_action(
                f"{self.nombre} no detectó nada., energía restante: {self.energia:.1f}")
            return None

    def recolectar(self, objeto, entorno):
        if not self.verificar_energia(2):
            return
        if objeto:
            self.bolsa.append(objeto)
            x, y = self.posicion
            self.energia -= 2
            entorno.matriz[x][y] = None  # Se retira el objeto del entorno
            self._log_action(f"{self.nombre} recolectó: {objeto}")
            self._log_action(
                f"{self.nombre} se retiro el: {objeto} del entorno")
            print(f"✅ {self.nombre} recolectó: {objeto}")
            print(f"⚡ Energía restante: {self.energia:.1f}")


def mostrar_bolsa(self):
    print("\n=== Resumen final ===")
    for item in set(self.bolsa):
        print(f"- {item}: {self.bolsa.count(item)}x")
    print(f"Total: {len(self.bolsa)} ítems")
    self._log_action("Resumen final de la bolsa")


Robot.mostrar_bolsa = mostrar_bolsa

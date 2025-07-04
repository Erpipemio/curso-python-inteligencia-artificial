from entorno import Entorno
from objetos import Objeto
import datetime


class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = (0, 0)
        self.bolsa = []
        self.log_file = "log.txt"
        self._init_log()

    def _init_log(self):
        with open(self.log_file, "w") as f:
            f.write(
                f"=== Simulación iniciada: {datetime.datetime.now()} ===\n")
            f.write(f"Mapa inicial:\n{Entorno}\n\n")

    def _log_action(self, action):
        with open(self.log_file, "a") as f:
            f.write(f"{datetime.datetime.now()} - {action}\n")
            f.write(f"Posición: {self.posicion} | Bolsa: {self.bolsa}\n")
            f.write(f"Mapa actual:\n{Entorno}\n\n")

    def mover(self, direccion):
        x, y = self.posicion
        if direccion == "norte":
            x -= 1
        elif direccion == "sur":
            x += 1
        elif direccion == "este":
            y += 1
        elif direccion == "oeste":
            y -= 1
        self._log_action(f"{self.nombre} se movió hacia {direccion}")

        # Limitar dentro de un mapa de 5x5
        x = max(0, min(x, 4))
        y = max(0, min(y, 4))

        self.posicion = (x, y)
        print(f"🤖 {self.nombre} se movió a {self.posicion}")

    def recoger_objeto(self, objeto):
        if objeto not in self.bolsa:
            self.bolsa.append(objeto)
            print(f"🤖 {self.nombre} recogió el objeto: {objeto}")
            self._log_action(f"{self.nombre} recogió el objeto: {objeto}")
        else:
            print(f"🤖 {self.nombre} ya tiene el objeto: {objeto}")
        self._log_action(f"{self.nombre} ya tiene el objeto: {objeto}")

    def detectar(self, entorno):
        objeto = entorno.get_objeto(self.posicion)
        if objeto:
            print(f"🔍 {self.nombre} detectó un objeto: {objeto}")
            self._log_action(f"{self.nombre} detectó un objeto: {objeto}")
            return objeto
        else:
            print(f"🔍 {self.nombre} no detectó nada.")
            self._log_action(f"{self.nombre} no detectó nada.")
            return None


def recolectar(self, objeto, entorno):
    if objeto:
        self.bolsa.append(objeto)
        x, y = self.posicion
        entorno.matriz[x][y] = None  # Se retira el objeto del entorno
        self._log_action(f"{self.nombre} recolectó: {objeto}")
        self._log_action(f"{self.nombre} se retiro el: {objeto} del entorno")
        print(f"✅ {self.nombre} recolectó: {objeto}")


def show_bag(self):
    print("\n=== Resumen final ===")
    for item in set(self.bolsa):
        print(f"- {item}: {self.bolsa.count(item)}x")
    print(f"Total: {len(self.bolsa)} ítems")
    self._log_action("Resumen final de la bolsa")

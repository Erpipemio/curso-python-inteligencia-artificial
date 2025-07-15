from entorno import Entorno
from objetos import Objeto
import datetime
import random


class Robot:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion
        self.energia = 30
        self.bolsa = []
        self.log = []
        self.pasos = 0

    def mover(self, direccion):
        x, y = self.posicion
        if self.energia < 1:
            print("⚠️ Sin energía para moverse.")
            return

        if direccion == "norte":
            self.posicion = (x - 1, y)
        elif direccion == "sur":
            self.posicion = (x + 1, y)
        elif direccion == "este":
            self.posicion = (x, y + 1)
        elif direccion == "oeste":
            self.posicion = (x, y - 1)

        self.energia -= 1
        self.pasos += 1
        self.log.append(
            f"🚶 Se movió al {direccion} → Pos: {self.posicion} | Energía: {self.energia}")
        print(
            f"🚶 {self.nombre} se movió al {direccion} → Pos: {self.posicion} | Energía: {self.energia}")

    def detectar(self, entorno):
        x, y = self.posicion
        return entorno.matriz[x][y]

    def recolectar(self, objeto, entorno):
        if self.energia >= 3:
            self.energia -= 3
            self.bolsa.append(objeto)
            entorno.matriz[self.posicion[0]][self.posicion[1]] = None
            print(f"🧲 {self.nombre} recolectó: {objeto}")
            self.log.append(
                f"🧲 Recolectó: {objeto} | Energía restante: {self.energia}")
        else:
            self.log.append("⚠️ Energía insuficiente para recolectar.")

    def mostrar_bolsa(self):
        print("📦 Objetos recolectados:")
        for obj in self.bolsa:
            print("  -", obj)

    def decidir_objetivo(self, entorno):
        mejor_objeto = None
        mejor_ratio = -1
        mejor_posicion = None

        for x in range(entorno.alto):
            for y in range(entorno.ancho):
                objeto = entorno.matriz[x][y]
                if objeto:
                    distancia = abs(
                        x - self.posicion[0]) + abs(y - self.posicion[1])
                    if distancia == 0:
                        distancia = 1
                    ratio = objeto.peso / distancia
                    if ratio > mejor_ratio:
                        mejor_ratio = ratio
                        mejor_objeto = objeto
                        mejor_posicion = (x, y)

        if mejor_objeto:
            print(
                f"📍 {self.nombre} eligió como objetivo: {mejor_objeto} en {mejor_posicion}")
            self.log.append(
                f"📍 Objetivo elegido: {mejor_objeto} en {mejor_posicion}")
        return mejor_posicion

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

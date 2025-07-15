import random
from collections import defaultdict


class Robot:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion
        self.energia = 20
        self.log = []

        # Sistema de memoria mejorado
        # {posicion: {"tipo": "objeto"/"vacio"/"obstaculo", "visitas": int}}
        self.memoria_celdas = defaultdict(dict)
        self.celdas_visitadas = set()
        self.ultima_direccion = None

        # Registramos la posición inicial
        self._actualizar_memoria(posicion, "vacio")

    def _actualizar_memoria(self, posicion, tipo_celda):
        """Actualiza la memoria con información sobre la celda"""
        if posicion not in self.memoria_celdas:
            self.memoria_celdas[posicion] = {"tipo": tipo_celda, "visitas": 0}

        self.memoria_celdas[posicion]["visitas"] += 1
        if tipo_celda != "vacio":  # Sobrescribe si encontramos algo interesante
            self.memoria_celdas[posicion]["tipo"] = tipo_celda

    def mover(self, direccion, entorno):
        x, y = self.posicion
        nueva_pos = {
            "norte": (x - 1, y),
            "sur": (x + 1, y),
            "este": (x, y + 1),
            "oeste": (x, y - 1)
        }.get(direccion, (x, y))

        # Validar límites del mapa
        if not (0 <= nueva_pos[0] < entorno.alto and 0 <= nueva_pos[1] < entorno.ancho):
            self.log.append(
                f"❌ Movimiento bloqueado hacia {direccion}: fuera de límites")
            return False

        celda = entorno.matriz[nueva_pos[0]][nueva_pos[1]]

        # Verificar obstáculos
        if celda in entorno.obstaculos:
            self._actualizar_memoria(nueva_pos, "obstaculo")
            self.log.append(
                f"🧱 Movimiento bloqueado hacia {direccion}: hay un obstáculo")
            return False

        # Movimiento válido
        self.posicion = nueva_pos
        self.energia -= 1
        self.ultima_direccion = direccion
        self.celdas_visitadas.add(nueva_pos)

        # Determinar tipo de celda para la memoria
        tipo = "vacio"
        if celda in entorno.objetos_disponibles:
            tipo = "objeto"
        self._actualizar_memoria(nueva_pos, tipo)

        self.log.append(
            f"🚶 Movido a {nueva_pos} ({direccion}) – Energía: {self.energia}")

        # Escanear automáticamente el nuevo entorno
        self.escanear_entorno(entorno)
        return True

    def escanear_entorno(self, entorno):
        x, y = self.posicion
        objetos_detectados = []

        # Escaneo de celdas adyacentes (4 direcciones)
        direcciones = {
            "norte": (x - 1, y),
            "sur": (x + 1, y),
            "este": (x, y + 1),
            "oeste": (x, y - 1)
        }

        for dir, (i, j) in direcciones.items():
            if 0 <= i < entorno.alto and 0 <= j < entorno.ancho:
                celda = entorno.matriz[i][j]

                if celda in entorno.obstaculos:
                    self._actualizar_memoria((i, j), "obstaculo")
                    self.log.append(
                        f"🧱 Obstáculo detectado al {dir} ({i},{j})")
                elif celda in entorno.objetos_disponibles:
                    self._actualizar_memoria((i, j), "objeto")
                    objetos_detectados.append((dir, celda))
                    self.log.append(
                        f"👀 Objeto {celda} detectado al {dir} ({i},{j})")
                else:
                    self._actualizar_memoria((i, j), "vacio")

        return objetos_detectados

    def decidir_movimiento(self, entorno):
        x, y = self.posicion
        direcciones = {
            "norte": (x - 1, y),
            "sur": (x + 1, y),
            "este": (x, y + 1),
            "oeste": (x, y - 1)
        }

        # Prioridad 1: Moverse hacia objetos conocidos no recolectados
        for dir, pos in direcciones.items():
            if pos in self.memoria_celdas and self.memoria_celdas[pos]["tipo"] == "objeto":
                # Verificar que aún esté allí
                if entorno.matriz[pos[0]][pos[1]] in entorno.objetos_disponibles:
                    return dir

        # Prioridad 2: Moverse a celdas no visitadas o menos visitadas
        celdas_validas = []
        for dir, pos in direcciones.items():
            # Verificar límites y obstáculos
            if not (0 <= pos[0] < entorno.alto and 0 <= pos[1] < entorno.ancho):
                continue
            if entorno.matriz[pos[0]][pos[1]] in entorno.obstaculos:
                continue

            # Preferir celdas no visitadas, luego las menos visitadas
            visitas = self.memoria_celdas.get(pos, {}).get("visitas", 0)
            celdas_validas.append((dir, pos, visitas))

        if celdas_validas:
            # Ordenar por menos visitadas primero
            celdas_validas.sort(key=lambda x: x[2])
            # Elegir aleatoriamente entre las 2 mejores opciones
            return random.choice([d for d, p, v in celdas_validas[:2]]) if len(celdas_validas) > 1 else celdas_validas[0][0]

        # Prioridad 3: Si todo está visitado, moverse aleatoriamente evitando obstáculos
        opciones_seguras = [dir for dir, pos in direcciones.items()
                            if (0 <= pos[0] < entorno.alto and
                                0 <= pos[1] < entorno.ancho and
                                entorno.matriz[pos[0]][pos[1]] not in entorno.obstaculos)]

        if opciones_seguras:
            return random.choice(opciones_seguras)

        return None  # No hay movimientos posibles

    def recolectar(self, entorno):
        x, y = self.posicion
        objeto = entorno.matriz[x][y]

        if objeto in entorno.obstaculos:
            self.log.append(
                f"🧱 ¡No se puede recolectar un obstáculo en ({x},{y})!")
            return False

        if objeto is None:
            self.log.append(f"⬜ No hay nada para recolectar en ({x},{y})")
            return False

        # Recolección exitosa
        entorno.matriz[x][y] = None
        self.energia += 2
        self._actualizar_memoria((x, y), "vacio")  # Actualizamos la memoria
        self.log.append(
            f"✅ Recolectado {objeto} en ({x},{y}) – Energía: {self.energia}")
        return True

    def resumen_final(self):
        self.log.append("\n--- RESUMEN FINAL ---")
        self.log.append(f"Posición final: {self.posicion}")
        self.log.append(f"Energía restante: {self.energia}")
        self.log.append(f"Celdas visitadas: {len(self.celdas_visitadas)}")

        # Estadísticas de memoria
        tipos = defaultdict(int)
        for datos in self.memoria_celdas.values():
            tipos[datos["tipo"]] += 1

        self.log.append(f"Memoria: {dict(tipos)}")
        self.log.append(
            f"Total registros en memoria: {len(self.memoria_celdas)}")
        print("\n".join(self.log))

    def exportar_log(self, ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("\n".join(self.log))

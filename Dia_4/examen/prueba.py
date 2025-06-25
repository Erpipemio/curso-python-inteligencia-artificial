# Escenario: Gestor de Inventario de Repuestos
# Crea una lista llamada repuestos_disponibles con al menos 5 repuestos distintos (strings).
# Crea un diccionario llamado inventario, donde:
# Las claves son los nombres de los repuestos
# Los valores son las cantidades disponibles (números enteros)
# Agrega un nuevo repuesto llamado "filtro de aire" con cantidad 5.
# Usa un set para representar un lote recibido:
# Muestra qué elementos del lote_nuevo no estaban en el inventario.
# Imprime un informe como este (usa un bucle):

repuestos_disponibles = ["bujías", "filtro de aceite",
                         "pastillas de freno", "aceite de motor", "filtro de combustible"]
inventario = {"bujías": 10, "filtro de aceite": 8, "pastillas de freno": 5,
              "aceite de motor": 12, "filtro de combustible": 7}
inventario["filtro de aire"] = 5
lote_nuevo = {"aceite", "filtro de aire", "filtro de aceite",
              "cadena", "bujías", "pastillas de freno"}
nuevos_repuestos = lote_nuevo - set(inventario.keys())
print("Informe de inventario:")
for repuesto, cantidad in inventario.items():
    print(f"{repuesto}: {cantidad} unidades")
print("Repuestos nuevos que no estaban en el inventario:", nuevos_repuestos)
# Imprime los repuestos disponibles
print("Repuestos disponibles:", repuestos_disponibles)

from inventario import inventario

print(" Repuestos disponibles:")
for repuesto, cantidad in inventario.items():
    print(f"- {repuesto}: {cantidad} unidades")

pedido_input = input("Ingresa tu pedido separado por comas: ")
pedido = [p.strip().lower() for p in pedido_input.split(",")]

pedido_set = set(pedido)
disponibles = pedido_set & set(inventario.keys())
no_disponibles = pedido_set - disponibles

print(" Repuestos que se pueden entregar:")
for item in disponibles:
    print(f"- {item}")

print("Repuestos no disponibles:")
for item in no_disponibles:
    print(f"- {item}")

    for item in disponibles:
        inventario[item] -= 1
        if inventario[item] < 0:
            inventario[item] = 0

print("Inventario actualizado:")
for item, cantidad in inventario.items():
    print(f"- {item}: {cantidad} unidades")

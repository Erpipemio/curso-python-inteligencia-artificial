from utilidades import mostrar_productos, calcular_total, aplicar_descuento

productos = {
    "bujía": 3.5,
    "aceite": 6.0,
    "cadena": 12.0,
    "batería": 18.0,
    "pastillas de freno": 7.5
}

pedido = {}

# Mostrar productos
mostrar_productos(productos)

# Recibir pedido del usuario
print("\n📝 Ingresa tu pedido (máx 3 productos):")
for i in range(3):
    nombre = input(f"Producto #{i+1}: ").strip().lower()
    if nombre in productos:
        try:
            cantidad = int(input(f"Cantidad de {nombre}: "))
            pedido[nombre] = cantidad
        except ValueError:
            print("❌ ¡Debe ser un número entero!")
    else:
        print(f"❌ '{nombre}' no está disponible. Productos válidos:")
        mostrar_productos(productos)

# Calcular total
total_sin_descuento = calcular_total(productos, pedido)
total_final = aplicar_descuento(total_sin_descuento)

# Mostrar resumen
print("\n🧾 RESUMEN DE COMPRA:")
for producto, cantidad in pedido.items():
    subtotal = productos[producto] * cantidad
    print(
        f"- {producto}: {cantidad} x ${productos[producto]:.2f} = ${subtotal:.2f}")

print(f"\n💰 Total sin descuento: ${total_sin_descuento:.2f}")

if total_final < total_sin_descuento:
    ahorro = total_sin_descuento - total_final
    print(f"🎉 Descuento aplicado: ${ahorro:.2f} (10%)")

print(f" Total a pagar: ${total_final:.2f}")

from lectura_archivo import cargar_productos_desde_archivo

# Cargar productos desde archivo .txt
productos = cargar_productos_desde_archivo("dia_7/archivo.txt")

# Ruta del archivo de historial
registro = "dia_7/registro.txt"

# Mostrar todos los productos y precios


def mostrar_productos():
    print("\n🛒 PRODUCTOS DISPONIBLES:")
    for nombre, precio in productos.items():
        print(f"• {nombre} - ${precio}")

# Registrar una venta


def registrar_venta():
    producto = input("Ingrese el producto vendido: ").strip().lower()
    if producto not in productos:
        print("❌ Producto no encontrado.")
        return

    try:
        cantidad = int(input("Ingrese la cantidad vendida: "))
        if cantidad <= 0:
            print("❌ Cantidad inválida.")
            return
    except ValueError:
        print("❌ Solo se permiten números.")
        return

    total = productos[producto] * cantidad

    with open(registro, "a") as archivo:
        archivo.write(f"Producto: {producto}\n")
        archivo.write(f"Cantidad: {cantidad}\n")
        archivo.write(f"Total: {total}\n")
        archivo.write("---\n")

    print(f"✅ Venta registrada: {producto} x{cantidad} = ${total}")

# Ver historial de ventas


def ver_historial():
    try:
        with open(registro, "r") as archivo:
            contenido = archivo.read()
            print("\n📄 HISTORIAL DE VENTAS:")
            print(contenido if contenido else "Aún no hay ventas registradas.")
    except FileNotFoundError:
        print("⚠️ No existe historial todavía.")

# Menú principal


def mostrar_menu():
    while True:
        print("\n==== MENÚ PRINCIPAL ====")
        print("1. Mostrar productos")
        print("2. Registrar venta")
        print("3. Ver historial de ventas")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            registrar_venta()
        elif opcion == "3":
            ver_historial()
        elif opcion == "4":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida.")


# Ejecutar menú
mostrar_menu()

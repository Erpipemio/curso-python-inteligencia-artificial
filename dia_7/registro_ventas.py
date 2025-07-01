from lectura_archivo import cargar_productos_desde_archivo

productos = cargar_productos_desde_archivo("dia_7/archivo.txt")
registro = "dia_7/registro.txt"


def registrar_venta(producto, cantidad):
    if producto not in productos:
        print("❌ Producto no encontrado.")
        return

    total = productos[producto] * cantidad

    with open(registro, "a") as archivo:
        archivo.write(f"Producto: {producto}\n")
        archivo.write(f"Cantidad: {cantidad}\n")
        archivo.write(f"Total: {total}\n")
        archivo.write("---\n")

    print("✅ Venta registrada.")


# Prueba de venta
producto = input("¿Qué producto vendiste?: ").strip().lower()
cantidad = int(input("¿Cuántos?: "))
registrar_venta(producto, cantidad)

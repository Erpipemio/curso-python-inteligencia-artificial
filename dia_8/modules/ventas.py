def registrar_venta(productos, archivo_registro):
    producto = input("Producto vendido: ").strip().lower()
    if producto not in productos:
        print("❌ Producto no encontrado.")
        return

    try:
        cantidad = int(input("Cantidad: "))
        if cantidad <= 0:
            print("❌ Cantidad inválida.")
            return
    except ValueError:
        print("❌ Solo se permiten números.")
        return

    total = productos[producto] * cantidad

    with open(archivo_registro, "a") as archivo:
        archivo.write(f"Producto: {producto}\n")
        archivo.write(f"Cantidad: {cantidad}\n")
        archivo.write(f"Total: {total}\n")
        archivo.write("---\n")

    print(f"✅ Venta registrada: {producto} x{cantidad} = ${total}")

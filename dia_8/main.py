from modules.productos import cargar_productos
from modules.ventas import registrar_venta
from config import ARCHIVO_PRODUCTOS, ARCHIVO_REGISTRO

productos = ARCHIVO_PRODUCTOS
registro = ARCHIVO_REGISTRO

productos = cargar_productos(ARCHIVO_PRODUCTOS)


def mostrar_productos():
    print("\n📦 Productos disponibles:")
    for nombre, precio in productos.items():
        print(f"• {nombre}: ${precio}")


def ver_historial():
    try:
        with open(ARCHIVO_REGISTRO, "r", encoding="utf-8") as archivo:
            print("\n🧾 HISTORIAL DE VENTAS:")
            print(archivo.read() or "Aún no hay ventas.")
    except FileNotFoundError:
        print("⚠️ El archivo de historial no existe.")


def mostrar_menu():
    while True:
        print("\n==== MENÚ PRINCIPAL ====")
        print("1. Mostrar productos")
        print("2. Registrar venta")
        print("3. Ver historial")
        print("4. Salir")

        opcion = input("Opción (1-4): ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            registrar_venta(productos, ARCHIVO_REGISTRO)
        elif opcion == "3":
            ver_historial()
        elif opcion == "4":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")


mostrar_menu()

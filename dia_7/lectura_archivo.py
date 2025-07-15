def cargar_productos_desde_archivo(nombre_archivo):
    productos = {}
    try:
        with open(nombre_archivo, "r") as archivo:
            next(archivo)
            for linea in archivo:
                nombre, precio = linea.strip().split(",")
                productos[nombre] = float(precio)
        return productos
    except FileNotFoundError:
        print("❌ El archivo no existe.")
        return {}
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return {}


# Prueba del código
productos = cargar_productos_desde_archivo("dia_7/archivo.txt")
print("📦 Productos cargados:")
for nombre, precio in productos.items():
    print(f"- {nombre}: ${precio}")

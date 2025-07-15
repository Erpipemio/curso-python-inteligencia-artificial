def cargar_productos(nombre_archivo):
    productos = {}
    try:
        with open(nombre_archivo, "r") as archivo:
            next(archivo)  # Saltar cabecera
            for linea in archivo:
                nombre, precio = linea.strip().split(",")
                productos[nombre] = float(precio)
        return productos
    except FileNotFoundError:
        print("❌ El archivo no existe.")
        return {}

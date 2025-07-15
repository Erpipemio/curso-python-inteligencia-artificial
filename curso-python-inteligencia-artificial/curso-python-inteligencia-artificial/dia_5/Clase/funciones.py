# 🧩 Reto 1
# Crea una función saludar(nombre) que imprima:
# Hola, [nombre]. Bienvenido al sistema.

def saludar(nombre="usuario"):
    print(f"Hola, {nombre}. Bienvenido al sistema.")


saludar("Diego")
saludar()

# 🧩 Reto 2
# Crea una función doble(valor) que devuelva el doble del número que recibe.


def doble(valor):
    return valor * 2


print(doble(5))

# 🧩 Reto 3
# Crea una función calcular_total(precio, cantidad=1) que:
# Devuelva el precio total (precio × cantidad)
# Si no se da cantidad, debe ser 1 por defecto.


def calcular_total(precio, cantidad=1):
    return precio * cantidad


precio_total = calcular_total(100, 3)
print(precio_total)


# 🧩 Reto 4
# Usa las funciones anteriores en un script que:
# Salude al usuario.
# Le pida un producto y una cantidad.
# Calcule y muestre el total usando un precio fijo (por ejemplo: 3.5 por unidad).

def main():
    saludar("Diego")

    producto = input("Introduce el nombre del producto: ")
    cantidad = int(input(f"¿Cuántos {producto}s quieres? "))

    precio_unitario = 6.9
    total = calcular_total(precio_unitario, cantidad)

    print(f"El total por {cantidad} {producto}(s) es: {total} $")


if __name__ == "__main__":
    main()

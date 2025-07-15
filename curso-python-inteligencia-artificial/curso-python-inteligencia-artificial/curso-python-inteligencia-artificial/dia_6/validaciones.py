# Tareas prácticas
# 🧩 Reto 1 – Validar edad
# Solicita al usuario su edad. Si no es número, muestra un mensaje de error. Si es menor de 18, niega acceso.

# 🧩 Reto 2 – Divisiones seguras
# Solicita dos números y realiza la división. Si el divisor es 0, muestra un mensaje claro.

# 🧩 Reto 3 – Pedido seguro
# Integra esto al proyecto anterior:
# Si el usuario escribe una cantidad no numérica o negativa, vuelve a preguntarle.
# 👉 Usa un bucle while True con try/except para hacerlo elegante.

def validar_edad():
    try:
        edad = int(input("Por favor, introduce tu edad: "))
        if edad < 18:
            print("Acceso denegado. Debes ser mayor de 18 años.")
        else:
            print("Acceso permitido.")
    except ValueError:
        print("Error: Debes introducir un número válido.")


print("Reto 1 - Validar edad")
validar_edad()


def division_segura():
    try:
        num1 = float(input("Introduce el numerador: "))
        num2 = float(input("Introduce el divisor: "))
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except ValueError:
        print("Error: Debes introducir números válidos.")


print("\nReto 2 - Divisiones seguras")
division_segura()


def pedido_seguro():
    while True:
        try:
            cantidad = float(input("Introduce la cantidad del pedido: "))
            if cantidad < 0:
                print("Error: La cantidad no puede ser negativa. Inténtalo de nuevo.")
                continue
            print(f"Pedido realizado por una cantidad de: {cantidad}")
            break
        except ValueError:
            print("Error: Debes introducir un número válido.")


print("\nReto 3 - Pedido seguro")
pedido_seguro()

# Fin de los retos


def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Solo se permiten números.")

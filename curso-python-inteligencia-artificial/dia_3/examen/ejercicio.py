# Simula un cajero automático muy básico que permita:
# Iniciar con un saldo de $100.
# Mostrar un menú en bucle con las opciones:
# 1. Ver saldo
# 2. Depositar dinero
# 3. Retirar dinero
# 4. Salir
# Usar while para repetir hasta que el usuario elija salir.
# Validar que:
# No se pueda retirar más dinero del que hay.
# El monto sea positivo.
# Mostrar el mensaje correspondiente para cada acción.

print("Bienvenido al cajero automático")
saldo = 100
while True:
    print("\nMenú:")
    print("1. Ver saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print(f"Saldo actual: ${saldo}")

    elif opcion == "2":
        monto = float(input("Ingrese el monto a depositar: "))
        if monto > 0:
            saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
        else:
            print("El monto debe ser positivo.")

    elif opcion == "3":
        monto = float(input("Ingrese el monto a retirar: "))
        if monto > 0:
            if monto <= saldo:
                saldo -= monto
                print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
            else:
                print("No se puede retirar más dinero del que hay.")
        else:
            print("El monto debe ser positivo.")

    elif opcion == "4":
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        break

    else:
        print("Opción no válida, por favor intente de nuevo.")

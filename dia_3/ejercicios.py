# Ejercicio A – Contador simple
# Imprime los números del 1 al 10 usando un bucle for.

contador = 0
for i in range(1, 11):
    contador += 1
print(contador)

# Ejercicio B – Suma acumulada
# Pide al usuario que ingrese 5 números (uno por uno).
# Al final, muestra la suma total de esos números usando un for.

numero = int(input("Ingrese un número: "))
for i in range(4):
    numero += int(input("Ingrese otro número: "))
print("La suma total es:", numero)

# Ejercicio C – Menú interactivo con while
# Haz un menú que se repita hasta que el usuario escriba "salir". Algo como:

opcion = ""
while opcion != "3":
    opcion = input("escribe una opcion (1, 2, 3): ")
    if opcion == "1":
        print("Hola")
    elif opcion == "2":
        print("Me llamo Python")
    elif opcion == "3":
        print("Hasta luego")
        exit()
    else:
        print("Opción inválida")

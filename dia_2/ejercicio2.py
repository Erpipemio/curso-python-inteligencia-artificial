nota_de_exmen = input("¿Cuál es tu nota de examen? ")
if nota_de_exmen.isdigit():
    nota_de_exmen = int(nota_de_exmen)
    if 0 < nota_de_exmen <= 20:
        if nota_de_exmen <= 9:
            print("Reprobado")
        elif nota_de_exmen <= 13:
            print("regular")
        elif nota_de_exmen <= 16:
            print("Bueno")
        else:
            print("Excelente")
    else:
        print("Nota no válida, debe estar entre 0 y 20.")

age = input("¿Cuál es tu edad? ")
license = input("¿Tienes licencia de conducir? (si/no) ")
if age.isdigit():
    age = int(age)
    if age >= 18 and license.lower() == "si":
        print("Puedes conducir.")
    elif age >= 18 and license.lower() == "no":
        print("No puedes conducir porque no tienes licencia.")
    else:
        print("No puedes conducir porque eres menor de edad.")

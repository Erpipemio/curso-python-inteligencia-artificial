# Reto 1: Crear una clase Producto
# 📝 Tu desafío:
# 1. Crea una clase llamada Producto
# 2. Que tenga atributos: nombre, precio, stock
# 3. Que tenga un método vender(cantidad) que:
# 4. Reste esa cantidad al stock
# 5. Si no hay suficiente stock, que diga "Stock insuficiente"
# 6. Que tenga otro método mostrar_info() que muestre:
# Producto: aceite
# Precio: $6.5
# Stock: 15 unidades
# Ejemplo de uso esperado:
# p = Producto("aceite", 6.5, 10)
# p.vender(3)        # Vende 3
# p.mostrar_info()   # Stock: 7
# p.vender(10)       # Stock insuficiente

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad > self.stock:
            print("Stock insuficiente")
        else:
            self.stock -= cantidad
            print(
                f"Se han vendido {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}")

    def mostrar_info(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Stock: {self.stock} unidades")


aceite = Producto("aceite", 6.5, 10)
print("Antes de la venta:")
aceite.mostrar_info()
print()
aceite.vender(3)        # Vende 3
print("Después de la venta:")
aceite.mostrar_info()   # Stock: 7
print()
aceite.vender(10)       # Stock insuficiente
print("Después de intentar vender 10:")
aceite.mostrar_info()   # Stock sigue siendo 7

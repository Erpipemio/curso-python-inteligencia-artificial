class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self._validar_atributos()

    def _validar_atributos(self):
        """Valida todos los atributos al inicializar"""
        if not isinstance(self.nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto")
        if not isinstance(self.precio, (int, float)) or self.precio < 0:
            raise ValueError("El precio debe ser un número positivo")
        if not isinstance(self.stock, int) or self.stock < 0:
            raise ValueError("El stock debe ser un entero positivo")

    def vender(self, cantidad):
        """Intenta vender una cantidad del producto"""
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo")

        if cantidad > self.stock:
            print(f"❌ Stock insuficiente. Disponible: {self.stock}")
            return False

        self.stock -= cantidad
        print(f"✅ Vendidas {cantidad} unidades de {self.nombre}")
        return True

    def mostrar_info(self):
        """Muestra la información del producto formateada"""
        print(f"""
        {'='*30}
        Producto: {self.nombre}
        Precio: ${self.precio:.2f}
        Stock: {self.stock} unidades
        {'='*30}""")

    @property
    def necesita_reabastecer(self):
        """Indica si el producto necesita reposición"""
        return self.stock < 5


# Ejemplo de uso mejorado
if __name__ == "__main__":
    try:
        aceite = Producto("aceite", 6.5, 10)
        print("\n=== Información inicial ===")
        aceite.mostrar_info()

        print("\n=== Intentando vender ===")
        aceite.vender(3)
        aceite.vender(8)  # Debería fallar
        aceite.vender(4)

        print("\n=== Estado final ===")
        aceite.mostrar_info()

        if aceite.necesita_reabastecer:
            print("\n⚠️ Advertencia: Stock bajo, necesita reabastecimiento")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

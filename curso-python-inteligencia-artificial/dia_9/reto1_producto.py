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

    @property
    def necesita_reabastecer(self):
        """Indica si el producto necesita reposición"""
        print("Verificando si necesita reabastecer...")
        if self.stock < 5:
            return True
        return False

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
        if self.necesita_reabastecer:
            print("⚠️ Atención: El producto necesita reabastecerse.")
        else:
            print("✅ El producto tiene suficiente stock.")
        print("\nInformación del producto:")
        print(f"""
        {'='*30}
        Producto: {self.nombre}
        Precio: ${self.precio:.2f}
        Stock: {self.stock} unidades
        {'='*30}""")

        return self.stock < 5


class Carrito:
    def __init__(self):
        self._items = []  # Atributo interno con _

    @property
    def items(self):
        return self._items.copy()

    def agregar_producto(self, producto, cantidad):
        """Agrega o actualiza un producto en el carrito"""
        if not isinstance(producto, Producto):
            raise TypeError("Debe ser un objeto Producto")
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("Cantidad debe ser entero positivo")

        # Verificar si el producto ya está en el carrito
        for idx, (prod, cant) in enumerate(self._items):
            if prod.nombre == producto.nombre:
                if producto.vender(cantidad):
                    self._items[idx] = (prod, cant + cantidad)
                    print(
                        f"✅ Actualizadas {cantidad} unidades de {producto.nombre}")
                    return
                else:
                    print(f"❌ Stock insuficiente de {producto.nombre}")
                    return

        # Producto nuevo en el carrito
        if producto.vender(cantidad):
            self._items.append((producto, cantidad))
            print(f"✅ Añadido {cantidad} unidades de {producto.nombre}")
        else:
            print(f"❌ Stock insuficiente de {producto.nombre}")

    def eliminar_producto(self, nombre_producto, cantidad=1):
        """Elimina o reduce la cantidad de un producto"""
        for idx, (prod, cant) in enumerate(self._items):
            if prod.nombre == nombre_producto:
                if cantidad >= cant:
                    del self._items[idx]
                    print(f"🗑️ {nombre_producto} eliminado del carrito")
                else:
                    self._items[idx] = (prod, cant - cantidad)
                    print(
                        f"➖ Reducidas {cantidad} unidades de {nombre_producto}")
                return
        print(f"⚠️ {nombre_producto} no encontrado en el carrito")

    def mostrar_carrito(self):
        """Muestra el contenido del carrito con formato"""
        if not self._items:
            print("🛒 El carrito está vacío")
            return

        print("\n🛒 Contenido del carrito:")
        print("-" * 40)
        for producto, cantidad in self._items:
            print(f"├─ {producto.nombre}:")
            print(f"│  ├─ Cantidad: {cantidad}")
            print(f"│  └─ Subtotal: ${producto.precio * cantidad:.2f}")
        print("-" * 40)
        print(f"TOTAL: ${self.total_compra():.2f}\n")

    def total_compra(self):
        """Calcula el total de la compra"""
        return sum(producto.precio * cantidad for producto, cantidad in self._items)

    def vaciar_carrito(self):
        """Elimina todos los productos del carrito"""
        self._items.clear()
        print("🔄 Carrito vaciado")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear productos
    aceite = Producto("aceite", 6.5, 10)
    arroz = Producto("arroz", 2.0, 20)

    # Mostrar información de los productos
    aceite.mostrar_info()
    arroz.mostrar_info()

    # Vender productos
    aceite.vender(3)
    arroz.vender(5)

    # Crear carrito y agregar productos
    carrito = Carrito()
    carrito.agregar_producto(aceite, 2)
    carrito.agregar_producto(arroz, 3)

    # Mostrar contenido del carrito
    carrito.mostrar_carrito()

    # Eliminar un producto del carrito
    carrito.eliminar_producto("aceite", 1)
    carrito.mostrar_carrito()

    # Vaciar el carrito
    carrito.vaciar_carrito()

# Muestra los productos
def mostrar_productos(productos):
    if not productos:
        print("\n⚠️ No hay productos disponibles.")
        return

    print("\n📋 Lista de productos:")
    for nombre, precio in productos.items():
        print(f"- {nombre}: ${precio:.2f}")


def calcular_total(productos, pedido):
    """
    Calcula el total a pagar basado en un pedido.

    Args:
        productos (dict): Diccionario {producto: precio}.
        pedido (dict): Diccionario {producto: cantidad}.

    Returns:
        float: Total a pagar. Si un producto no existe, se ignora.
    """
    total = 0
    for producto, cantidad in pedido.items():
        if producto in productos:
            total += productos[producto] * cantidad
        else:
            print(f" Producto '{producto}' no encontrado. Se omitirá.")
    return total


def aplicar_descuento(total, umbral=30, porcentaje=0.1):
    """
    Aplica un descuento si el total supera un umbral.

    Args:
        total (float): Total a pagar.
        umbral (float): Mínimo para aplicar descuento (default: 30).
        porcentaje (float): % de descuento (default: 10%).

    Returns:
        float: Total con descuento (si aplica).
    """
    if not isinstance(total, (int, float)):
        raise ValueError("El total debe ser numérico.")

    return total * (1 - porcentaje) if total > umbral else total

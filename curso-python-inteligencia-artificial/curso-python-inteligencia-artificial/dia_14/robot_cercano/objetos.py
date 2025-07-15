from dataclasses import dataclass
from typing import Literal


@dataclass
class Objeto:
    """Representa un objeto que el robot puede recolectar en el entorno.

    Atributos:
        nombre (str): Nombre descriptivo del objeto
        tipo (Literal['Herramienta', 'Repuesto', 'Componente', 'Accesorio']): Categoría del objeto
        peso (float): Peso en kilogramos (debe ser positivo)
    """
    nombre: str
    tipo: Literal['Herramienta', 'Repuesto', 'Componente', 'Accesorio']
    peso: float

    def __post_init__(self):
        """Validación de los valores al crear el objeto"""
        if not isinstance(self.nombre, str) or len(self.nombre) < 2:
            raise ValueError(
                "El nombre debe ser un string de al menos 2 caracteres")
        if self.peso <= 0:
            raise ValueError("El peso debe ser un número positivo")

    def __str__(self):
        """Representación legible del objeto"""
        return f"{self.nombre} ({self.tipo}, {self.peso}kg)"

    def __eq__(self, other):
        """Comparación por igualdad basada en atributos"""
        if not isinstance(other, Objeto):
            return False
        return (self.nombre == other.nombre and
                self.tipo == other.tipo and
                abs(self.peso - other.peso) < 0.001)

    def info_corta(self):
        """Versión resumida para visualización en UI"""
        return f"{self.nombre[:10]:<10} | {self.tipo[:1]} | {self.peso:>4.1f}kg"

    def __hash__(self):
        return hash((self.nombre, self.tipo, round(self.peso, 3)))

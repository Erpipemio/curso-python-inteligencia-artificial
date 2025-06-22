from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Semana 1 - Ruta de IA: Python + Git + GitHub",
                  ln=True, align="C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 11)
        self.ln(4)
        self.cell(0, 10, title, ln=True, align="L")

    def chapter_body(self, body):
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 8, body)
        self.ln()


# Lista de contenidos
semana_1 = [
    {
        "titulo": "Dia 1 - Tu primer script en Python",
        "contenido": """
Temas: Variables, tipos de datos, entrada/salida, operadores

Videos:
- Dalto (min 0 a 21): https://www.youtube.com/watch?v=Kp4Mvapo5kc
- Pildoras Informaticas: https://www.youtube.com/watch?v=r-MjXJnrn84

Ejercicios:
- Hola mundo y calculadora basica
        """
    },
    {
        "titulo": "Dia 2 - Condicionales",
        "contenido": """
Temas: if, elif, else

Videos:
- Dalto (min 21 a 32): https://www.youtube.com/watch?v=Kp4Mvapo5kc&t=1260s
- Pildoras: https://www.youtube.com/watch?v=9J0-LQoxLrw

Ejercicio:
- Verifica si una persona puede conducir
        """
    },
    {
        "titulo": "Dia 3 - Bucles",
        "contenido": """
Temas: for, while, range

Videos:
- Dalto (32 a 46): https://www.youtube.com/watch?v=Kp4Mvapo5kc&t=1920s
- Pildoras: https://www.youtube.com/watch?v=k-jB78RSU8I

Ejercicio:
- Contador y verificador de numeros primos
        """
    },
    {
        "titulo": "Dia 4 - Estructuras de datos",
        "contenido": """
Temas: Listas, diccionarios, tuplas, sets

Videos:
- Dalto (46 a 1h05): https://www.youtube.com/watch?v=Kp4Mvapo5kc&t=2760s
- Pildoras: https://www.youtube.com/watch?v=mVYk3vMPjN4

Ejercicio:
- Lista de repuestos y diccionario de motos
        """
    },
    {
        "titulo": "Dia 5 - Funciones",
        "contenido": """
Temas: Definir funciones, argumentos, return

Videos:
- Dalto (desde 1h05): https://www.youtube.com/watch?v=Kp4Mvapo5kc&t=3900s
- Pildoras: https://www.youtube.com/watch?v=fvWvIWd6zLA

Ejercicio:
- Funcion que calcule IVA y si un numero es par o impar
        """
    },
    {
        "titulo": "Dia 6 - Proyecto de lista de tareas",
        "contenido": """
Proyecto:
- Agregar tareas
- Mostrar tareas
- Eliminar tareas

Video:
- Dalto - Menu consola: https://www.youtube.com/watch?v=rJt7TnN6-uQ
        """
    },
    {
        "titulo": "Dia 7 - Git & GitHub",
        "contenido": """
Temas: Comandos Git y uso de GitHub

Video:
- Git desde cero (Fazt): https://www.youtube.com/watch?v=HiXLkL42tMU

Tarea:
- Crear README.md y subir todo a GitHub
        """
    }
]

# Crear el PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

for dia in semana_1:
    pdf.chapter_title(dia["titulo"])
    pdf.chapter_body(dia["contenido"])

# Guardar el archivo en la misma carpeta
pdf.output("Semana_1_Ruta_IA.pdf")

import re
import csv
from pathlib import Path
import matplotlib.pyplot as plt


def extraer_metricas(path_log):
    with open(path_log, encoding="utf-8") as file:
        contenido = file.read()

    objetos = re.search(r"Objetos recolectados:\s*(\d+)", contenido)
    valor = re.search(r"Valor total \(peso acumulado\):\s*(\d+)", contenido)
    pasos = re.search(r"Pasos dados:\s*(\d+)", contenido)
    energia = re.search(r"Energía restante:\s*(\d+)", contenido)

    return {
        "Objetos": int(objetos.group(1)) if objetos else 0,
        "Valor total": int(valor.group(1)) if valor else 0,
        "Pasos": int(pasos.group(1)) if pasos else 0,
        "Energía": int(energia.group(1)) if energia else 0
    }


# Rutas de logs
log_valor = Path("dia_14/robot_valor/log/log_robot_valor_dia14.txt")
log_cercano = Path("dia_14/robot_cercano/log/log_robot_cercano.txt")

metrics_valor = extraer_metricas(log_valor)
metrics_cercano = extraer_metricas(log_cercano)

# Mostrar en consola
print("\n📊 COMPARACIÓN DE ROBOTS\n")
print(f"{'Métrica':<20} {'Robot Valor':<15} {'Robot Cercano':<15}")
print("-" * 50)
for clave in metrics_valor:
    print(
        f"{clave:<20} {metrics_valor[clave]:<15} {metrics_cercano[clave]:<15}")

# Exportar CSV
with open("dia_14/comparacion_resultados.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Métrica", "Robot Valor", "Robot Cercano"])
    for clave in metrics_valor:
        writer.writerow([clave, metrics_valor[clave], metrics_cercano[clave]])
print("\n✅ CSV exportado.")

# Visualización gráfica
metrica_labels = list(metrics_valor.keys())
valores_valor = list(metrics_valor.values())
valores_cercano = list(metrics_cercano.values())

x = range(len(metrica_labels))
bar_width = 0.35

plt.figure(figsize=(10, 6))
plt.bar([i - bar_width/2 for i in x], valores_valor,
        width=bar_width, label='Robot Valor')
plt.bar([i + bar_width/2 for i in x], valores_cercano,
        width=bar_width, label='Robot Cercano')

plt.xticks(ticks=x, labels=metrica_labels)
plt.ylabel('Cantidad / Puntaje')
plt.title('Comparación de Desempeño – Robot Valor vs. Cercano')
plt.legend()
plt.tight_layout()
plt.savefig("dia_14/comparacion_grafica.png")
plt.show()

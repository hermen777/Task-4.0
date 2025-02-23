import speedtest as st
import random
import math
import matplotlib.pyplot as plt
# para instalar speedtest use el comando pip install speedtest-cli
# para instalar random use el comando pip install random
# para instalar math use el comando pip install math
# para instalar matplotlib use el comando pip install matplotlib

# Función para medir la velocidad de internet
def Speed_Test():
    test = st.Speedtest()

    # Obtener valores reales
    down_speed = test.download() / 10**6  # Convertir a Mbps
    up_speed = test.upload() / 10**6      # Convertir a Mbps
    ping = test.results.ping              # Obtener ping en ms

    # Aplicar variabilidad aleatoria (±10%) usando math
    down_speed = round(down_speed * random.uniform(0.9, 1.1), 2)
    up_speed = round(up_speed * random.uniform(0.9, 1.1), 2)
    ping = round(ping * random.uniform(0.9, 1.1), 2)

    # Mostrar resultados en la terminal
    print(f"Velocidad de descarga: {down_speed} Mbps")
    print(f"Velocidad de subida: {up_speed} Mbps")
    print(f"Ping: {ping} ms")

    # Usamos matplotlib para crear un gráfico de barras
    etiquetas = ["Descarga (Mbps)", "Subida (Mbps)", "Ping (ms)"]
    valores = [down_speed, up_speed, ping]
    colores = ["blue", "green", "red"]

    # Configuración de la gráfica 
    plt.figure(figsize=(6, 4))  # Tamaño de la gráfica
    plt.bar(etiquetas, valores, color=colores)  # Crear gráfico de barras
    plt.ylabel("Valores")
    plt.title("Resultados de Speed Test")

    # Mostrar valores encima de las barras y usamos math para calcular la raíz cuadrada
    for i, v in enumerate(valores):
        plt.text(i, v + math.sqrt(v) * 0.1, f"{v}", ha="center", fontsize=12)

    # Guardar la imagen en formato PNG
    plt.savefig("speedtest_results.png", dpi=300)
    plt.show()

# Ejecutar la función
Speed_Test()
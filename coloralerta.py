import time
import random
from datetime import datetime
from colorama import init, Fore, Style

# Inicializar colorama (se necesita solo una vez)
init()

def obtener_temperatura():
    # Simulación de obtención de temperatura
    return random.uniform(0, 99)

def cambiar_estado(temp):
    # Simulación de cambio de estado basado en la temperatura
    if temp == 0:
        return "UNKNOW", Fore.BLACK
    elif temp <= 25:
        return "EXCELLENT", Fore.GREEN
    elif temp <= 45:
        return "GOOD", Fore.BLUE
    elif temp <= 65:
        return "WARNING", Fore.YELLOW
    elif temp <= 85:
        return "FAULTY", Fore.LIGHTRED_EX
    elif temp >= 100:
        return "KILLED", Fore.RED
    else:
        return "Funcionando con Normalidad"

def guardar_registro(registro, ruta):
    with open(ruta, 'a') as archivo_log:
        archivo_log.write(registro + '\n')

def imprimir_mensaje(mensaje, color):
    print(color + mensaje + Style.RESET_ALL)

def simulacion(dispositivo, ruta_log):
    for _ in range(15):  # Realizar 5 ciclos de simulación
        mission= ["OrbitOne", "GalaxyTwo", "ColonyMoon", "VacsMars"]
        device_type= "Servidor DELL XPS-420P"
        temperatura = obtener_temperatura()
        estado, color_estado = cambiar_estado(temperatura)
        registro = f"{datetime.now()} - Mision: {mission}, Tipo de dispositivo: {device_type}, Temperatura: {temperatura:.2f}°C, Estado: {estado}"
        guardar_registro(registro, ruta_log)
        imprimir_mensaje(registro, color_estado)
        time.sleep(2)  # Esperar 5 segundos entre cada registro

if __name__ == "__main__":
    dispositivo_simulado = "Dispositivo Simulado"
    ruta_preferencial_log = "simulacion.log"

    try:
        simulacion(dispositivo_simulado, ruta_preferencial_log)
    except KeyboardInterrupt:
        print("\nSimulación interrumpida.")

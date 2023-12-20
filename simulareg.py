import logging
import random
import time
from datetime import datetime

def configurar_logger(ruta_log):
    logging.basicConfig(filename=ruta_log, level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def simulacion_dispositivo(ruta_log):
    configurar_logger(ruta_log)

    # Parámetros iniciales
    estados_posibles = ["Apagado", "Funcionando normalmente", "Sobrecalentamiento", "Alta humedad"]
    temperatura_actual = 20.0
    humedad_actual = 50.0

    # Realizar simulación con un ciclo cada 20 segundos durante 5 ciclos
    for ciclo in range(5):
        # Cambiar de estado cada 20 segundos
        if ciclo % 4 == 0:
            nuevo_estado = random.choice(estados_posibles)
            logging.info("Ciclo %d: Cambio de estado - Nuevo estado: %s", ciclo + 1, nuevo_estado)

        # Simulación de cambios aleatorios en la temperatura y la humedad
        temperatura_actual += random.uniform(-1, 1)
        humedad_actual += random.uniform(-2, 2)

        # Imprimir estado actual en pantalla cada 5 segundos
        if (ciclo + 1) % 1 == 0:  # Cambiar a 5 para mostrar cada 5 segundos
            print(f"Ciclo {ciclo + 1}: Estado: {nuevo_estado if ciclo % 4 == 0 else 'Funcionando normalmente'}, "
                  f"Temperatura: {temperatura_actual:.2f}°C, Humedad: {humedad_actual:.2f}%")

        # Registrar el estado actual en el archivo de registro
        logging.info("Ciclo %d: Estado: %s, Temperatura: %.2f°C, Humedad: %.2f%%", ciclo + 1,
                     nuevo_estado if ciclo % 4 == 0 else 'Funcionando normalmente', temperatura_actual, humedad_actual)

        # Esperar 20 segundos antes del próximo ciclo
        time.sleep(20)

    # Devolver resultados al final de la simulación
    return {
        "estado_final": nuevo_estado if ciclo % 4 == 0 else 'Funcionando normalmente',
        "temperatura_final": temperatura_actual,
        "humedad_final": humedad_actual
    }

def main():
    ruta_preferencial_log = 'ruta_preferencial.log'
    print(f"Iniciando simulación del dispositivo. Resultados registrados en '{ruta_preferencial_log}'...")

    resultados_simulacion = simulacion_dispositivo(ruta_preferencial_log)

    # Mostrar resultados al final de la simulación
    print("\nResultados de la simulación:")
    print(f"Estado final: {resultados_simulacion['estado_final']}")
    print(f"Temperatura final: {resultados_simulacion['temperatura_final']:.2f}°C")
    print(f"Humedad final: {resultados_simulacion['humedad_final']:.2f}%")

if __name__ == "__main__":
    main()

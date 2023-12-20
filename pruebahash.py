import hashlib
from datetime import datetime


def obtener_datos_formulario():
    print("DILIGENCIAR FORMULARIO DE REGISTRO DEL DISPOSITIVO")
    fecha= input("Fecha: ")
    device_type= input("Tipo de Dispositivo: ")
    device_status= input("Estado del Dispositivo: ")
    #hash= input("")
    return {'fecha':fecha, 'device_type':device_type, 'device_status':device_status}

def generar_hash(datos):
    # genera un hash unico basado en los datos del formulario y la fecha actual
    timestamp= datetime.now().strftime("%Y-%m-%d %H-%M:%S")
    datos_concatenados=f"{datos['fecha']}_{datos['device_type']}_{datos['device_status']}_19{timestamp}"
    hash_generado= hashlib.sha256(datos_concatenados.encode()).hexdigest()
    return hash_generado

def almacenar_datos_log(datos, hash_generado):
    timestamp= datetime.now().strftime("%Y-%m-%d %H-%M:%S")
    log_entry= f"{timestamp} - Datos ingresados{datos}, Hash{hash_generado}\n"
    with open('form_con_hash.log', 'a') as log_file:
        log_file.write(log_entry)
        
def mostrar_resultados(datos, hash_generado):
    print("\nDatos ingresados:")
    print("Fecha: ", datos['fecha'])
    print("Tipo de Dispositivo: ", datos['device_type'])
    print("Estado del Dispositivo: ", datos['device_status'])
    print("Hash: ", hash_generado)       
    
def main():
    formulario= obtener_datos_formulario()
    hash_generado= generar_hash(formulario)
    almacenar_datos_log(formulario, hash_generado)
    mostrar_resultados(formulario, hash_generado)
    print("Los resultados han sido almacenados en 'form_con_hash.log'.")
    
if __name__== "__main__":
    main()
import os

def limpiar_pantalla():
    if os.name== 'nt':
        os.system('cls')
    else:
        os.system('clear')    

def mostrar_menu():
    print("\n")
    print("----------MENU DE ACCESO APOLO 11--------")
    print("-----------------------------------------")
    print("1. opcion 1")
    print("2. opcion 2")
    print("3. opcion 3")
    print("4. opcion 4")
    print("5. salir")
    
def ejecutar_opcion(opcion):
    
    limpiar_pantalla()
    
    if opcion == 1:
        #print("\033[1;33m]Está ejecutando la opcion 1")
        print("\033[4;35;41m"+"Texto subr morado sobre blanco"+'\033[0;m') 
        # Aqui se agrega la logica correspondiente a la opcion
    elif opcion == 2:
          print("Está ejecutando la opcion 2")
        # Aqui se agrega la logica correspondiente a la opcion  
    elif opcion == 3:
          print("Está ejecutando la opcion 3")
        # Aqui se agrega la logica correspondiente a la opcion
    elif opcion == 4:
          print("Está ejecutando la opcion 4")
        # Aqui se agrega la logica correspondiente a la opcion
    elif opcion == 5:
          print("Está ejecutando la opcion 5")
        # Aqui se agrega la logica correspondiente a la opcion
    else:
        print("opcion no valida, ingrese de nuevo")  
        
        
def main():
    while True:
        mostrar_menu()
        try:
            opcion= int(input("Seleccione una opcion: "))
            ejecutar_opcion(opcion)
            if opcion == 5:
                break # Se rompe el bucle si la opcion es 5 (salir del menu)
            input("Presiona Enter para continuar...")
            limpiar_pantalla()
        except ValueError:
            print("Error: ingresar un numero valido")   
            
 
if __name__== "__main__":
    main()             
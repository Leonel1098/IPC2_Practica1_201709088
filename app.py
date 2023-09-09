from lista_piezas import lista_piezas
tablero_creado = lista_piezas()

def Creando_Tablero():
    print("")
    print("")
    print("=============================CONFIGURACIÓN TABLERO=================================")
    print("Por favor ingrese las dimensiones del tablero FilasxColumnas ")
    filas = input("Ingrese el alto del Tablero: ")
    columnas = input("Ingrese el ancho del Tablero: ")
    
    tablero_creado.recorrer_Tablero(int(filas),int(columnas))
    tablero_creado.filas = int(filas)
    tablero_creado.columnas = int(columnas)
    
    tablero_creado.recorrer_e_imprimir_lista()

  
    print("=============================CONFIGURACIÓN PIEZAS=================================")
    nueva_pieza = True
    while nueva_pieza:
        fila = input("Ingrese la fila en la que desea colocar la pieza: ")
        columna = input("Ingrese la columna en la que desea colocar la pieza: ")
        color = input("Ingrese el color que desea darle a la pieza: ")
        tablero_creado.actualizar_pieza(int(fila),int(columna),color)
        print("")
        print("")
        tablero_creado.imprimir_tablero()
        respuesta = input("Desea agregar otra pieza Y/N: ")
        print("")
        print("")
        if respuesta =="N" or respuesta =="n":
            nueva_pieza = False
    print("=============================FIN CONFIGURACIÓN PIEZAS=================================")
    tablero_creado.imprimir_tablero()
    print("=============================FIN CONFIGURACIÓN TABLERO=================================")
    print("")
    print("")
   

def Menu():
    while True:
        print("")
        print("---------------------------------------")
        print("---------- Tablero ---------")
        print("")
        print("1. Crear Tablero")
        print("2. Datos del Estudiante")
        print("3. Salir")
        opcion = input(" Elija una opción: ") 
        if opcion == "1":
            print("")
            Creando_Tablero()

        elif opcion == "2":
            print("")
            print("-------------Datos del Estudiante-----------")
            print("-Leonel Antonio González García \n", 
                  "-201709088 \n"
                  "-Introducción a la Programación y Computación 2 \n"
                  "- Sección C")
            print("---------------------------------------") 
            print("")
        
        elif opcion == "3":
            print("")
            print("Gracias, Regresa Pronto!")
            print("")
            break
        else:
            print("")
            print("Por favor selecciona una opción válida :)")
            

Menu()

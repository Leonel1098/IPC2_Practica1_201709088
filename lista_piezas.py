from nodo import nodo
from pieza import pieza
class lista_piezas:

    def __init__(self):
        self.primero = None
        self.columnas = 0
        self.filas = 0
        self.contador = 0
    
    def insertar_pieza(self,pieza):
        if self.primero is None:
            self.primero = nodo(pieza = pieza)
            self.contador +=1
        else:
            actual = self.primero 
            while actual.siguiente:
                  actual = actual.siguiente
            actual.siguiente = nodo(pieza = pieza)
            self.contador+=1
    
    def recorrer_e_imprimir_lista(self):
        print("")
        print("")
        actual = self.primero
        print("--------------------------")
        while actual != None:
                print(self.columnas)
                print("Fila: ",actual.pieza.fila,"Columna: ",actual.pieza.columna,"Color: ",actual.pieza.color)
                actual = actual.siguiente
        print("--------------------------")
        print("")
        print("")
                
    def recorrer_Tablero(self,filas,columnas):
        for i in range(1,filas+1):
         for j in range(1,columnas+1):
            self.insertar_pieza(pieza(i,j,"White"))
            
            

    def actualizar_pieza(self,fila,columna,color):
        actual=self.primero
        while actual != None:
            if actual.pieza.fila == fila and actual.pieza.columna == columna:
                actual.pieza.color=color
                print("Se pintó la pieza con éxito!")
                return
            actual = actual.siguiente
        print("La posición ingresada no Existe, pruebe con otra :=)")
  
    def devolver_color(self,fila,columna):
        actual = self.primero
        while actual != None:
            if actual.pieza.fila == fila and actual.pieza.columna == columna:
                return actual.pieza.color
            actual = actual.siguiente

    def imprimir_tablero(self):
        for i in range(1,self.filas+1):
            for j in range(1,self.columnas+1):
                print(self.devolver_color(i,j), end = " ")
                
        print("")
        print("")

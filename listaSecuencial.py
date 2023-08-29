import numpy as np
class Lista:
    __datos=None
    def __init__(self):
        self.__datos = np.array([])
        
    def insertar(self, elemento, posicion):
        if posicion <= len(self.__datos) and posicion>=0:
            self.__datos=np.insert(self.__datos,posicion, elemento)

    def suprimir(self, posicion):
        if posicion < len(self.__datos):
            self.__datos = np.delete(self.__datos,posicion)
        
        else:
            print("Índice fuera de rango")

    def recuperar(self, posicion):
        if posicion < len(self.__datos):
            return self.__datos[posicion]
        else:
            print("Índice fuera de rango")

    def buscar(self, elemento):
        i=0
        while i < len(self.__datos):
            if self.__datos[i]==elemento:
                return i
            i+=1
        else:
            return -1

    def primer_elemento(self):
        if len(self.__datos) > 0:
            return self.__datos[0]
        else:
            return None

    def ultimo_elemento(self):
        if len(self.__datos) > 0:
            return self.__datos[-1]
        else:
            return None

    def siguiente(self, posicion):
        if posicion < len(self.__datos) - 1:
            return posicion + 1
        else:
            return None

    def anterior(self, posicion):
        if posicion > 0:
            return posicion - 1
        else:
            return None

    def recorrer(self):
        return self.__datos

# Crear una instancia de la clase
mi_lista = Lista()

# Insertar elementos
mi_lista.insertar(10, 0)
mi_lista.insertar(20, 1)
mi_lista.insertar(30, 2)

# Suprimir elemento en posición 1
mi_lista.suprimir(1)

# Recuperar elemento en posición 1
print(mi_lista.recuperar(1))  # Imprimirá 30

# Buscar el índice del elemento 10
print(mi_lista.buscar(10))  # Imprimirá 0

# Obtener primer y último elemento
print(mi_lista.primer_elemento())  # Imprimirá 10
print(mi_lista.ultimo_elemento())  # Imprimirá 30

# Obtener posición siguiente y anterior
print(mi_lista.siguiente(0))  # Imprimirá 1
print(mi_lista.anterior(1))   # Imprimirá 0

# Recorrer la lista
print(mi_lista.recorrer())  # Imprimirá [10, 30]

class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    def getdato(self):
        return self.__dato
    
    def setsiguiente(self, objeto):
        self.__siguiente=objeto

    def getsiguiente(self):
        return self.__siguiente
    
class ListaConCursor:
    def __init__(self):
        self.__primero = None
        self.__cursor = None

    def Insertar(self, elemento):
        nuevo_nodo = Nodo(elemento)
        if self.__primero is None:
            self.__primero = nuevo_nodo
            self.__cursor = nuevo_nodo
        else:
            nuevo_nodo.setsiguiente(self.__cursor.getsiguiente())
            self.__cursor.setsiguiente(nuevo_nodo)

    def Suprimir(self):
        if self.__cursor is not None:
            actual = self.__primero
            anterior = None
            while actual != self.__cursor:
                anterior = actual
                actual = actual.getsiguiente()
            if anterior is not None:
                anterior.setsiguiente(self.__cursor.getsiguiente())
            else:
                self.__primero = self.__cursor.getsiguiente()
            self.__cursor = self.__cursor.getsiguiente()

    def Avanzar(self):
        if self.__cursor is not None and self.__cursor.getsiguiente() is not None:
            self.__cursor = self.__cursor.getsiguiente()

    def Retroceder(self):
        if self.__primero is not None and self.__cursor != self.__primero:
            actual = self.__primero
            while actual.getsiguiente() != self.__cursor:
                actual = actual.getsiguiente()
            self.__cursor = actual

    def Recuperar(self):
        if self.__cursor is not None:
            return self.__cursor.getdato()
        else:
            return None

    def Buscar(self, elemento):
        actual = self.__primero
        contador = 0
        while actual is not None:
            if actual.getdato() == elemento:
                return contador
            actual = actual.getsiguiente()
            contador += 1
        return -1

    def Recorrer(self):
        actual = self.__primero
        while actual is not None:
            print(actual.getdato())
            actual = actual.getsiguiente()

# Ejemplo de uso
mi_lista = ListaConCursor()
mi_lista.Insertar(1)
mi_lista.Insertar(2)
mi_lista.Insertar(3)

print("Recorrido de la lista:")
mi_lista.Recorrer()

print("Recuperar elemento del cursor:", mi_lista.Recuperar())
mi_lista.Avanzar()
print("Recuperar elemento después de avanzar:", mi_lista.Recuperar())
mi_lista.Retroceder()
print("Recuperar elemento después de retroceder:", mi_lista.Recuperar())

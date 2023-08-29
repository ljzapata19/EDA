class Nodo:
    __item = int()
    __sig = object
    
    def __init__(self, dato):
        self.__item = dato
        self.__sig = None
    
    def setSiguiente(self, sig):
        self.__sig = sig
    
    def getSiguiente(self):
        return self.__sig
    
    def getItem(self):
        return self.__item
    

class Pila:
    __tope = None
    
    def __init__(self):
        self.__tope = None
    
    def vacio(self):
        return self.__tope is None
    
    def insertar (self, valor):
        nueva_celda = Nodo(valor)
        nueva_celda.setSiguiente(self.__tope)
        self.__tope = nueva_celda
        
    def eliminar (self):
        if self.vacio():
            print('pila vacia')
            return None
        valor = self.__tope.getItem()
        self.__tope = self.__tope.getSiguiente()
        return valor
    
    def mostrar (self):
        if self.vacio():
            print('pila vacia')
        else:
            celda_actual=self.__tope
            while celda_actual:
                print(celda_actual.getItem())
                celda_actual = celda_actual.getSiguiente()

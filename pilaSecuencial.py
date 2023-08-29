import numpy as np
class Pila:
    __tope = int()
    __dim  = int()
    __arr = []
    
    def __init__(self, dim):
        self.__tope = 0
        self.__dim = dim
        self.__pila = np.empty(dim)
    
    def insertar(self, obj):
        if not self.pila_llena():
            self.__pila[self.__tope]=obj
            self.__tope+=1
        else:
            print('pila llena')
    
    def pila_llena(self):
        band=False
        if self.__tope == self.__dim:
            band = True
        return band
    
    def pila_vacia(self):
        band = False
        if self.__tope == -1:
            band = True
        return band
    
    def suprimir(self):
        if not self.pila_vacia():
            self.__tope = self.__tope-1
    

if __name__== '__main__':
    p = Pila(5)
    p.insertar(2)
    p.insertar(3)
    p.insertar(4)
    p.insertar(5)
    p.suprimir()
    p.insertar(6)
    p.insertar(7)
    
    

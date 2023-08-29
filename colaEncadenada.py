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

class Cola:
    __cant = int()
    __pri = None
    __ult = None
    
    def __init__(self):

        self.__cant = 0
    
    def vacia(self):
        return(self.__cant == 0)
    
    def insertar(self, x):
        p=Nodo(x)
        if self.__ult == None :
            self.__pri = p
        else:
            self.__ult.setSiguiente(p)
        self.__ult = p
        self.__cant +=1
        return self.__ult.getItem()
    
    def suprimir(self):
        if self.vacia():
            print('Cola Vacia')
            return (0)
        else:
            
            x= self.__pri.getItem()
            self.__pri = self.__pri.getSiguiente()
            self.__cant -= 1
            if self.vacia():
                self.__ult= None
            return (x)
    
    def getPri(self):
        return self.__pri
    
    def recorrer(self, aux):
        if aux != None:
            print(aux.getItem())
            self.recorrer(aux.getSiguiente())

'''
if __name__ == '__main__':
    cola=Cola()
    cola.insertar(1)
    cola.insertar(2)
    cola.insertar(3)
    cola.insertar(4)
    cola.insertar(5)
    cola.insertar(6)
    cola.recorrer(cola.getPri())
    sup=cola.suprimir()
    s=cola.suprimir()
    print('cola dsp de suprimir')
    cola.recorrer(cola.getPri())
'''
        

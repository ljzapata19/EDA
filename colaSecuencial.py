import numpy as np
class Cola:
    __pri= int()
    __ult= int()
    __cant= int()
    __max= int()
    __arreglo = []
    
    def __init__(self, xmax):
        self.__cant = 0
        self.__pri= 0
        self.__ult= 0
        self.__max = xmax
        self.__arreglo = np.empty(xmax)
    
    def vacia(self):
        return self.__cant==0
    
    def lleno(self):
        return self.__cant == self.__max
    
    def insertar(self, x):
        if self.__cant < self.__max:
            self.__arreglo[self.__ult]= x
            self.__ult = (self.__ult+1) % self.__max
            self.__cant +=1
            return x
        else:
            return (0)
    
    def suprimir(self):
        if self.vacia():
            print('Pila vacia')
            return (0)
        else:
            x= self.__arreglo[self.__pri]
            self.__pri = (self.__pri+1)% self.__max
            self.__cant -=1
            return (x)
    
    def recorrer (self):
        if not self.vacia():
            i=self.__pri
            
            for j in range(self.__cant):
                print (self.__arreglo[i])
                i= (i+1) % self.__max
                
if __name__ == '__main__':
    cola=Cola(5)
    cola.insertar(1)
    cola.insertar(2)
    cola.insertar(3)
    cola.insertar(4)
    cola.insertar(5)
    cola.insertar(6)
    cola.recorrer()
    cola.suprimir()
    cola.suprimir()
    print('cola dsp de suprimir')
    cola.recorrer()

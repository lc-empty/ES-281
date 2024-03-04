class Nodo:
    def __init__(self, dato):
        self.dato = dato;
        self.siguiente = None;

        
class ListaEnlazadaSimple:
    def __init__(self, dato):
        self.inicio = None;
        self.fin = Nonne;

    #  1. Eliminar por el primero de una lista enlazada
    def eliminarPrimero(self):
        if self.priemro =- None:
            return None;
        elif self.primero.enlace == None:
            self.primero = None;
        else:
            aux = self.primero;
            self.primero = aux.enlace;
            aux.enlace = None;

    #  2. Insertar después del dato buscado
    def insertarDBuscado(self, dato, datoB):
        nuevo = Nodo(dato);
        aux = self.primero;
        while aux.dato != datoB:
            aux = aux.enlace;
        nuevo.enalace = aux.enlace;
        aux.enlace = nuevo;

    #  3. Insertar al final de una lista simple
    def insertarFinal(self, dato):
        nuevo = Nodo(dato);
        if self.primero != None:
            aux = self.primero;
            while aux.enlace:
                aux = aux.enalce;
            aux.enlace = nuevo;
        else:
            self.primero = nuevo;

    #  4. Insertar un nodo en la primera posicion
    #  5. Insertar un dato antes de un Nodo
    #  6. Eliminar un elemento
    #  7. Eliminar un Nodo antes del Nodo buscado
    #  8. Eliminar el primer Nodo


class NodoDole:
    def __init__(self, dato):
        self.dato = dato;
        self.siguiente = None;
        self.anterior = None;


class ListaEnlazadaDoble:
    def __init__(self, dato):
        return;

    # 12.
    # 13.
    # 14.

class NodoCircular:
    def __init__(self, dato):
        self.dato = dato;
        self.siguiente = self;


class ListaEnlazdaCircular:
    def __init__(self, dato):
        self.dato = dato;

    #  9.
    # 10.
    # 11.

class Nodo:
    def __init__(self, dato):
        self.dato = dato;
        self.siguiente = None;


class ListaEnlazadaCircular:
    def __init__(self):
        self.primero = None;


    def insertarFinal(self, dato):
        nuevo_nodo = Nodo(dato);
        if self.primero is None:
            self.primero = nuevo_nodo;
            nuevo_nodo.siguiente = nuevo_nodo;
        else:
            nuevo_nodo.siguiente = self.primero;
            nodo_actual = self.primero;
            while nodo_actual.siguiente != self.primero:
                nodo_actual = nodo_actual.siguiente;
            nodo_actual.siguiente = nuevo_nodo;


    def imprimir(self):
        if self.primero is None:
            print("La lista está vacía")
        else:
            aux = self.primero
            while True:
                print(aux.dato, end=" ")
                aux = aux.siguiente
                if aux == self.primero:
                    break
            print()


# --- crear ---
lista = ListaEnlazadaCircular()
lista.insertarFinal(1)
lista.insertarFinal(2)
lista.insertarFinal(3)
lista.imprimir()


# --- agregar ---


# --- modificar ---


# --- eliminar ---




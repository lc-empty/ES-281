class Nodo:
    def __init__(self, dato):
        self.dato = dato;
        self.siguiente = None;


class ListaEnlazadaCircular:
    def __init__(self):
        self.primero = None;


    # Insertar/Agregar
    def insertarInicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            self.primero = nuevo_nodo


    def insertar(self, dato):
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


    # Mostrar
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


# # --- crear ---
lista = ListaEnlazadaCircular()
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.imprimir()


# --- agregar ---
lista.insertarInicio(0)
lista.imprimir()


# --- modificar ---


# --- eliminar ---


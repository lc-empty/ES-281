class Nodo:
    def __init__(self, dato):
        self.dato = dato;
        self.siguiente = None;
        self.anterior = None;


class ListaEnlazadaDoble:
    def __init__(self):
        self.primero = None;
        self.ultimo = None;

    
    def insertarFinal(self, dato):
        nuevo_nodo = Nodo(dato);
        if self.primero is None:
            self.primero = nuevo_nodo;
            self.ultimo = nuevo_nodo;
        else:
            self.ultimo.siguiente = nuevo_nodo;
            nuevo_nodo.anterior = self.ultimo;
            self.ultimo = nuevo_nodo;

    
    def insertarInicio(self, dato):
        nuevo_nodo = Nodo(dato);
        if self.primero is None:
            self.primero = nuevo_nodo;
            self.ultimo = nuevo_nodo;
        else:
            nuevo_nodo.siguiente = self.primero;
            self.primero.anterior = nuevo_nodo;
            self.primero = nuevo_nodo;


    def imprimir(self):
        if self.primero is None:
            print("La lista está vacía");
        else:
            aux = self.primero;
            while aux is not None:
                print(aux.dato, end=" ");
                aux = aux.siguiente;
            print();


# --- crear ---
lista_doble = ListaEnlazadaDoble();
lista_doble.insertarFinal(1);
lista_doble.insertarFinal(2);
lista_doble.insertarInicio(0);
lista_doble.imprimir();


# --- agregar ---


# --- modificar ---


# --- eliminar ---

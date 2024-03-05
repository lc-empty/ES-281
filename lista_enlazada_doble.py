class Nodo:
    def __init__(self, dato):
        self.dato = dato;
        self.siguiente = None;
        self.anterior = None;


class ListaEnlazadaDoble:
    def __init__(self):
        self.primero = None;
        self.ultimo = None;


    # Insertar/Agregar
    def insertarInicio(self, dato):
        nuevo_nodo = Nodo(dato);
        if self.primero is None:
            self.primero = nuevo_nodo;
            self.ultimo = nuevo_nodo;
        else:
            nuevo_nodo.siguiente = self.primero;
            self.primero.anterior = nuevo_nodo;
            self.primero = nuevo_nodo;
    

    def insertarAntes(self, dato, dato_buscado):
        nuevo_nodo = Nodo(dato);
        actual = self.primero;
        while actual is not None:
            if actual.dato == dato_buscado:
                nuevo_nodo.anterior = actual.anterior;
                actual.anterior = nuevo_nodo;
                if actual == self.primero:
                    self.primero = nuevo_nodo;
                else:
                    nuevo_nodo.anterior.siguiente = nuevo_nodo;
                nuevo_nodo.siguiente = actual;
                break;
            actual = actual.siguiente;
    

    def insertarDespues(self, dato, dato_buscado):
        nuevo_nodo = Nodo(dato);
        actual = self.primero;
        while actual is not None:
            if actual.dato == dato_buscado:
                nuevo_nodo.siguiente = actual.siguiente;
                actual.siguiente = nuevo_nodo;
                if actual == self.ultimo:
                    self.ultimo = nuevo_nodo;
                else:
                    nuevo_nodo.siguiente.anterior = nuevo_nodo;
                nuevo_nodo.anterior = actual;
                break;
            actual = actual.siguiente;

    
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato);
        if self.primero is None:
            self.primero = nuevo_nodo;
            self.ultimo = nuevo_nodo;
        else:
            self.ultimo.siguiente = nuevo_nodo;
            nuevo_nodo.anterior = self.ultimo;
            self.ultimo = nuevo_nodo;
    

    # Eliminar/quitar
    def eliminarPrimero(self):
        if self.primero is None:
            print("La lista está vacía");
            return;
        if self.primero == self.ultimo:
            self.primero = None;
            self.ultimo = None;
        else:
            self.primero = self.primero.siguiente;
            self.primero.anterior = None;


    def eliminarAntes(self, dato_buscado):
        if self.primero is None:
            print("La lista está vacía");
            return;
        actual = self.primero;
        while actual is not None:
            if actual.dato == dato_buscado:
                if actual == self.primero:
                    print("No hay un nodo anterior al primer nodo");
                    return;
                nodo_anterior = actual.anterior;
                if nodo_anterior == self.primero:
                    self.primero = actual;
                else:
                    nodo_anterior.anterior.siguiente = actual;
                actual.anterior = nodo_anterior.anterior;
                return;
            actual = actual.siguiente;
        print("El dato", dato_buscado, "no se encuentra en la lista");
    

    def eliminar(self, dato):
        if self.primero is None:
            print("La lista está vacía");
            return;
        actual = self.primero;
        while actual is not None:
            if actual.dato == dato:
                if actual == self.primero:
                    self.primero = actual.siguiente;
                    if self.primero is not None:
                        self.primero.anterior = None;
                    else:
                        self.ultimo = None;
                elif actual == self.ultimo:
                    self.ultimo = actual.anterior;
                    self.ultimo.siguiente = None;
                else:
                    actual.anterior.siguiente = actual.siguiente;
                    actual.siguiente.anterior = actual.anterior;
                return;
            actual = actual.siguiente;
        print("El dato", dato, "no se encuentra en la lista");
    

    def eliminarDespues(self, dato_buscado):
        if self.primero is None:
            print("La lista está vacía");
            return;
        actual = self.primero;
        while actual is not None:
            if actual.dato == dato_buscado:
                nodo_siguiente = actual.siguiente;
                if nodo_siguiente is None:
                    print("No hay un nodo después del último nodo");
                    return;
                actual.siguiente = nodo_siguiente.siguiente;
                if nodo_siguiente == self.ultimo:
                    self.ultimo = actual;
                else:
                    nodo_siguiente.siguiente.anterior = actual;
                return;
            actual = actual.siguiente;
        print("El dato", dato_buscado, "no se encuentra en la lista");
    

    def eliminarUltimo(self):
        if self.ultimo is None:
            print("La lista está vacía");
            return;
        if self.primero == self.ultimo:
            self.primero = None;
            self.ultimo = None;
        else:
            self.ultimo = self.ultimo.anterior;
            self.ultimo.siguiente = None;


    # Mostrar
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
lista_doble.insertar(3);
lista_doble.insertar(5);
lista_doble.insertarInicio(1);
lista_doble.imprimir();


# --- agregar ---
lista_doble.insertarAntes(2, 3);
lista_doble.insertarDespues(4, 3);
lista_doble.imprimir();


# --- modificar ---


# --- eliminar ---
lista_doble.eliminar(0);
lista_doble.eliminarAntes(3);
lista_doble.eliminarDespues(3);
lista_doble.eliminarPrimero();
lista_doble.eliminarUltimo();
lista_doble.imprimir();

class Nodo:
    def __init__(self, dato):
        self.dato = dato;
        self.siguiente = None;
        self.anterior = None;


class ListaEnlazadaDoble:
    def __init__(self):
        self.inicio = None;
        self.fin = None;


    # Insertar/Agregar
    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato);
        if self.inicio is None:
            self.inicio = nuevo_nodo;
            self.fin = nuevo_nodo;
        else:
            nuevo_nodo.siguiente = self.inicio;
            self.inicio.anterior = nuevo_nodo;
            self.inicio = nuevo_nodo;
    

    def insertar_antes(self, dato, dato_buscado):
        nuevo_nodo = Nodo(dato);
        actual = self.inicio;
        while actual is not None:
            if actual.dato == dato_buscado:
                nuevo_nodo.anterior = actual.anterior;
                actual.anterior = nuevo_nodo;
                if actual == self.inicio:
                    self.inicio = nuevo_nodo;
                else:
                    nuevo_nodo.anterior.siguiente = nuevo_nodo;
                nuevo_nodo.siguiente = actual;
                break;
            actual = actual.siguiente;
    

    def insertar_despues(self, dato, dato_buscado):
        nuevo_nodo = Nodo(dato);
        actual = self.inicio;
        while actual is not None:
            if actual.dato == dato_buscado:
                nuevo_nodo.siguiente = actual.siguiente;
                actual.siguiente = nuevo_nodo;
                if actual == self.fin:
                    self.fin = nuevo_nodo;
                else:
                    nuevo_nodo.siguiente.anterior = nuevo_nodo;
                nuevo_nodo.anterior = actual;
                break;
            actual = actual.siguiente;

    
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato);
        if self.inicio is None:
            self.inicio = nuevo_nodo;
            self.fin = nuevo_nodo;
        else:
            self.fin.siguiente = nuevo_nodo;
            nuevo_nodo.anterior = self.fin;
            self.fin = nuevo_nodo;
    

    # Modificar
    def modificar_primero(self, nuevo_dato):
        if self.inicio is not None:
            self.inicio.dato = nuevo_dato;


    def modificar_ultimo(self, nuevo_dato):
        if self.fin is not None:
            self.fin.dato = nuevo_dato;


    def modificar_antes(self, nodo_buscado, nuevo_dato):
        actual = self.inicio;
        while actual is not None:
            if actual.dato == nodo_buscado:
                if actual.anterior is not None:
                    actual.anterior.dato = nuevo_dato;
                break;
            actual = actual.siguiente;


    def modificar_despues(self, nodo_buscado, nuevo_dato):
        actual = self.inicio;
        while actual is not None:
            if actual.dato == nodo_buscado:
                if actual.siguiente is not None:
                    actual.siguiente.dato = nuevo_dato;
                break;
            actual = actual.siguiente;


    def modificar_nodo(self, nodo_a_modificar, nuevo_dato):
        actual = self.inicio
        while actual is not None:
            if actual.dato == nodo_a_modificar:
                actual.dato = nuevo_dato;
                break;
            actual = actual.nodo_siguiente;


    # Eliminar/quitar
    def eliminar_primero(self):
        if self.inicio is None:
            print("La lista está vacía");
            return;
        if self.inicio == self.fin:
            self.inicio = None;
            self.fin = None;
        else:
            self.inicio = self.inicio.siguiente;
            self.inicio.anterior = None;


    def eliminar_antes(self, dato_buscado):
        if self.inicio is None:
            print("La lista está vacía");
            return;
        actual = self.inicio;
        while actual is not None:
            if actual.dato == dato_buscado:
                if actual == self.inicio:
                    print("No hay un nodo anterior al primer nodo");
                    return;
                nodo_anterior = actual.anterior;
                if nodo_anterior == self.inicio:
                    self.inicio = actual;
                else:
                    nodo_anterior.anterior.siguiente = actual;
                actual.anterior = nodo_anterior.anterior;
                return;
            actual = actual.siguiente;
        print("El dato", dato_buscado, "no se encuentra en la lista");
    

    def eliminar(self, dato):
        if self.inicio is None:
            print("La lista está vacía");
            return;
        actual = self.inicio;
        while actual is not None:
            if actual.dato == dato:
                if actual == self.inicio:
                    self.inicio = actual.siguiente;
                    if self.inicio is not None:
                        self.inicio.anterior = None;
                    else:
                        self.fin = None;
                elif actual == self.fin:
                    self.fin = actual.anterior;
                    self.fin.siguiente = None;
                else:
                    actual.anterior.siguiente = actual.siguiente;
                    actual.siguiente.anterior = actual.anterior;
                return;
            actual = actual.siguiente;
        print("El dato", dato, "no se encuentra en la lista");
    

    def eliminar_despues(self, dato_buscado):
        if self.inicio is None:
            print("La lista está vacía");
            return;
        actual = self.inicio;
        while actual is not None:
            if actual.dato == dato_buscado:
                nodo_siguiente = actual.siguiente;
                if nodo_siguiente is None:
                    print("No hay un nodo después del último nodo");
                    return;
                actual.siguiente = nodo_siguiente.siguiente;
                if nodo_siguiente == self.fin:
                    self.fin = actual;
                else:
                    nodo_siguiente.siguiente.anterior = actual;
                return;
            actual = actual.siguiente;
        print("El dato", dato_buscado, "no se encuentra en la lista");
    

    def eliminar_ultimo(self):
        if self.fin is None:
            print("La lista está vacía");
            return;
        if self.inicio == self.fin:
            self.inicio = None;
            self.fin = None;
        else:
            self.fin = self.fin.anterior;
            self.fin.siguiente = None;


    # Mostrar
    def imprimir(self):
        if self.inicio is None:
            print("La lista está vacía");
        else:
            aux = self.inicio;
            while aux is not None:
                print(aux.dato, end=" ");
                aux = aux.siguiente;
            print();

# --- crear ---
lista_doble = ListaEnlazadaDoble();
lista_doble.insertar(3);
lista_doble.insertar(5);
lista_doble.insertar_inicio(1);
lista_doble.insertar(6);
lista_doble.insertar(7);
lista_doble.insertar(8);
lista_doble.imprimir();


# --- agregar ---
lista_doble.insertar_antes(2, 3);
lista_doble.insertar_despues(4, 3);
lista_doble.imprimir();


# --- modificar ---
lista_doble.modificar_primero(10);
lista_doble.modificar_ultimo(20);
lista_doble.modificar_antes(3, 12);
lista_doble.modificar_despues(4, 16);
lista_doble.imprimir();


# --- eliminar ---
lista_doble.eliminar(0);
lista_doble.eliminar_antes(3);
lista_doble.eliminar_despues(3);
lista_doble.eliminar_primero();
lista_doble.eliminar_ultimo();
lista_doble.imprimir();

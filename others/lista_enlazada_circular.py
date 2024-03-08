class Nodo:
    def __init__(self, dato):
        self.dato = dato;
        self.siguiente = None;


class ListaEnlazadaCircular:
    def __init__(self):
        self.primero = None;


    # Insertar/Agregar
    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato);
        if self.primero is None:
            self.primero = nuevo_nodo;
            nuevo_nodo.siguiente = nuevo_nodo;
        else:
            nuevo_nodo.siguiente = self.primero
            actual = self.primero;
            while actual.siguiente != self.primero:
                actual = actual.siguiente;
            actual.siguiente = nuevo_nodo;
            self.primero = nuevo_nodo;


    def insertar_antes(self, dato_buscado, dato_nuevo):
        if self.primero is None:
            print("La lista está vacía.");
            return;
        nuevo_nodo = Nodo(dato_nuevo);
        if self.primero.dato == dato_buscado:
            nuevo_nodo.siguiente = self.primero;
            actual = self.primero;
            while actual.siguiente != self.primero:
                actual = actual.siguiente;
            actual.siguiente = nuevo_nodo;
            self.primero = nuevo_nodo;
            return;
        anterior = self.primero;
        actual = self.primero.siguiente;
        while actual != self.primero:
            if actual.dato == dato_buscado:
                nuevo_nodo.siguiente = actual;
                anterior.siguiente = nuevo_nodo;
                return;
            anterior = actual;
            actual = actual.siguiente;
        print("El dato", dato_buscado, "no se encuentra en la lista.");


    def insertar_despues(self, dato_buscado, dato_nuevo):
        if self.primero is None:
            print("La lista está vacía.");
            return;
        nuevo_nodo = Nodo(dato_nuevo);
        actual = self.primero;
        while actual is not None:
            if actual.dato == dato_buscado:
                nuevo_nodo.siguiente = actual.siguiente;
                actual.siguiente = nuevo_nodo;
                if actual == self.primero:
                    self.primero = nuevo_nodo;
                return;
            actual = actual.siguiente;
            if actual == self.primero:
                print("El dato", dato_buscado, "no se encuentra en la lista.");
                return;
    

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

    
    # Modificar / Actualizar
    def modificar_primero(self, nuevo_dato):
        if self.primero is not None:
            self.primero.dato = nuevo_dato

    

    def modificar_antes(self, nodo_buscado, nuevo_dato):
        if self.primero is None:
            print("La lista está vacía.")
            return
        actual = self.primero
        anterior = None
        while actual.siguiente != self.primero:
            if actual.dato == nodo_buscado:
                if anterior is not None:
                    anterior.dato = nuevo_dato
                    return
                else:
                    print("El nodo buscado es el primero de la lista.")
                    return
            anterior = actual
            actual = actual.siguiente
            if actual == self.primero:
                break
        print("El nodo antes del nodo buscado no se encuentra en la lista.")


    
    def modificar(self, nodo_a_modificar, nuevo_dato):
        if self.primero is None:
            print("La lista está vacía.")
            return
        actual = self.primero
        while actual.siguiente != self.primero:
            if actual.dato == nodo_a_modificar:
                actual.dato = nuevo_dato
                return
            actual = actual.siguiente
            if actual == self.primero:
                break
        print("El nodo buscado no se encuentra en la lista.")

    
    def modificar_despues(self, nodo_buscado, nuevo_dato):
        if self.primero is None:
            print("La lista está vacía.")
            return
        actual = self.primero
        while actual.siguiente != self.primero:
            if actual.dato == nodo_buscado:
                nuevo_nodo = Nodo(nuevo_dato)
                nuevo_nodo.siguiente = actual.siguiente.siguiente
                actual.siguiente = nuevo_nodo
                return
            actual = actual.siguiente
            if actual == self.primero:
                break
        print("El nodo buscado no se encuentra en la lista.")

    
    def modificar_ultimo(self, nuevo_dato):
        if self.primero is None:
            print("La lista está vacía.")
            return
        actual = self.primero
        while actual.siguiente != self.primero:
            actual = actual.siguiente
        actual.dato = nuevo_dato
    

    # Eliminar / Remover
    def eliminar_primero(self):
        if self.primero is None:
            print("La lista está vacía, no se puede eliminar ningún nodo.")
            return
        if self.primero.siguiente == self.primero:  # Si solo hay un nodo en la lista
            self.primero = None
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = self.primero.siguiente
            self.primero = self.primero.siguiente

    
    def eliminar_antes(self, nodo_buscado):
        if self.primero is None:
            print("La lista está vacía.")
            return
        if self.primero.dato == nodo_buscado:
            print("El nodo buscado es el primer nodo de la lista, no se puede eliminar antes de él.")
            return
        actual = self.primero
        while actual.siguiente != self.primero:
            if actual.siguiente.dato == nodo_buscado:
                if actual == self.primero:
                    anterior = self.primero
                    while anterior.siguiente != self.primero:
                        anterior = anterior.siguiente
                    anterior.siguiente = actual.siguiente
                    self.primero = actual.siguiente
                else:
                    actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente
            if actual == self.primero:
                break
        print("No hay ningún nodo antes del nodo buscado.")

    
    def eliminar(self, dato):
        if self.primero is None:
            print("La lista está vacía.")
            return
        if self.primero.dato == dato:
            self.eliminar_primer_nodo()
            return
        actual = self.primero
        while actual.siguiente != self.primero:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente
            if actual == self.primero:
                break
        print("El nodo buscado no se encuentra en la lista.")

    
    def eliminar_despues(self, nodo_buscado):
        if self.primero is None:
            print("La lista está vacía.")
            return
        actual = self.primero
        while actual.siguiente != self.primero:
            if actual.dato == nodo_buscado:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente
            if actual == self.primero:
                break
        print("El nodo buscado no se encuentra en la lista.")

    
    def eliminar_ultimo(self):
        if self.primero is None:
            print("La lista está vacía.")
            return
        if self.primero.siguiente == self.primero:
            self.primero = None
            return
        actual = self.primero
        while actual.siguiente.siguiente != self.primero:
            actual = actual.siguiente
        actual.siguiente = self.primero

    
    # Mostrar
    def imprimir(self):
        if self.primero is None:
            print("La lista está vacía");
        else:
            aux = self.primero;
            while True:
                print(aux.dato, end=" ");
                aux = aux.siguiente;
                if aux == self.primero:
                    break;
            print();


# # --- crear ---
lista = ListaEnlazadaCircular();
lista.insertar(1);
lista.insertar(3);
lista.insertar(5);
print("Lista original: ", end='');
lista.imprimir();


# --- agregar ---
lista.insertar_inicio(0);
lista.insertar_antes(3, 2);
lista.insertar_despues(3, 4);
print('Lista después de agregar datos: ', end='');
lista.imprimir();


# --- modificar ---
lista.modificar_primero(10)
lista.modificar_antes(2, 20)
lista.modificar(3, 30)
lista.modificar_despues(30, 40)
lista.modificar_ultimo(50)
print('Lista después de modificar datos: ', end='');
lista.imprimir();

# --- eliminar ---
lista.eliminar_primero()
lista.eliminar_antes(2)
lista.eliminar(40)
lista.eliminar_despues(2)
lista.eliminar_ultimo()
print('Lista después de eliminar: ', end= '');
lista.imprimir();

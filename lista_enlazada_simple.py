
class Nodo:
    def __init__(self, dato):
        self.dato = dato;
        self.enlace = None;

class ListaEnlazadaSimple:
    def __init__(self):
        self.primero = None;

    # Insertar/Agregar - Dato
    def insertarInicio(self, dato):
        nuevo = Nodo(dato);
        nuevo.enlace = self.primero;
        self.primero = nuevo;
        print(f'Se agrego al inicio {dato}')


    def insertarAntes(self, dato, datoB):
        nuevo = Nodo(dato);
        print("Insertando el dato", dato, "antes del dato", datoB)
        if self.primero is None:
            self.primero = nuevo;
            return;
        if self.primero.dato == datoB:
            nuevo.enlace = self.primero;
            self.primero = nuevo;
            return;
        anterior = self.primero;
        actual = self.primero.enlace;
        while actual is not None:
            if actual.dato == datoB:
                nuevo.enlace = actual;
                anterior.enlace = nuevo;
                return;
            anterior = actual;
            actual = actual.enlace;
        print("El dato", datoB, "no se encuentra en la lista.");
    

    def insertarDespues(self, dato, datoB):
        nuevo = Nodo(dato);
        print("Insertando el dato", dato, "después del dato", datoB)
        if self.primero is None:
            self.primero = nuevo;
            return;
        aux = self.primero;
        while aux is not None:
            if aux.dato == datoB:
                nuevo.enlace = aux.enlace;
                aux.enlace = nuevo;
                return;
            aux = aux.enlace;
        print("El dato", datoB, "no se encuentra en la lista.");


    def insertar(self, dato):
        print(f'Se agrego el dato {dato}')
        nuevo = Nodo(dato);
        if self.primero is None:
            self.primero = nuevo;
            return;
        aux = self.primero;
        while aux.enlace is not None:
            aux = aux.enlace;
        aux.enlace = nuevo;
       

    # Modificar/Actualizar - Nodo
    def modificarPrimerNodo(self, nuevo_dato):
        if self.primero is not None:
            self.primero.dato = nuevo_dato;
        else:
            print("La lista está vacía, no se puede modificar el primer nodo.");
    

    def modificar(self, dato, dato_nuevo):
        aux = self.primero;
        while aux is not None:
            if aux.dato == dato:
                aux.dato = dato_nuevo;
                return;
            aux = aux.enlace;
        print("El dato", dato, "no se encuentra en la lista.");

    def modificarUltimoNodo(self, nuevo_dato):
        if self.primero is None:
            print("La lista está vacía, no se puede modificar el último nodo.");
            return;
        aux = self.primero;
        while aux.enlace is not None:
            aux = aux.enlace;
        aux.dato = nuevo_dato;
    

    # Eliminar/Quitar
    def eliminarPrimero(self):
        if self.primero is None:
            return;
        temp = self.primero;
        self.primero = self.primero.enlace;
        temp.enlace = None;


    def eliminarAntes(self, datoB):
        if self.primero is None or self.primero.enlace is None:
            print("La lista está vacía o tiene solo un nodo.");
            return;
        if self.primero.enlace.dato == datoB:
            self.primero = self.primero.enlace;
            return;
        anterior = self.primero;
        actual = self.primero.enlace;
        while actual.enlace is not None:
            if actual.enlace.dato == datoB:
                anterior.enlace = actual.enlace;
                return;
            anterior = actual;
            actual = actual.enlace;
        print("El dato", datoB, "no se encuentra en la lista o es el primer nodo.");
    

    def eliminar(self, dato):
        if self.primero is None:
            return;
        if self.primero.dato == dato:
            self.eliminarPrimero();
            return;
        anterior = self.primero;
        actual = self.primero.enlace;
        while actual is not None:
            if actual.dato == dato:
                anterior.enlace = actual.enlace;
                actual.enlace = None;
                return;
            anterior = actual;
            actual = actual.enlace;
        print("El dato", dato, "no se encuentra en la lista.");


    def eliminarDespues(self, datoB):
        if self.primero is None:
            print("La lista está vacía, no se puede eliminar un nodo después del nodo buscado.");
            return;
        actual = self.primero;
        while actual is not None:
            if actual.dato == datoB and actual.enlace is not None:
                actual.enlace = actual.enlace.enlace;
                return;
            actual = actual.enlace;
        print("El dato", datoB, "no se encuentra en la lista o es el último nodo.");


    def eliminarUltimo(self):
        if self.primero is None:
            print('La lista está vacía, no se puede eliminar el último nodo.');
            return;
        if self.primero.enlace is None:
            self.primero = None;
            return;
        aux = self.primero;
        while aux.enlace.enlace is not None:
            aux = aux.enlace;
        aux.enlace = None;


    def imprimir(self):
        aux = self.primero;
        while aux is not None:
            print(aux.dato, end=" ");
            aux = aux.enlace;
        print();


# --- crear ---
lista = ListaEnlazadaSimple();
lista.insertar(2);
lista.insertar(4);
lista.insertar(6);
print("Lista original: ", end='');
lista.imprimir();


# --- Insertar ---
lista.insertarInicio(1);
lista.insertarAntes(3, 4);
lista.insertarDespues(5, 4);
lista.insertar(7);
print('Lista después de agregar datos: ', end='');
lista.imprimir();


# --- Actualizar / Modificar ---
#lista.modificarPrimerNodo(0);
#lista.modificar(0, 10);
#lista.modificarUltimoNodo(8);
#lista.imprimir();


# --- Eliminar ---
lista.eliminarPrimero();
lista.eliminarAntes(4);
lista.eliminar(7);
lista.eliminarDespues(4);
lista.eliminarUltimo();
print('Lista después de eliminar: ', end= '');
lista.imprimir();


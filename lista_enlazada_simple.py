
class NodoSimple:
    def __init__(self, dato):
        self.dato = dato;
        self.enlace = None;

class ListaEnlazadaSimple:
    def __init__(self):
        self.primero = None;

    # Insertar/Agregar
    def insertarInicio(self, dato):
        nuevo = NodoSimple(dato);
        nuevo.enlace = self.primero;
        self.primero = nuevo;


    def insertarAntes(self, dato, datoB):
        nuevo = NodoSimple(dato);
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
        nuevo = NodoSimple(dato);
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

    def insertarFinal(self, dato):
        nuevo = NodoSimple(dato);
        if self.primero is None:
            self.primero = nuevo;
            return;
        aux = self.primero;
        while aux.enlace is not None:
            aux = aux.enlace;
        aux.enlace = nuevo;

    # Modificar/Actualizar
    def modificar(self, dato, dato_nuevo):
        aux = self.primero;
        while aux is not None:
            if aux.dato == dato:
                aux.dato = dato_nuevo;
                return;
            aux = aux.enlace;
        print("El dato", dato, "no se encuentra en la lista.");

    # Eliminar/Quitar
    def eliminarPrimero(self):
        if self.primero is None:
            return;
        temp = self.primero;
        self.primero = self.primero.enlace;
        temp.enlace = None;

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

    def imprimir(self):
        aux = self.primero;
        while aux is not None:
            print(aux.dato, end=" ");
            aux = aux.enlace;
        print();

lista = ListaEnlazadaSimple();
lista.insertarFinal(1);
lista.insertarFinal(2);
lista.insertarFinal(3);
lista.insertarFinal(4);
print("Lista original:");
lista.imprimir();

print('--- Insertar ---');
lista.insertarInicio(5);
lista.insertarAntes(2.5, 3);
lista.insertarDespues(3.5, 3);
print('--- Modificar ---');
print('___ Eliminar ---');


lista.imprimir();

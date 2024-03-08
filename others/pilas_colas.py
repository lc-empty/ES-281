from collections import deque;

# Pila
class Pila:
    def __init__(self):
        self.cima = None;

    def esta_vacia(self):
        return self.cima is None;

    # Agregar
    def apilar(self, elemento):
        nuevo = Nodo(elemento);
        nuevo.enlace = self.cima;
        self.cima = nuevo;

    # Quitar
    def desapilar(self):
        if not self.esta_vacia():
            dato = self.cima.dato;
            self.cima = self.cima.enlace;
            return dato;
        else:
            print("La pila está vacía");

    # Mostrar
    def imprimir(self):
        if self.esta_vacia():
            print("La pila está vacía");
        else:
            temp = self.cima
            while temp is not None:
                print(temp.dato);
                temp = temp.enlace;

# Cola
class Cola:
    def __init__(self):
        self.cabeza = None;
        self.cola = None;


    def esta_vacia(self):
        return self.cabeza is None;


    def enColar(self, dato):
        nuevo = Nodo(dato);
        if self.esta_vacia():
            self.cabeza = nuevo;
            self.cola = nuevo;
        else:
            self.cola.siguiente = nuevo;
            self.cola = nuevo;


    def desColar(self):
        if not self.esta_vacia():
            dato = self.cabeza.dato;
            self.cabeza = self.cabeza.siguiente;
            if self.cabeza is None:
                self.cola = None;
            return dato;
        else:
            return None;


    def tamano(self):
        contador = 0;
        aux = self.cabeza;
        while aux is not None:
            contador += 1;
            aux = aux.siguiente;
        return contador;


    # Mostrar
    def imprimir(self):
        if self.esta_vacia():
            print("La cola está vacía");
        else:
            aux = self.cabeza;
            while aux is not None:
                print(aux.dato, end=" ");
                aux = aux.siguiente;
            print();


# Pila
pila = Pila();
pila.apilar(1);
pila.apilar(2);
pila.apilar(3);
pila.imprimir();


# Cola
cola = Cola();
cola.enColar(1);
cola.enColar(2);
cola.enColar(3);
cola.imprimir();

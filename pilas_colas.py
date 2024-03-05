from collections import deque;

# Pila
class Pila:
    def __init__(self):
        self.items = [];


    def esta_vacia(self):
        return len(self.items) == 0;
    

    def apilar(self, elemento):
        # self.items.append(elemento);
        self.items += [elemento]
    

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop();
        print("La pila esta vacia")


    # Mostrar
    def imprimir(self):
        print(self.items);

# Cola
class Cola:
    def __init__(self):
        self.items = deque();


    def esta_vacia(self):
        return len(self.items) == 0;


    def enColar(self, dato):
        self.items.append(dato);


    def desColar(self):
        if not self.esta_vacia():
            return self.items.popleft();
        else:
            return None;


    def tamano(self):
        return len(self.items);


    # Mostrar
    def imprimir(self):
        print(self.items);


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

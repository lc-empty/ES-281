
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def imprimir(self):
        actual = self.primero
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def extraer_sublista(self, inicio, fin):
        sublista = ListaDobleEnlazada()
        actual = self.primero
        posicion = 1

        # Buscar el inicio de la sublista
        while actual and posicion < inicio:
            actual = actual.siguiente
            posicion += 1

        # Extraer los nodos hasta el final del rango
        while actual and posicion <= fin:
            sublista.agregar_final(actual.dato)
            actual = actual.siguiente
            posicion += 1

        return sublista

# Crear la lista original
lista = ListaDobleEnlazada()
for i in range(1, 9):
    lista.agregar_final(i)

# Imprimir la lista original
print("Lista original:")
lista.imprimir()

# Extraer y mostrar diferentes sublistas
print("\nSublista [2:5]:")
sublista1 = lista.extraer_sublista(2, 5)
sublista1.imprimir()


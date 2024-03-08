
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
    def modificar_nodo(self, nodo_a_modificar, nuevo_dato):
        actual = self.inicio
        while actual is not None:
            if actual.dato == nodo_a_modificar:
                actual.dato = nuevo_dato;
                break;
            actual = actual.nodo_siguiente;
    def imprimir(self):
        actual = self.primero
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def invertir_en_grupos(self, k):
        actual = self.primero
        while actual:
            inicio_grupo = actual
            final_grupo = actual
            for _ in range(k - 1):
                if final_grupo.siguiente:
                    final_grupo = final_grupo.siguiente
                else:
                    break

            for _ in range(k // 2):
                self.modificar_nodo(inicio_grupo, final_grupo.dato)
                self.modificar_nodo(final_grupo, inicio_grupo.dato)
                inicio_grupo = inicio_grupo.siguiente
                final_grupo = final_grupo.anterior

            actual = inicio_grupo.siguiente

# Crear la lista original
lista = ListaDobleEnlazada()
for i in range(1, 11):
    lista.agregar_final(i)

# Imprimir la lista original
print("Lista original:")
lista.imprimir()

# Invertir nodos en grupos de tamaño K
K = 2
print("\nDespués de invertir en grupos de tamaño", K)
lista.invertir_en_grupos(K)
lista.imprimir()

# Realizar la inversión con otro valor de K
K = 3
print("\nDespués de invertir en grupos de tamaño", K)
lista.invertir_en_grupos(K)
lista.imprimir()


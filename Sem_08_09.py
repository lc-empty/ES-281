# Ejercicios parte 2

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.inicio = None


    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.inicio
        self.inicio = nuevo_nodo


    def insertar_final(self, dato):
        return


    def eliminar_nodo(self, dato):
        return


    def mostrar(self):
        actual = self.inicio
        while actual:
            if actual.siguiente:
                print(actual.dato, end=" -> ")
            else:
                print(actual.dato)
            actual = actual.siguiente


    # 10. Desarrollar el código de buscar nodo en la lista enlazada simple.
    def buscar(self, dato):
        actual = self.inicio
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False


    # Suma de Nodos
    # 11. Implementa una función que sume todos los nodos de una lista enlazada simple.
    def suma_todos_nodos(self):
        suma = 0
        actual = self.inicio
        while actual:
            suma += actual.dato
            actual = actual.siguiente
        return suma


    # Longitud de la Lista
    # 12. Crea una función que devuelva la longitud de una lista enlazada simple.
    def longitud(self):
        contador = 0
        actual = self.inicio
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador


    # Concatenar Listas
    # 13. Implementa una función que concatene dos listas enlazadas simples.
    def concatenar(self, otra_lista):
        actual = self.inicio
        if actual is None:
            self.inicio = otra_lista.inicio
            return
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = otra_lista.inicio


    # Eliminar Duplicados
    # 14. Crea una función que elimine los nodos duplicados de una lista enlazada simple.
    def eliminar_duplicados(self):
        if self.inicio is None:
            return
        valores_vistos = set()
        actual = self.inicio
        valores_vistos.add(actual.dato)
        while actual.siguiente:
            if actual.siguiente.dato in valores_vistos:
                actual.siguiente = actual.siguiente.siguiente
            else:
                valores_vistos.add(actual.siguiente.dato)
                actual = actual.siguiente


    # Invertir Lista
    # 15. Implementa una función que invierta el orden de una lista enlazada simple
    def invertir_orden(self):
        anterior = None
        actual = self.inicio
        siguiente = None
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.inicio = anterior


# actual = lista.inicio
# while actual:
#     print(actual.dato, end=" -> ")
#     actual = actual.siguiente


# Creamos una lista enlazada
lista = ListaEnlazadaSimple()

# Insertamos algunos nodos al inicio de la lista
lista.insertar_inicio(3)
lista.insertar_inicio(2)
lista.insertar_inicio(1)
lista.insertar_inicio(1)

# Mostramos la lista
print("Lista original:")
lista.mostrar()

# Buscamos un valor en la lista
valor_buscado = 2
if lista.buscar(valor_buscado):
    print(f"El valor {valor_buscado} está en la lista.")
else:
    print(f"El valor {valor_buscado} no está en la lista.")

# Sumamos todos los nodos de la lista
suma_total = lista.suma_todos_nodos()
print("La suma de todos los nodos es:", suma_total)

# Obtenemos la longitud de la lista
longitud_lista = lista.longitud()
print("La longitud de la lista es:", longitud_lista)

# Creamos otra lista
otra_lista = ListaEnlazadaSimple()
otra_lista.insertar_inicio(4)
otra_lista.insertar_inicio(5)

# Concatenamos las dos listas
lista.concatenar(otra_lista)

# Mostramos la lista concatenada
print("Lista concatenada:")
lista.mostrar()

# Eliminamos los nodos duplicados
lista.eliminar_duplicados()

# Mostramos la lista sin duplicados
print("Lista sin duplicados:")
lista.mostrar()

# Invertimos el orden de la lista
lista.invertir_orden()

# Mostramos la lista invertida
print("Lista invertida:")
lista.mostrar()
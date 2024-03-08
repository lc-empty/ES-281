# Ejercicio parte 01 -  Listas Enlazadas Dobles:

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaEnlazadaDoble:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def esta_vacia(self):
        return self.inicio is None

    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.inicio = self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.inicio
            self.inicio.anterior = nuevo_nodo
            self.inicio = nuevo_nodo

    def agregar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.inicio = self.fin = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.fin
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo

    def eliminar(self, dato):
        actual = self.inicio
        while actual is not None:
            if actual.dato == dato:
                if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.inicio = actual.siguiente

                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.fin = actual.anterior
                return  # Se encontro y elimino el nodo, salir del metodo

            actual = actual.siguiente

    def imprimir_adelante(self):
        print("Lista invertida hacia adelante:")
        actual = self.inicio
        while actual is not None:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def imprimir_atras(self):
        print("Lista invertida hacia atras:")
        actual = self.fin
        while actual is not None:
            print(actual.dato, end=" ")
            actual = actual.anterior
        print()

    # Duplicar Nodos:
    # 1. Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e imprime la lista original y la lista duplicada hacia adelante y hacia atras.
    def duplicar_nodos(self):
        actual = self.inicio
        while actual is not None:
            nuevo_nodo = Nodo(actual.dato)
            siguiente_temporal = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
            if siguiente_temporal is not None:
                nuevo_nodo.siguiente = siguiente_temporal
                siguiente_temporal.anterior = nuevo_nodo
            else:
                self.fin = nuevo_nodo
            actual = siguiente_temporal

    # Contar Nodos Pares e Impares:
    # 2. Crea una lista con al menos 9 nodos, cuenta cuantos nodos tienen un dato par y cuantos tienen un dato impar e imprime la lista hacia adelante y hacia atras.
    def contar_pares_impares(self):
        contador_pares = 0
        contador_impares = 0
        actual = self.inicio
        while actual is not None:
            if actual.dato % 2 == 0:
                contador_pares += 1
            else:
                contador_impares += 1
            actual = actual.siguiente
        return contador_pares, contador_impares

    # Insertar Nodo en Posicion Especifica:
    # 3. Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 en la posicion 3 e imprime la lista hacia adelante y hacia atras.
    def insertar_en_posicion(self, dato, posicion):
        nuevo_nodo = Nodo(dato)
        if posicion < 1:
            raise ValueError("La posicion no puede ser menor que 1.")
        if posicion == 1:
            nuevo_nodo.siguiente = self.inicio
            if self.inicio is not None:
                self.inicio.anterior = nuevo_nodo
            self.inicio = nuevo_nodo
        else:
            contador = 1
            actual = self.inicio
            while contador < posicion - 1 and actual is not None:
                actual = actual.siguiente
                contador += 1
            if actual is None:
                raise ValueError(
                    "La posicion no puede ser mayor que la cantidad de nodos."
                )
            nuevo_nodo.siguiente = actual.siguiente
            if actual.siguiente is not None:
                actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    # Eliminar Nodos Duplicados:
    # 4. Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, dejando solo una instancia de cada dato e imprime la lista hacia adelante y hacia atras.
    def eliminar_duplicados(self):
        # Verificar si la lista está vacía
        if self.inicio is None:
            return

        # Inicializar un conjunto para almacenar los nodos vistos
        nodos_vistos = set()
        nodo_actual = self.inicio

        # Recorrer la lista
        while nodo_actual:
            # Comprobar si el dato del nodo actual ya se ha visto
            if nodo_actual.dato in nodos_vistos:
                # Eliminar el nodo duplicado
                nodo_anterior = nodo_actual.anterior
                nodo_siguiente = nodo_actual.siguiente

                if nodo_anterior:
                    nodo_anterior.siguiente = nodo_siguiente
                else:
                    self.inicio = nodo_siguiente

                if nodo_siguiente:
                    nodo_siguiente.anterior = nodo_anterior
                else:
                    self.fin = nodo_anterior

                nodo_actual = nodo_siguiente
            else:
                # Agregar el dato del nodo actual al conjunto de nodos vistos
                nodos_vistos.add(nodo_actual.dato)
                nodo_actual = nodo_actual.siguiente    # Invertir la Lista:


    # 5. Crea una lista con al menos 6 nodos, invierte el orden de la lista (el ultimo elemento se convierte en el primero y viceversa) e imprime la lista hacia adelante y hacia atras
    def invertir(self):
        actual = self.inicio
        while actual is not None:
            actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
            actual = actual.anterior
        self.inicio, self.fin = self.fin, self.inicio


lista_original = ListaEnlazadaDoble()
lista_original.agregar_final(1)
lista_original.agregar_final(2)
lista_original.agregar_final(3)
lista_original.agregar_final(4)

lista_original.imprimir_adelante()
lista_original.imprimir_atras()

# 1 ----------------------------------------------------------------
# lista_duplicada = ListaEnlazadaDoble()
# actual = lista_original.inicio
# while actual is not None:
#     lista_duplicada.agregar_final(actual.dato)
#     actual = actual.siguiente

# lista_duplicada.duplicar_nodos()
# lista_duplicada.imprimir_adelante()
# lista_duplicada.imprimir_atras()


# 2 ----------------------------------------------------------------
# lista_original.agregar_final(5)
# lista_original.agregar_final(6)
# lista_original.agregar_final(7)
# lista_original.agregar_final(8)
# lista_original.agregar_final(9)
# pares, impares = lista_original.contar_pares_impares()
# print("Cantidad de nodos pares:", pares)
# print("Cantidad de nodos impares:", impares)


# 3 ----------------------------------------------------------------
# lista_original.agregar_final(5)
# lista_original.insertar_en_posicion(15, 3)
# lista_original.imprimir_adelante()


# 4 ----------------------------------------------------------------
#lista_original.insertar_en_posicion(12,3)
#lista_original.agregar_final(12)
#lista_original.eliminar_duplicados()
#lista_original.imprimir_adelante()


# 5 ----------------------------------------------------------------
# lista_original.invertir()

# lista_original.imprimir_adelante()
# lista_original.imprimir_atras()




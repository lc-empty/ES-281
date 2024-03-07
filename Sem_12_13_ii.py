# ARBOLES
# -----------------------------------------------

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.rama_izquierda = None
        self.rama_derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None


    # Insertar
    def insertar(self, dato):
        # Creamos un nuevo nodo con el dato dado
        nuevo_nodo = Nodo(dato)
        # Si el árbol está vacío, el nuevo nodo se convierte en la raíz
        if not self.raiz:
            self.raiz = nuevo_nodo
        else:
            # Inicializamos el nodo actual como la raíz del árbol
            nodo_actual = self.raiz
            # Iteramos hasta que encontremos el lugar adecuado para insertar el nuevo nodo
            while True:
                # Si el dato es menor que el dato del nodo actual, nos movemos a la rama izquierda
                if dato < nodo_actual.dato:
                    # Si la rama izquierda está vacía, insertamos el nuevo nodo aquí y salimos del bucle
                    if not nodo_actual.rama_izquierda:
                        nodo_actual.rama_izquierda = nuevo_nodo
                        break
                    # Si no está vacía, continuamos hacia abajo por la rama izquierda
                    else:
                        nodo_actual = nodo_actual.rama_izquierda
                # Si el dato es mayor que el dato del nodo actual, nos movemos a la rama derecha
                elif dato > nodo_actual.dato:
                    # Si la rama derecha está vacía, insertamos el nuevo nodo aquí y salimos del bucle
                    if not nodo_actual.rama_derecha:
                        nodo_actual.rama_derecha = nuevo_nodo
                        break
                    # Si no está vacía, continuamos hacia abajo por la rama derecha
                    else:
                        nodo_actual = nodo_actual.rama_derecha
                # Si el dato ya está presente en el árbol, no hacemos nada y salimos del bucle
                else:
                    break


    #  5. Implementar una función que cuente la cantidad de nodos en el árbol
    def cantidad_nodos(self):
        # Si el árbol está vacío, no hay nodos, así que devolvemos 0
        if not self.raiz:
            return 0
        contador = 0
        # Creamos una pila y agregamos la raíz del árbol a ella
        pila = [self.raiz]
        # Iteramos mientras haya nodos en la pila
        while pila:
            # Sacamos el nodo actual de la pila
            nodo_actual = pila.pop()
            # Incrementamos el contador de nodos
            contador += 1
            # Si hay una rama derecha en el nodo actual, la agregamos a la pila
            if nodo_actual.rama_derecha:
                pila.append(nodo_actual.rama_derecha)
            # Si hay una rama izquierda en el nodo actual, la agregamos a la pila
            if nodo_actual.rama_izquierda:
                pila.append(nodo_actual.rama_izquierda)
        return contador


    #  6. Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos).
    def cantidad_nodos_hoja(self):
        # Si el árbol está vacío, no hay nodos hoja, así que devolvemos 0
        if not self.raiz:
            return 0
        contador = 0
        # Creamos una pila y agregamos la raíz del árbol a ella
        pila = [self.raiz]
        # Iteramos mientras haya nodos en la pila
        while pila:
            # Sacamos el nodo actual de la pila
            nodo_actual = pila.pop()
            # Verificamos si el nodo actual es una hoja (no tiene ramas izquierda ni derecha)
            if not nodo_actual.rama_izquierda and not nodo_actual.rama_derecha:
                # Si es una hoja, incrementamos el contador
                contador += 1
            # Si hay una rama derecha en el nodo actual, la agregamos a la pila
            if nodo_actual.rama_derecha:
                pila.append(nodo_actual.rama_derecha)
            # Si hay una rama izquierda en el nodo actual, la agregamos a la pila
            if nodo_actual.rama_izquierda:
                pila.append(nodo_actual.rama_izquierda)
        return contador

    #  7. Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo).
    def cantidad_nodos_internos(self):
        # Si el árbol está vacío, no hay nodos internos, así que devolvemos 0
        if not self.raiz:
            return 0
        contador = 0
        # Creamos una pila y agregamos la raíz del árbol a ella
        pila = [self.raiz]
        # Iteramos mientras haya nodos en la pila
        while pila:
            # Sacamos el nodo actual de la pila
            nodo_actual = pila.pop()
            # Verificamos si el nodo actual no es la raíz y tiene al menos una rama
            if nodo_actual != self.raiz and (nodo_actual.rama_izquierda or nodo_actual.rama_derecha):
                # Si es un nodo interno, incrementamos el contador
                contador += 1
            # Si hay una rama derecha en el nodo actual, la agregamos a la pila
            if nodo_actual.rama_derecha:
                pila.append(nodo_actual.rama_derecha)
            # Si hay una rama izquierda en el nodo actual, la agregamos a la pila
            if nodo_actual.rama_izquierda:
                pila.append(nodo_actual.rama_izquierda)
        return contador


    #  8. Implementar una función que calcule la altura del árbol (la longitud del camino más largo desde la raíz hasta una hoja)
    def cantidad_nodos_internos(self):
        # Si el árbol está vacío, no hay nodos internos, así que devolvemos 0
        if not self.raiz:
            return 0
        contador = 0
        # Creamos una pila y agregamos la raíz del árbol a ella
        pila = [self.raiz]
        # Iteramos mientras haya nodos en la pila
        while pila:
            # Sacamos el nodo actual de la pila
            nodo_actual = pila.pop()
            # Verificamos si el nodo actual no es la raíz y tiene al menos una rama
            if nodo_actual != self.raiz and (nodo_actual.rama_izquierda or nodo_actual.rama_derecha):
                # Si es un nodo interno, incrementamos el contador
                contador += 1
            # Si hay una rama derecha en el nodo actual, la agregamos a la pila
            if nodo_actual.rama_derecha:
                pila.append(nodo_actual.rama_derecha)
            # Si hay una rama izquierda en el nodo actual, la agregamos a la pila
            if nodo_actual.rama_izquierda:
                pila.append(nodo_actual.rama_izquierda)
        # Devolvemos el contador que contiene la cantidad total de nodos internos en el árbol
        return contador


    #  9. Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz hasta el nodo).
    def profundidad_nodo(self, dato):
        # Si el árbol está vacío, retornamos -1 porque no hay ningún nodo
        if not self.raiz:
            return -1
        profundidad = 0
        # Inicializamos el nivel actual con la raíz del árbol
        nivel_actual = [self.raiz]
        # Iteramos mientras haya nodos en el nivel actual
        while nivel_actual:
            # Inicializamos una lista para el siguiente nivel de nodos
            siguiente_nivel = []
            # Iteramos sobre todos los nodos en el nivel actual
            for nodo in nivel_actual:
                # Verificamos si el dato del nodo actual es igual al dato buscado
                if nodo.dato == dato:
                    # Si es así, devolvemos la profundidad actual
                    return profundidad
                # Agregamos las ramas del nodo actual al siguiente nivel
                if nodo.rama_izquierda:
                    siguiente_nivel.append(nodo.rama_izquierda)
                if nodo.rama_derecha:
                    siguiente_nivel.append(nodo.rama_derecha)
            # Actualizamos el nivel actual al siguiente nivel
            nivel_actual = siguiente_nivel
            # Incrementamos la profundidad para el siguiente nivel
            profundidad += 1
        return -1  # El nodo no está en el árbol


    # 10. Implementar una función que encuentre el nodo con el valor mínimo en el árbol.
    def encontrar_minimo(self):
        # Si el árbol está vacío, no hay mínimo, así que retornamos None
        if not self.raiz:
            return None
        # Comenzamos desde la raíz del árbol
        nodo_actual = self.raiz
        # Avanzamos por las ramas izquierdas del árbol hasta encontrar el nodo más a la izquierda
        while nodo_actual.rama_izquierda:
            nodo_actual = nodo_actual.rama_izquierda
        # Una vez que no hay más ramas izquierdas, hemos llegado al nodo más a la izquierda que es el mínimo
        return nodo_actual.dato


    # 11. Implementar una función que encuentre el nodo con el valor máximo en el árbol.
def encontrar_maximo(self):
    # Si el árbol está vacío, no hay máximo, así que retornamos None
    if not self.raiz:
        return None
    # Comenzamos desde la raíz del árbol
    nodo_actual = self.raiz
    # Avanzamos por las ramas derechas del árbol hasta encontrar el nodo más a la derecha
    while nodo_actual.rama_derecha:
        nodo_actual = nodo_actual.rama_derecha
    # Una vez que no hay más ramas derechas, hemos llegado al nodo más a la derecha que es el máximo
    return nodo_actual.dato


# Crear un arbol_binario
arbol_binario = ArbolBinario()

# Agregar elementos
arbol_binario.insertar(5)
arbol_binario.insertar(3)
arbol_binario.insertar(7)
arbol_binario.insertar(1)
arbol_binario.insertar(4)

# --  5
print(arbol_binario.cantidad_nodos())

# --  6
print(arbol_binario.cantidad_nodos_hoja())

# --  7
print(arbol_binario.cantidad_nodos_internos())

# --  8
print(arbol_binario.altura_arbol())

# --  9
print(arbol_binario.profundidad_nodo(5))

# -- 10
print(arbol_binario.encontrar_minimo())

# -- 11
print(arbol_binario.encontrar_maximo())


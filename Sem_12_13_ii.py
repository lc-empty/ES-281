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

        # Inicializamos un contador para contar los nodos
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
        # Devolvemos el contador que contiene la cantidad total de nodos en el árbol
        return contador

    #  6. Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos).
    def cantidad_nodos_hoja(self):
        # Si el árbol está vacío, no hay nodos hoja, así que devolvemos 0
        if not self.raiz:
            return 0

        # Inicializamos un contador para contar los nodos hoja
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
        # Devolvemos el contador que contiene la cantidad total de nodos hoja en el árbol
        return contador

    #  7. Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo).
    def cantidad_nodos_internos(self):
        # Si el árbol está vacío, no hay nodos internos, así que devolvemos 0
        if not self.raiz:
            return 0

        # Inicializamos un contador para contar los nodos internos
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

    #  8. Implementar una función que calcule la altura del árbol (la longitud del camino más largo desde la raíz hasta una hoja)
    def altura_arbol(self):
        if not self.raiz:
            return 0
        
        altura = 0
        nivel_actual = [self.raiz]
        while nivel_actual:
            siguiente_nivel = []
            for nodo in nivel_actual:
                if nodo.rama_izquierda:
                    siguiente_nivel.append(nodo.rama_izquierda)
                if nodo.rama_derecha:
                    siguiente_nivel.append(nodo.rama_derecha)
            nivel_actual = siguiente_nivel
            altura += 1
        return altura


    #  9. Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz hasta el nodo).
    def profundidad_nodo(self, dato):
        if not self.raiz:
            return -1
        
        profundidad = 0
        nivel_actual = [self.raiz]
        while nivel_actual:
            siguiente_nivel = []
            for nodo in nivel_actual:
                if nodo.dato == dato:
                    return profundidad
                if nodo.rama_izquierda:
                    siguiente_nivel.append(nodo.rama_izquierda)
                if nodo.rama_derecha:
                    siguiente_nivel.append(nodo.rama_derecha)
            nivel_actual = siguiente_nivel
            profundidad += 1
        return -1  # El nodo no está en el árbol    


    # 10. Implementar una función que encuentre el nodo con el valor mínimo en el árbol.
    def encontrar_minimo(self):
        if not self.raiz:
            return None
        
        nodo_actual = self.raiz
        while nodo_actual.rama_izquierda:
            nodo_actual = nodo_actual.rama_izquierda
        return nodo_actual.dato


    # 11. Implementar una función que encuentre el nodo con el valor máximo en el árbol.
    def encontrar_maximo(self):
        if not self.raiz:
            return None
        
        nodo_actual = self.raiz
        while nodo_actual.rama_derecha:
            nodo_actual = nodo_actual.rama_derecha
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


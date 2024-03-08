from collections import deque

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.rama_izquierda = None
        self.rama_derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None


    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.raiz:
            self.raiz = nuevo_nodo
        else:
            nodo_actual = self.raiz
            while True:
                if dato < nodo_actual.dato:
                    if not nodo_actual.rama_izquierda:
                        nodo_actual.rama_izquierda = nuevo_nodo
                        break
                    else:
                        nodo_actual = nodo_actual.rama_izquierda
                elif dato > nodo_actual.dato:
                    if not nodo_actual.rama_derecha:
                        nodo_actual.rama_derecha = nuevo_nodo
                        break
                    else:
                        nodo_actual = nodo_actual.rama_derecha
                else:
                    break


def arboles_iguales(arbol1, arbol2):
    if not arbol1.raiz and not arbol2.raiz:
        return True
    if not arbol1.raiz or not arbol2.raiz:
        return False
    
    cola1 = deque([arbol1.raiz])
    cola2 = deque([arbol2.raiz])
    
    while cola1 and cola2:
        nodo1 = cola1.popleft()
        nodo2 = cola2.popleft()
        
        if nodo1.dato != nodo2.dato:
            return False
        
        if nodo1.rama_izquierda and nodo2.rama_izquierda:
            cola1.append(nodo1.rama_izquierda)
            cola2.append(nodo2.rama_izquierda)
        elif nodo1.rama_izquierda or nodo2.rama_izquierda:
            return False
        
        if nodo1.rama_derecha and nodo2.rama_derecha:
            cola1.append(nodo1.rama_derecha)
            cola2.append(nodo2.rama_derecha)
        elif nodo1.rama_derecha or nodo2.rama_derecha:
            return False
        
    return len(cola1) == len(cola2) == 0

# Ejemplo de uso:
arbol_binario1 = ArbolBinario()
arbol_binario1.insertar(5)
arbol_binario1.insertar(2)
arbol_binario1.insertar(7)
arbol_binario1.insertar(1)
arbol_binario1.insertar(4)

arbol_binario2 = ArbolBinario()
arbol_binario2.insertar(5)
arbol_binario2.insertar(3)
arbol_binario2.insertar(7)
arbol_binario2.insertar(1)
arbol_binario2.insertar(4)

print(arboles_iguales(arbol_binario1, arbol_binario2))

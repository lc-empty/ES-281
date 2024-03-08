### Colas

#1. Implementa una función que determine si una palabra es palíndroma o no. Utiliza una cola para
#comparar los caracteres de la palabra en orden original y reverso.

from collections import deque


def es_palindromo(palabra):# Definimos la función es palindromo, esta recibe como parametro una palabra
    # Creamos una cola vacía utilizando deque
    cola = deque()# utiliczando deque del modulo collections se crea una cola vacía 

    for caracter in palabra:   # con un for recorremos la palabra y agregamos cada carácter a la cola
        cola.append(caracter)

   
    palindromo = True # inicializamos la variable apalindromo con True, esta variable nos permite saber si la palabra es palindromo

    while len(cola) > 1 and palindromo: # utilzando while comparamos los caracteres en orden original y reverso, siempre que haya mas de un caracter en la cola y sea palindromo 
        if cola.popleft() != cola.pop():# con if Comparamos el primer y último elemento de la cola, utilizando append y pop
                                        # Si los caracteres no son iguales, la palabra no es palíndroma
           palindromo = False

    return palindromo #entonces la funcion retorna True si es palindromo, de lo contrario retorna False

# Ejemplo
palabra = "reconocer"
if es_palindromo(palabra):
    print(f"{palabra} es palíndroma.")
else:
    print(f"{palabra} no es palíndroma.")



# Importamos la clase deque del módulo collections
from collections import deque

# Definimos una clase llamada GestionarPedidos
class GestionarPedidos:
    # Método de inicialización de la clase
    def __init__(self): ## con el método de inicialización de la clase y creamos una cola que almacene pedidos
        self.cola_pedidos = deque()

    
    def agregar_pedido(self, pedido):# definimos el método para agregar un pedido a la cola utilizando append 
        self.cola_pedidos.append(pedido)


    
    def procesar_pedido(self):# definimos el método para procesar un pedido de la cola
        
        if self.cola_pedidos: # si hay pedidos en la cola extraemos y procesamos el primero de la cola utilizando popleft
            pedido = self.cola_pedidos.popleft()

        else: 
            
            print("No hay pedidos para procesar.") # de lo contrario solo imprimimos un mensaje indicando que no hay pedidos para procesar

    
    def mostrar_estado_cola(self):# definimos el método para mostrar el estado actual de la cola de pedidos
    
        if self.cola_pedidos:   # Verificamos si hay pedidos en la cola, si eso ocurre imprimimos un mensaje indicando el estado actual de la cola
            print("Estado actual de la cola de pedidos:")
           
            for indice, pedido in enumerate(self.cola_pedidos, start=1): # Iteramos sobre los pedidos en la cola e imprimimos cada uno con su índice
                print(f"{indice}. {pedido}")
        else:
            print("La cola de pedidos está vacía.")# Si la cola está vacía, imprimimos un mensaje indicando que la cola está vacía

#ejempplo: un del sistema de gestion de pedidos una heladeria
# Creamos una instancia de la clase GestionarPedidos

sistema = GestionarPedidos()

sistema.agregar_pedido("helado de chocolate")
sistema.agregar_pedido("capuccino")# Agregamos algunos pedidos de los productos de la heladeria a la cola utilizando el método agregar_pedido()
sistema.agregar_pedido("cafe helado")


sistema.mostrar_estado_cola()# con el método mostrar_estado_cola() se muestra el estado actual de la cola de pedidos 


sistema.procesar_pedido()
sistema.procesar_pedido()# Procesamos algunos pedidos de la cola utilizando el método procesar_pedido()
sistema.procesar_pedido()


sistema.mostrar_estado_cola()# Mostramos nuevamente el estado actual de la cola de pedidos

# 3. Desarrolla un programa que encuentre el camino más corto a través de un laberinto. Utiliza una cola
# para realizar un recorrido en anchura (BFS) desde el punto de inicio hasta el punto de destino.

from collections import deque

# Definimos una función para encontrar el camino más corto a través del laberinto
def encontrar_camino_laberinto(laberinto, inicio, destino):
    # Definimos las direcciones posibles para moverse (arriba, abajo, izquierda, derecha)
    direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # Obtenemos las dimensiones del laberinto
    filas = len(laberinto)
    columnas = len(laberinto[0])
    # Creamos una cola para realizar el recorrido en anchura
    cola = deque()
    # Agregamos el punto de inicio a la cola
    cola.append(inicio)
    # Creamos un conjunto para almacenar los nodos visitados
    visitados = set()
    # Marcamos el punto de inicio como visitado
    visitados.add(inicio)
    # Creamos un diccionario para almacenar los padres de cada nodo (para reconstruir el camino)
    padres = {inicio: None}

    # Mientras haya nodos en la cola
    while cola:
        # Sacamos el nodo actual de la cola
        nodo_actual = cola.popleft()
        # Si llegamos al destino, terminamos la búsqueda
        if nodo_actual == destino:
            break
        # Exploramos las direcciones posibles desde el nodo actual
        for direccion in direcciones:
            # Calculamos las coordenadas del siguiente nodo
            fila_nueva = nodo_actual[0] + direccion[0]
            columna_nueva = nodo_actual[1] + direccion[1]
            # Verificamos si las coordenadas están dentro del laberinto y el nodo no ha sido visitado
            if 0 <= fila_nueva < filas and 0 <= columna_nueva < columnas and laberinto[fila_nueva][columna_nueva] != '#' and (fila_nueva, columna_nueva) not in visitados:
                # Agregamos el nuevo nodo a la cola y lo marcamos como visitado
                cola.append((fila_nueva, columna_nueva))
                visitados.add((fila_nueva, columna_nueva))
                # Guardamos el padre del nuevo nodo
                padres[(fila_nueva, columna_nueva)] = nodo_actual

    # Reconstruimos el camino más corto desde el punto de inicio hasta el destino
    camino = []
    nodo_actual = destino
    while nodo_actual is not None:
        camino.append(nodo_actual)
        nodo_actual = padres[nodo_actual]
    camino.reverse()

    return camino

# Ejemplo
laberinto = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '.', '#', '.', '#', '#', '#', '#'],
    ['#', '.', '#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]
inicio = (1, 1)  # Coordenadas del punto de inicio
destino = (3, 8)  # Coordenadas del punto de destino

# Llamamos a la función para encontrar el camino más corto en el laberinto
camino = encontrar_camino_laberinto(laberinto, inicio, destino)

# Si se encontró un camino, se imprime; de lo contrario se indica que no se encontró un camino válido
if camino:
    print("Camino más corto encontrado:")
    for paso in camino:
        print(paso)
else:
    print("No se encontró un camino válido.")
    
#4. Implementa un sistema de gestión de tareas que permita agregar tareas, marcar tareas como
# completadas y mostrar la próxima tarea pendiente.



from collections import deque


class SistemaGestionTareas:# Definimos una clase llamada GestionarTareas 
    
    def __init__(self):
        self.tareas_pendientes = deque() # Creamos una cola vacía para almacenar las tareas pendientes

    
    def agregar_tarea(self, tarea):# metodo para agregar una tarea a la cola de tareas pendientes
        
        self.tareas_pendientes.append(tarea)# Agregamos la tarea a la cola utilizando el método append() de deque
        print(f"Tarea agregada: {tarea}")#confirmamos que la tarea ha sido agregada

    
    def tarea_completada(self, tarea):# metodo para marcar una tarea como completada
        try:
            # removemos la tarea de la cola de tareas pendientes
            self.tareas_pendientes.remove(tarea)
           
            print(f"Tarea completada: {tarea}") # Si la tarea existe y fue removida con éxito se imprime un mensaje de confirmación
        except ValueError:
            print(f"No se encontró la tarea: {tarea}")# Si la tarea no se encontró en la cola, imprimimos un mensaje
    
    def mostrar_proxima_tarea_pendiente(self):# método para mostrar la próxima tarea pendiente en la cola
        # Verificamos si hay tareas pendientes en la cola
        if self.tareas_pendientes: # si hay tareas pendientes en la cola, imprimimos la primera tarea de la cola de lo contraio imprimimos un mensaje indicando que no hay tareas pendientes

            print(f"Próxima tarea pendiente: {self.tareas_pendientes[0]}")
        else:
            print("No hay tareas pendientes.")

# Ejemplo 
sistema = SistemaGestionTareas()


sistema.agregar_tarea("Hacer la compra")# Agregamos algunas tareas al sistema
sistema.agregar_tarea("Llamar al cliente")
sistema.agregar_tarea("Enviar informe")
sistema.mostrar_proxima_tarea_pendiente()# mostramos la próxima tarea pendiente en la cola
sistema.marcar_completada("Hacer la compra")# marcamos una tarea como completada
sistema.mostrar_proxima_tarea_pendiente()# mostramos la próxima tarea pendiente después de marcar una como completada
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


# PILAS
# -----------------------------------------------
from collections import deque

# 1. Verificar si una palabra es palíndroma
class Cola:
    def __init__(self):
        # Inicializa la cola como una lista vacía
        self.items = []

    def esta_vacia(self):
        # Verifica si la cola está vacía
        return len(self.items) == 0

    def encolar(self, item):
        # Agrega un elemento al final de la cola
        self.items.append(item)

    def desencolar(self):
        # Elimina y devuelve el primer elemento de la cola
        if self.esta_vacia():
            return None
        return self.items.pop(0)

def es_palindromo(palabra):
    # Crea una instancia de la clase Cola
    cola = Cola()
    # Encola cada letra de la palabra en la cola
    for letra in palabra:
        cola.encolar(letra)
    # Inicializa una cadena vacía para almacenar la palabra invertida
    palabra_reverso = ""
    # Desencola las letras de la cola y las agrega en orden inverso a palabra_reverso
    while not cola.esta_vacia():
        palabra_reverso += cola.desencolar()
    # Compara la palabra original con la palabra invertida para determinar si es un palíndromo
    return palabra == palabra_reverso


palabra = "reconocer"
if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")


# -----------------------------------------------
# 2. Diseño de un sistema de gestión de pedidos
class ColaPedidos:
    def __init__(self):
        self.pedidos = []

    def agregar_pedido(self, pedido):
        # Agrega un pedido a la cola de pedidos
        self.pedidos.append(pedido)

    def procesar_pedido(self):
        if self.pedidos:
            # Si hay pedidos en la cola, extrae y devuelve el primero
            return self.pedidos.pop(0)
        else:
            # Si no hay pedidos, devuelve un mensaje indicando que no hay pedidos para procesar
            return "No hay pedidos para procesar"

    def mostrar_estado(self):
        if self.pedidos:
            # Si hay pedidos en la cola, muestra el estado enumerando los pedidos en espera
            print("Pedidos en espera:")
            for pedido in self.pedidos:
                print("-", pedido)
        else:
            # Si no hay pedidos, indica que no hay pedidos en espera
            print("No hay pedidos en espera")


cola_pedidos = ColaPedidos()
# Agregar algunos pedidos
cola_pedidos.agregar_pedido("Pedido 1: Pizza")
cola_pedidos.agregar_pedido("Pedido 2: Hamburguesa")
cola_pedidos.agregar_pedido("Pedido 3: Sushi")

# Mostrar el estado actual de la cola de pedidos
cola_pedidos.mostrar_estado()

# Procesar los pedidos en el orden en que fueron recibidos
print("\nProcesando pedidos:")
print(cola_pedidos.procesar_pedido())
print(cola_pedidos.procesar_pedido())
#print(cola_pedidos.procesar_pedido())

# Mostrar el estado actual de la cola de pedidos después de procesar los pedidos
print("\nEstado actual de la cola de pedidos:")
cola_pedidos.mostrar_estado()


# -----------------------------------------------
# 3. Búsqueda de rutas en un laberinto
# Definición de las direcciones posibles: arriba, abajo, izquierda, derecha
direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs_laberinto(laberinto, inicio, fin):
    # Dimensiones del laberinto
    filas = len(laberinto)
    columnas = len(laberinto[0])
    # Cola para BFS
    cola = deque()
    cola.append(inicio)
    # Conjunto para almacenar las celdas visitadas
    visitado = set()
    visitado.add(inicio)
    # Diccionario para almacenar el camino
    camino = {}
    camino[inicio] = None
    while cola:
        fila, columna = cola.popleft()
        # Si llegamos al destino, reconstruimos el camino y lo devolvemos
        if (fila, columna) == fin:
            camino_reconstruido = reconstruir_camino(camino, inicio, fin)
            return camino_reconstruido
        # Exploramos las direcciones posibles desde la celda actual
        for df, dc in direcciones:
            nueva_fila, nueva_columna = fila + df, columna + dc
            # Verificamos si la nueva celda está dentro del laberinto y no está bloqueada
            if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and laberinto[nueva_fila][nueva_columna] != "#":
                nueva_celda = (nueva_fila, nueva_columna)
                if nueva_celda not in visitado:
                    cola.append(nueva_celda)
                    visitado.add(nueva_celda)
                    camino[nueva_celda] = (fila, columna)
    return None


# Función para reconstruir el camino más corto a través del laberinto
def reconstruir_camino(camino, inicio, fin):
    # Inicialización de la lista para almacenar el camino reconstruido
    camino_reconstruido = []
    actual = fin
    
    # Recorrido inverso desde el punto final hasta el punto inicial
    while actual != inicio:
        camino_reconstruido.append(actual)
        actual = camino[actual]
    
    # Añadir el punto inicial al camino reconstruido
    camino_reconstruido.append(inicio)
    
    # Invertir el camino reconstruido para obtener el orden correcto
    camino_reconstruido.reverse()
    
    return camino_reconstruido

# Laberinto de ejemplo representado como una matriz de caracteres
    # "S" indica el punto de inicio.
    # "." indica un espacio libre por el que se puede pasar.
    # "#" indica una pared o bloqueo que no se puede atravesar.
    # "E" indica el punto de destino o salida del laberinto.
laberinto = [
    ["S", ".", ".", "#", ".", "."],
    [".", "#", ".", "#", ".", "."],
    [".", "#", ".", ".", ".", "#"],
    [".", ".", "#", "#", ".", "E"],
    [".", ".", ".", ".", ".", "."]
]

# Coordenadas de inicio y fin en el laberinto
inicio = (0, 0)
fin = (3, 5)

camino_mas_corto = bfs_laberinto(laberinto, inicio, fin)

# Si se encontró un camino, mostrar el laberinto con el camino marcado con "*"
if camino_mas_corto:
    print("Camino más corto encontrado:")
    for fila, columna in camino_mas_corto:
        laberinto[fila][columna] = "*"
    for fila in laberinto:
        print(" ".join(fila))
else:
    print("No se encontró un camino desde el punto de inicio al punto de destino.")


# -----------------------------------------------
# 4. Diseño de un sistema de gestión de tareas (Avanzado)
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

class SistemaGestionTareas:
    def __init__(self):
        # Inicialización de la lista de tareas
        self.tareas = []

    def agregar_tarea(self, descripcion):
        # Método para agregar una nueva tarea a la lista
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)

    def marcar_completada(self, indice):
        # Método para marcar una tarea como completada dado su índice en la lista
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True
        else:
            print("Índice de tarea no válido.")

    def proxima_tarea_pendiente(self):
        # Método para encontrar la próxima tarea pendiente en la lista
        for tarea in self.tareas:
            if not tarea.completada:
                return tarea.descripcion
        return "¡Felicidades! No hay tareas pendientes."

# Creación de una instancia de SistemaGestionTareas y manipulación de las tareas
sistema_tareas = SistemaGestionTareas()

# Agregar nuevas tareas al sistema
sistema_tareas.agregar_tarea("Hacer la compra")
sistema_tareas.agregar_tarea("Estudiar para el examen")
sistema_tareas.agregar_tarea("Llamar al cliente")

# Mostrar la próxima tarea pendiente y marcar una tarea como completada
print("Próxima tarea pendiente:", sistema_tareas.proxima_tarea_pendiente())
sistema_tareas.marcar_completada(0)
print("Próxima tarea pendiente:", sistema_tareas.proxima_tarea_pendiente())

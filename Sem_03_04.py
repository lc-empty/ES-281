import numpy as np
from typing import Tuple

# Exercises part I

# ---------------------------------------------------------------------------------------
# Recursive functions
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------
# 01: Escribe una función recursiva que imprima los números pares del 1 al 100.
# Se define la función print_even_numbers usando "type hints"
def print_even_numbers(n: int = 1) -> None:
    """
    Esta función imprime los números pares de 1 a 100

    Parameters:
        n (int, optional): limite superior

    Returns:
        None

    """
    if n == 100:
        # caso base: se detiene si es 100
        return
    if n % 2 == 0:
        # imprime los números pares de 1 a 100
        print(n, end=" - ")
    # caso recursivo: llama a la función pasando como argumento el siguiente número
    print_even_numbers(n + 1)

# llamada de la función
# print_even_numbers()


# ---------------------------------------------------------------------------------------
# 02: Escribe una función recursiva que imprima la suma de los números del 1 al n
def recursive_sum(current_number: int, target_number: int, current_sum: int = 0) -> None:
    """
    Imprime la suma de los números del 1 al n

    Parameters:
        current_number (int): número actual
        target_number (int): número final
        current_sum (int, optional): suma actual

    Returns:
        None
    """
    if current_number > target_number:
        # caso base, termina con la ejecución
        return
    # almacena en current_sum la suma de current_sum + current_number
    current_sum: int =current_sum + current_number
    # imprime la suma actual
    print(current_sum)
    # caso recursivo: llama a la función
    recursive_sum(current_number + 1, target_number, current_sum)

# llamada de la función
# recursive_sum(1, 5)


# ---------------------------------------------------------------------------------------
# 03: Escribe una función recursiva que imprima la pirámide de números del 1 al n
def print_number_pyramid(n: int, current_row: int = 1) -> None:
    """
    Imprime la pirámide de números del 1 al n

    Parameters:
        n (int): número de filas de la pirámide
        current_row (int, optional): fila actual de la pirámide

    Returns:
        None

    """
    if current_row > n:
        # caso base: Se detiene si n es 100
        return

    # imprime espacios antes de los números de la fila actual
    print(" " * (n - current_row), end="")

    # imprime los números de la fila actual de manera ascendente
    for num in range(1, current_row + 1):
        print(num, end="")
    # imprime los números de la fila actual de manera descendente
    for num in range(current_row - 1, 0, -1):
        print(num, end="")

    # pasar a la siguiente línea después de imprimir la fila.
    print()

    # caso recursivo: imprime recursivamente la siguiente fila
    print_number_pyramid(n, current_row + 1)

# llamada de la función
# print_number_pyramid(9)


# ---------------------------------------------------------------------------------------
# 04: Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n
def print_inverted_number_pyramid(n: int, current_row: int = 1) -> None:
    """
    Imprime la pirámide de números invertidos del 1 al n.

    Parameters:
        n (int): número de filas de la pirámide
        current_row (int, optional): la fila actual que se está imprimiendo

    Returns:
        None
    """
    if current_row > n:
        # caso base: Se detiene si current_row es mayor a n
        return

    # imprime espacios antes de los números invertidos de la fila actual
    print(" " * (n - current_row), end="")

    # imprime los números de la fila actual de manera descendente
    for num in range(current_row, 0, -1):
        print(num, end="")

    # imprime los números de la fila actual de manera ascendente
    for num in range(2, current_row + 1):
        print(num, end="")

    # pasar a la siguiente línea después de imprimir la fila.
    print()

    # caso recursivo: imprime recursivamente la siguiente fila
    print_inverted_number_pyramid(n, current_row + 1)

# llamada de la función
# print_inverted_number_pyramid(6)


# ---------------------------------------------------------------------------------------
# 05:  Escribe una función recursiva que imprima la tabla de multiplicar del n.
def print_multiplication_table(n: int, multiplier: int = 1) -> None:
    """
    Imprime la tabla de multiplicar del n.

    Parameters:
        n (int): el número para el cual se imprimirá la tabla de multiplicar
        multiplier (int, optional): el multiplicador de la fila de la tabla

    Returns:
        None

    """
    if multiplier > 10:
        # caso base: esta instrucción if verifica si el multiplicador es mayor que 10.
        return
    # esta variable almacena el producto de n y el multiplicador actual
    result: int = n * multiplier
    # el resultado (entero) se imprime usando la sintaxis de format (f), \t: carácter de tabulación
    print(f"\t{n} x {multiplier} = {result}")
    # caso recursivo: esta función se llama de forma recursiva para imprimir la siguiente fila
    print_multiplication_table(n, multiplier + 1)

# llamada de la función
# print_multiplication_table(5)


# ---------------------------------------------------------------------------------------
# Arreglos y Matrices
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------
# 06: Crea una matriz de números reales
# usando types hints (np.ndarray para matrizes)
def real_matrix() -> np.ndarray:
    """
    Crea una matriz de números reales.

    Returns:
        np.ndarray: matriz de números reales.
    """
    return np.array([
        [7, 2, 5],
        [4, 5, 8],
        [6, 0, 9]
    ])

# llamada de la función
# print(real_matrix())


# ---------------------------------------------------------------------------------------
# 07: Crea una matriz de números complejos
def complex_matrix() -> np.ndarray:
    """
    Crea una matriz de números complejos.

    Returns:
        np.ndarray: matriz de números complejos.
    """
    return np.array([
        [1 + 2j, 3 + 4j, 6 + 5j],
        [5 + 6j, 7 + 8j, 0],
        [9 + 1j, 2, 2j]
    ], dtype=complex)

# llamada de la función
# print(complex_matrix())


# ---------------------------------------------------------------------------------------
# 08: Crea una matriz de matrices
def matrix_matrix() -> np.ndarray:
    return np.array([
        [8, 9, 3, 5],
        [9, 4, 0, 2],
        [0, 5, 2, 1],
        [7, 8, 9, 0]
    ])

# llamada de la función
# print(matrix_matrix())

# Función lambda para crear matrices aleatorias, recibe 2 parametros, el número de filas y el número de columnas.
random_matrix_generator: np.ndarray = lambda rows, cols: np.random.randint(1, 10, size=(rows, cols))


# ---------------------------------------------------------------------------------------
# 09: Accede al elemento central de una matriz
def central_matrix(matrix: np.ndarray) -> np.ndarray:
    """
    Accede al elemento central de una matriz

    Parameters:
        matrix (np.ndarray): Matriz

    Returns:
        float: Elemento central de la matriz
    """
    if matrix.shape[0] != matrix.shape[1]:
        # Verifica que sea una matriz cuadrada
        return 'matriz de dimensiones incorrectas'
    return matrix[int(matrix.shape[0] / 2)][int(matrix.shape[1] / 2)]

# creando la matriz A con la función random_matrix_generator
# A: np.ndarray = random_matrix_generator(5, 5)
# la matriz A
# print(f"La matriz A es:\n{A}\n")
# llamada de la función
# num_central: int = central_matrix(A)
# print(f'El elemento central de la matriz A es: {num_central}')





# ---------------------------------------------------------------------------------------
# 10:  Suma dos matrices de diferentes tamaños.
def matrix_sum(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Suma dos matrices de diferentes tamaños.

    Parameters:
        A (np.ndarray): La primera matriz
        B (np.ndarray): La segunda amtriz

    Returns:
        np.ndarray: La suma de las matrices
    """
    # Usamos concatenate() de numpy para concatenar matrices de diferentes tamaños.
    result_matrix: np.ndarray = A + B
    return result_matrix

# creando la matriz A, B con la función random_matrix_generator
# A: np.ndarray = random_matrix_generator(3, 3)
# la matriz A
# print(f"La matriz A es:\n{A}\n")
# la matriz B
# B: np.ndarray = random_matrix_generator(3, 3)
# print(f"La matriz B es:\n{B}\n")
# llamada de la función, pasandole como arguemnto la matriz A y la matriz B
# sum_matrix: np.ndarray = matrix_sum(A, B)
# print(f'Suma de las matrices es:\n{sum_matrix}')


# ---------------------------------------------------------------------------------------
# 11: Multiplica una matriz por un número.
def multiply_matrix_by_scalar(matrix: np.ndarray, scalar: float) -> np.ndarray:
    """
    Multiplica una matriz por un número.

    Parameters:
        matrix (np.ndarray): Matriz
        scalar (float): Número

    Returns:
        np.ndarray: Matriz multiplicada por el número
    """
    return matrix * scalar

# creamos la matriz X, hacemos uso de la función multiply_matrix_by_scalar
# X: np.ndarray = random_matrix_generator(3, 3)
# print(f'la matriz X es:\n{X}\n')
# scalar_dot_matrix: np.ndarray = multiply_matrix_by_scalar(X, 6)
# print(f'La matriz multiplicada por 6 es:\n{scalar_dot_matrix}\n')


# ---------------------------------------------------------------------------------------
# 12:  Calcula la media de los elementos de una matriz
def matrix_mean(matrix: np.ndarray) -> float:
    """
    Calcula la media de los elementos de una matriz

    Parameters:
        matrix (np.ndarray): Matriz

    Returns:
        float: Media
    """
    return np.mean(matrix)

# usamos la matriz X anteriormente creada, hacemos uso de la funcion matrix_mean
# mean_matrix: float = matrix_mean(X)
# print(f'La media de la matriz es: {mean_matrix}\n')


# =======================================================================================
# Exercises part II
# =======================================================================================

# ---------------------------------------------------------------------------------------
# 01: Crea una matriz de números aleatorios de tamaño 100x100
def random_matrix() -> np.ndarray:
    # crea una matriz de números aleatorios de tamaño 100 x 100
    return np.random.rand(100, 100)

# llamada de la función
# matrix_random: np.ndarray = random_matrix()
# print(f'matriz aleatoria de tamaño 100x100 es:\n{matrix_random}')


# ---------------------------------------------------------------------------------------
# 02: Calcula la media, la mediana y la desviación estándar de los elementos de una matriz
def calculate_statistics(matrix: np.ndarray) -> Tuple[float, float, float]:
    """
    Calcula la media, mediana y desviación estándar de los elementos de una matriz

    Parameters:
        matrix (np.ndarray): Matriz

    Returns:
        Tuple[float, float, float]: Una tupla que contiene la media, la mediana y la desviación estándar
    """
    # calcula la media
    mean_value = np.mean(matrix)
    # llama la función matrix_mean para obtener la media de la matriz
    median_value = matrix_mean(matrix)
    # calcula la desviación estándar
    std_deviation = np.std(matrix)

    return mean_value, median_value, std_deviation

# creamos la matriz A, llamamos a la función calculate_statistics
# A: np.ndarray = random_matrix_generator(5, 5)
# print(f"La matriz A es:\n{A}\n")
# usando la asignación múltiple o desempaquetado de tuplas en Python tenemos:
# mean_value, median_value, std_deviation = calculate_statistics(A)
# print(mean_value, median_value, std_deviation)

# ---------------------------------------------------------------------------------------
# 03: Escribe una función que encuentre el elemento máximo de una matriz
def find_max_element(matrix: np.ndarray) -> float:
    """
    Encuentra el elemento máximo de una matriz

    Parameters:
        matrix (np.ndarray): Matriz

    Returns:
        float: El elemento máximo de la matriz
    """
    # calcula el máximo elemento de la matriz
    return np.max(matrix)

# creamos la matriz B, llamamos a la función calculate_statistics
# B: np.ndarray = random_matrix_generator(5, 5)
# max_element: float = find_max_element(B)
# print(f"Matriz B:\n{B}")
# print(f"Elemento máximo: {max_element}")


# ---------------------------------------------------------------------------------------
# 04: Escribe una función que encuentre la submatriz de mayor suma de una matriz
def find_submatrix_max(matrix: np.ndarray, count: int) -> [np.ndarray, int]:
    """
    Encuentra la submatriz de mayor suma de una matriz

    Parameters:
        matrix (np.ndarray): Matriz
        count (int): Número de elementos a obtener

    Returns:
        Tuple[np.ndarray, int]: Una tupla que contiene la submatriz de mayor suma y el valor de la suma
    """
    # convertirmos la matriz en un arreglo
    arr_numbers = np.array(matrix).flatten()

    if count <= 0:
        # Si count es 0 o negativo, retornar un arreglo vacío
        return []

    # Ordenar el arreglo en orden descendente
    sorted_arr = sorted(arr_numbers, reverse=True)
    # Obtener los primeros count elementos
    result_arr = sorted_arr[:count]

    # Obtener la suma
    sum_arr: int = sum(result_arr)

    return result_arr, sum_arr


# Creamos una matriz de 5 x 5 con random_matrix_generator
# matrix: np.ndarray = random_matrix_generator(5, 5)
# print(f"Matriz:\n{matrix}\n")
# usamos asignación múltiple para alamcenar los valores que nos retorna la función
# submatrix, sum = find_submatrix_max(matrix, matrix.shape[0])
# print(f"submatriz: {submatrix} y la suma: {sum}")


# ---------------------------------------------------------------------------------------
# 05: Escribe una función que encuentre la matriz de covarianza de dos matrices
def covariance_matrix(matrix_a: np.ndarray, matrix_b: np.ndarray) -> np.ndarray:

    if matrix_a.shape != matrix_b.shape:
        raise ValueError("Matrices must have the same shape for covariance calculation.")

    # Apilar las matrices para obtener una matriz combinada
    combined_matrix = np.vstack((matrix_a, matrix_b))

    # Calcular la matriz de covarianza
    # rowvar=False se utiliza para tratar cada columna como una variable y cada fila como una observación
    covariance_matrix = np.cov(combined_matrix, rowvar=False)

    return covariance_matrix

# creamos matrices: X e Y, llamamos a la función covariance_matrix
# X: np.ndarray = random_matrix_generator(5, 5)
# Y: np.ndarray = random_matrix_generator(5, 5)
# matrix_covariance: np.ndarray = covariance_matrix(X, Y)
# print(f"Matriz A:\n{X}\n")
# print(f"Matriz B:\n{Y}\n")
# print(f'Matriz de covarianza:\n{matrix_covariance}\n')
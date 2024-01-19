# -------------------------------------------------------------------------------------------------------
# 1. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números primos.
numeros = set()

def conjunto_numeros_primos(numeros):
    numero = int(input("ingrese numero:"))
    respuesta = "si"
    while respuesta == "si":
        numero = float(input("ingrese numero:"))
        if numero % 1 == 0 and numero % numero == 0:
            numeros.add(numero)
        respuesta = input("desea ingresar otro numero?:")
    return numeros

print(conjunto_numeros_primos(numeros))

# -------------------------------------------------------------------------------------------------------
# 2. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las
# palabras que comienzan con una letra determinada.
palabras = ["mora", "cereza", "ciruela", "coco"]
conjunto_palabra = set(palabras)

def palabras(conjunto_palabra):
    palabras_iniciales = set()
    letra = input("letra:")
    for palabra in conjunto_palabra:
        if letra in palabra:
            palabras_iniciales.add(palabra)
    return palabras_iniciales

print(palabras(conjunto_palabra))

# -------------------------------------------------------------------------------------------------------
# 3. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que son
# divisibles por un número determinado.
numeros = {1, 2, 3, 4, 5, 6}

def conjunto_numeros(numeros):
    numeros_divisibles = set()
    numero = int(input("ingrese numero:"))
    for i in numeros:
        if i % numero == 0:
            numeros_divisibles.add(numero)
    return numeros_divisibles

print(conjunto_numeros(numeros))

# -------------------------------------------------------------------------------------------------------
# 4. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están
# en ambos conjuntos.
conjunto1 = {1, 3, 4, 65, 89, 9}
conjunto2 = {5, 3, 6, 8, 4, 87}

def union_conjuntos(conjunto1, conjunto2):
    nuevo_conjunto = conjunto2.union(conjunto1)
    return nuevo_conjunto

print(union_conjuntos(conjunto1, conjunto2))

# -------------------------------------------------------------------------------------------------------
# 5. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están
# en el primer conjunto pero no en el segundo.
conjunto1 = {1, 3, 4, 65, 89, 9}
conjunto2 = {5, 3, 6, 8, 4, 87}

def diferencia_conjuntos(conjunto1, conjunto2):
    conjunto_nuevo = set()
    for i in conjunto1:
        if i not in conjunto2:
            conjunto_nuevo.add(i)
    return conjunto_nuevo

print(diferencia_conjuntos(conjunto1, conjunto2))

# -------------------------------------------------------------------------------------------------------
# 6. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están
# en el segundo conjunto pero no en el primero.
conjunto1 = {1, 3, 4, 65, 89, 9}
conjunto2 = {5, 3, 6, 8, 4, 87}

def diferencia_conjuntos(conjunto1, conjunto2):
    conjunto_nuevo = set()
    for i in conjunto2:
        if i not in conjunto1:
            conjunto_nuevo.add(i)
    return conjunto_nuevo

print(diferencia_conjuntos(conjunto1, conjunto2))


# -------------------------------------------------------------------------------------------------------
# 7. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
# son anagramas.

# -------------------------------------------------------------------------------------------------------
# 8. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos.
def palabras_palindromo(palabras):
    palabrasPalindromo = set()
    for palabra in palabras:
        if palabra == palabra[::-1]:
            palabrasPalindromo.add(palabra)
    return palabrasPalindromo

palabras = {"oso", "radar", "casa", "reconocer"}
print(palabras_palindromo(palabras))

# -------------------------------------------------------------------------------------------------------
# 9. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que tienen una longitud determinada.
def palabras_tamano(palabras):
    palabrasTamañoIgual = set()
    tamaño = int(input("Tamaño: "))
    for i in palabras:
        if len(i) == tamaño:
            palabrasTamañoIgual.add(i)
    return palabrasTamañoIgual

palabras = {"manzana", "pera", "uva", "kiwi"}
print(palabras_tamano(palabras))

# -------------------------------------------------------------------------------------------------------
# 10. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que contienen una letra determinada.
def palabras_con_letra(conjunto_palabra):
    palbrasInicial = set()
    letra = input("Letra: ")
    for palabra in conjunto_palabra:
        if letra in palabra:
            palbrasInicial.add(palabra)
    return palbrasInicial

palabras = {"mora", "cereza", "ciruela", "coco"}
conjunto_palabra = set(palabras)
print(palabras_con_letra(conjunto_palabra))

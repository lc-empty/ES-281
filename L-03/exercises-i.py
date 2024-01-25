# -------------------------------------------------------------------------------------------------------
# 1. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números primos.
conjunto_numeros = {7,8,9,1,3,11,5,6,8,20,47}
def imprimir_conjunto_numeros_primos(conjunto_numeros):
    conjunto_numeros_primos =set()
    for numero in conjunto_numeros:
        divisores = 0
        for i in range(1,numero+1):
            if numero % i == 0:
                divisores = divisores + 1
        if divisores == 2:
            conjunto_numeros_primos.add(numero)
    return sorted(conjunto_numeros_primos)

# print (imprimir_conjunto_numeros_primos(conjunto_numeros ))

# -------------------------------------------------------------------------------------------------------
# 2. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las
# palabras que comienzan con una letra determinada.


palabras = ["mora" ,"cereza","ciruela","coco"]
conjunto_palabra=set(palabras)

def palabras(conjunto_palabra):
    palabras_inicial_iguales= set()
    letra= input("letra:")
    for palabra in conjunto_palabra:
        if letra == palabra[0]:
            palabras_inicial_iguales.add(palabra)
    return palabras_inicial_iguales


# print (palabras(conjunto_palabra))

# -------------------------------------------------------------------------------------------------------
# 3. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que son
# divisibles por un número determinado.
numeros = {1, 2, 3, 4, 5, 6}

def conjunto_numeros(numeros):
    numeros_divisibles = set()
    numero = int(input("ingrese numero:"))
    for i in numeros:
        if i % numero == 0:
            numeros_divisibles.add(i)
    return numeros_divisibles

# print(conjunto_numeros(numeros))

# -------------------------------------------------------------------------------------------------------
# 4. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están
# en ambos conjuntos.


conjunto1 = {1,3,5,7,9,11,13,15,17,19}
conjunto2 = {23,11,17,13,2,7,5,3}

def mostar_conjunto_interseccion(conjunto1,conjunto2):
    conjunto_inteseccion = conjunto1.intersection(conjunto2)
    return sorted(conjunto_inteseccion)


# print(mostar_conjunto_interseccion(conjunto1,conjunto2))

# -------------------------------------------------------------------------------------------------------
# 5. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están
# en el primer conjunto pero no en el segundo.
conjunto1 = {3,4,5,13,24,56,2,6,7}
conjunto2 = {5,3,11,7,9,8,2,6,23,13}

def mostar_diferencia_conjuntos(conjunto1,conjunto2):
    conjunto_diferencia = conjunto1.difference(conjunto2)
    return sorted(conjunto_diferencia)


# print(mostar_diferencia_conjuntos(conjunto1,conjunto2))

# -------------------------------------------------------------------------------------------------------
# 6. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están
# en el segundo conjunto pero no en el primero.

conjunto1 = {3,4,5,13,24,56,2,6,7}
conjunto2 = {5,3,11,7,9,8,2,6,23,13}

def mostar_diferencia_conjuntos(conjunto1,conjunto2):
    conjunto3 = conjunto2.difference(conjunto1)
    return sorted(conjunto3)


# print(mostar_diferencia_conjuntos(conjunto1,conjunto2))


# -------------------------------------------------------------------------------------------------------
# 7. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
# son anagramas.
def son_anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

def encontrar_anagramas(conjunto_palabras):
    anagramas_dict = {}

    for palabra in conjunto_palabras:
        anagramas = [key for key in anagramas_dict if son_anagramas(palabra, key)]

        if anagramas:
            anagramas_dict[anagramas[0]].add(palabra)
        else:
            anagramas_dict[palabra] = {palabra}

    anagramas_resultado = {tuple(val) for val in anagramas_dict.values() if len(val) > 1}

    return anagramas_resultado

conjunto_palabras = {"amor", "roma", "carro", "arco", "delira", "ramo", "lidera"}
resultado = encontrar_anagramas(conjunto_palabras)
# print(resultado)

# -------------------------------------------------------------------------------------------------------
# 8. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos.
def palabras_palindromo(palabras):
    conjunto_palabras_palindromo = set()
    for palabra in palabras:
        if palabra == palabra[::-1]:
            conjunto_palabras_palindromo.add(palabra)
    return conjunto_palabras_palindromo

palabras = {"oso", "radar", "casa", "reconocer"}
# print(palabras_palindromo(palabras))

# -------------------------------------------------------------------------------------------------------
# 9. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que tienen una longitud determinada.

def palabras_tamaños_iguales(palabras):
    palabrasTamañoIgual = set()
    tamaño = int(input("Tamaño: "))
    for i in palabras:
        if len(i) == tamaño:
            palabrasTamañoIgual.add(i)
    return palabrasTamañoIgual

animales = {"mapache","cebra","escarabajo","ballena","merluza","bisonte","mariposa","flamenco"}
# print(palabras_tamaños_iguales(animales))

# -------------------------------------------------------------------------------------------------------
# 10. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que contienen una letra determinada.
def palabras(conjun_palabras): 
    palabras_letra_determinada= set()
    letra= input("letra:")
    for palabra in conjun_palabras:
        if letra in palabra:
            palabras_letra_determinada.add(palabra)
    return palabras_letra_determinada
    
utencilios_cocina = {"cuchillo","olla","sarten","espátula","cucharon","tenedor","colador"}
# rint (palabras(utencilios_cocina))

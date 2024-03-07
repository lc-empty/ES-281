# ------------------------------------------------------------------------------------
# 11. Escriba una función que reciba un conjunto de números y devuelva un conjunto con
#  los números que están ordenados de menor a mayor.
def order_numbers(numbers):
  numbers = list(numbers)
  numbers.sort()
  return set(numbers)


numbers = {6, 2, 3, 4, 2, 3}
ordered_numbers = order_numbers(numbers)
print(ordered_numbers)


# ------------------------------------------------------------------------------------
# 12. Función que devuelve un conjunto con los números ordenados de mayor a menor.
def numeros_ordenados_de_mayor_a_menor(conjunto):
    # Convertimos el conjunto a una lista y la ordenamos de mayor a menor
    lista_ordenada = sorted(conjunto, reverse=True)
    # Convertimos la lista ordenada de nuevo a un conjunto y la retornamos
    return set(lista_ordenada)

# conjunto = {3, 6, 1, 9, 4}
# resultado = numeros_ordenados_de_mayor_a_menor(conjunto)
# print(resultado) 


# ------------------------------------------------------------------------------------
# 13. Función que devuelve un conjunto con los números duplicados en el conjunto dado.
def numeros_duplicados(conjunto):
    # Creamos un conjunto vacío para almacenar los números duplicados
    duplicados = set()
    # Creamos un conjunto para almacenar los números únicos mientras recorremos el conjunto dado
    numeros_unicos = set()
    # Iteramos sobre cada número en el conjunto dado
    for numero in conjunto:
        # Si el número ya está en el conjunto de números únicos, significa que es duplicado
        if numero in numeros_unicos:
            duplicados.add(numero)  # Agregamos el número duplicado al conjunto de duplicados
        else:
            numeros_unicos.add(numero)  # Agregamos el número único al conjunto de números únicos
    # Retornamos el conjunto de números duplicados
    return duplicados

# conjunto = {3, 6, 1, 9, 4, 6, 2, 3}
# resultado = numeros_duplicados(conjunto)
# print(resultado) 


# ------------------------------------------------------------------------------------
# 14. Función que devuelve un conjunto con los números no duplicados en el conjunto dado.
def numeros_no_duplicados(conjunto):
    # Creamos un conjunto vacío para almacenar los números no duplicados
    no_duplicados = set()
    # Creamos un conjunto para almacenar los números duplicados mientras recorremos el conjunto dado
    duplicados = set()
    # Iteramos sobre cada número en el conjunto dado
    for numero in conjunto:
        # Si el número ya está en el conjunto de números duplicados, lo ignoramos
        if numero in duplicados:
            continue
        # Si el número ya está en el conjunto de números no duplicados, lo movemos al conjunto de duplicados
        elif numero in no_duplicados:
            no_duplicados.remove(numero)
            duplicados.add(numero)
        # Si el número no está en ninguno de los conjuntos, lo agregamos al conjunto de no duplicados
        else:
            no_duplicados.add(numero)
    # Retornamos el conjunto de números no duplicados
    return no_duplicados

# conjunto = {3, 6, 1, 9, 4, 6, 2, 3}
# resultado = numeros_no_duplicados(conjunto)
# print(resultado)

# ------------------------------------------------------------------------------------
# 15. Escriba una función que reciba un conjunto de números y devuelva un conjunto con
#  los números que son primos y están ordenados de menor a mayor.
def is_prime(number):
  if number <= 1:
    return False

  for divisor in range(2, int(number ** 0.5) + 1):
    if number % divisor == 0:
      return False
  return True

def primes(numbers):
  primes = set()
  for number in numbers:
    if is_prime(number):
      primes.add(number)
  return sorted(primes)


numbers = {23, 3, 5, 7, 13, 11, 19, 17, 2}
# print(primes(numbers))


# ------------------------------------------------------------------------------------
# 16. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con
#  las palabras que son palíndromos y están ordenadas de menor a mayor.
def palindromes(words):
  palindromes = set()
  for word in words:
    if word == word[::-1]:
      palindromes.add(word)
  return sorted(palindromes)


words = {"xyzyx", "elefante", "abcdcba", "pqrqp", "abcba", "abcde"}
# print(palindromes(words))


# ------------------------------------------------------------------------------------
# 17. Escriba  una  función  que  reciba  un  conjunto  de  palabras  y  devuelva  un
#  conjunto  con  las  palabras  que tienen una longitud determinada y están ordenadas de menor a mayor.
def words_with_length(words, length):
  words_with_length = set()
  for word in words:
    if len(word) == length:
      words_with_length.add(word)
  return sorted(words_with_length)


words = {"pqrst", "abcd", "xyz", "xxyyz", "adxc", "xd", "abcde"}
length = 5
# print(words_with_length(words, length))


# ------------------------------------------------------------------------------------
# 18. Escriba  una  función  que  reciba  un  conjunto  de  palabras  y  devuelva  un
#  conjunto  con  las  palabras  que contienen una letra determinada y están ordenadas de mayor a menor.
def words_with_letter(words, letter):
  words_with_letter = set()
  for word in words:
    if letter in word:
      words_with_letter.add(word)
  return sorted(words_with_letter, reverse=True)


words = {"abcd", "mknf", "xdda", "xyza"}
letter = "a"
# print(words_with_letter(words, letter))


# ------------------------------------------------------------------------------------
# 19. Escriba una función que reciba un conjunto de números y devuelva un conjunto con
#  los números que están ordenados de menor a mayor y que no están duplicados.
def unique_sorted_numbers(numbers):
  return numbers


numbers = {8, 1, 2, 3, 1, 2, 3, 4, 5, 6}
# print(numbers)
# print(unique_sorted_numbers(numbers))


# ------------------------------------------------------------------------------------
# 20.  Escriba una función que reciba un conjunto de palabras y devuelva un conjunto
# con las palabras que son palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor.
def palindromes(words, length):
  palindromes = set()
  for word in words:
    if len(word) == length and word == word[::-1]:
      palindromes.add(word)
  return sorted(palindromes)


words = {"xyzyx", "elefante", "abcdcba", "pqrqp", "abcba", "abcde"}
length = 5
# print(palindromes(words, length))

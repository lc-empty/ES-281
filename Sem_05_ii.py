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
# 12. Escriba una función que reciba un conjunto de números y devuelva un conjunto con
#  los números que están ordenados de mayor a menor.


# ------------------------------------------------------------------------------------
# 13. Escriba una función que reciba un conjunto de números y devuelva un conjunto con
#  los números que están duplicados.


# ------------------------------------------------------------------------------------
# 14. Escriba una función que reciba un conjunto de números y devuelva un conjunto con
#  los números que no están duplicados.



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
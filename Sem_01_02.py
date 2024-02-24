import math

# --------------------------------------------------------------------------------
# 1. Realiza la suma, resta, multiplicación y división de dos números ingresados por el usuario
# num1 = int(input("a:"))
# num2 = int(input("b:"))
# print(f"a + b:{num1+num2}\na - b:{num1-num2}\na xb:{num1*num2}\na/b:{num1/num2}")

# --------------------------------------------------------------------------------
# 2. Solicita un número al usuario y determina si es par o impar.
# numero = int(input("numero:"))

# if numero % 2 == 0:
#     print(f"{numero} es par")
# else:
#     print(f"{numero} es impar")

# --------------------------------------------------------------------------------
# 3. Pide la base y la altura de un triángulo al usuario y calcula su área.
# base = float(input("base:"))
# altura = float(input("altura:"))
# area = base*altura

# print(f"area del triangulo: {area}")

# --------------------------------------------------------------------------------
# 4. Crea una función que calcule la factorial de un número.
# def factorial (n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial (n-1)
# print(factorial(7))

# --------------------------------------------------------------------------------
# 5. Verifica si un número ingresado por el usuario es primo o no.
# def es_primo(n):
#     es_primo = True
#     for i in range(2, n):
#         if n % i == 0:
#             es_primo = False
#             break
#     return es_primo

# n = int(input("Ingrese un número: "))

# es_primo = es_primo(n)

# if es_primo:
#     print(n, "es primo.")
# else:
#     print(n, "no es primo.")

# --------------------------------------------------------------------------------
# 6. Toma una cadena de texto y muestra su inversión.
# def invertir_cadena(cadena):
#     return cadena[::-1]

# cadena = "Hola, mundo!"

# invertida = invertir_cadena(cadena)

# print("La cadena invertida es:", invertida)

# --------------------------------------------------------------------------------
# 7. Calcula la suma de los números pares en un rango especificado por el usuario.
def sum_peers(start, end):
    sum: int = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            sum += i
    return sum

def sum_range_peers():
    initial: int = int(input("Enter the start of the range: "))
    end: int = int(input("Enter the end of the range: "))
    return sum_peers(initial, end)

# print(sum_range_peers())

# --------------------------------------------------------------------------------
# 8. Crea una lista de los cuadrados de los primeros 10 números naturales
def array_sqrt(num):
    arr_sqrt: [int] = []
    for i in range(1, num + 1):
        arr_sqrt.append(i * i)

    return arr_sqrt

# print(array_sqrt(10))

# --------------------------------------------------------------------------------
# 9. Cuenta el número de vocales en una cadena de texto.
def count_vowels(text):
    count: int = 0
    for i in text:
        if i in "aeiouAEIOUáéíóú":
            count += 1
    return count

# print(count_vowels("This is a new text"))

# --------------------------------------------------------------------------------
# 10. Genera los primeros 10 números de la serie Fibonacci.
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def array_fibonacci(num):
    array: [int] = []
    for i in range(num):
        array.append(fibonacci(i))
    return array

# print(array_fibonacci(10))


# --------------------------------------------------------------------------------
# 11. Ordena una lista de números ingresados por el usuario de menor a mayor.
def arr_numbers_sort():
    arr_numbers: [int] = []
    for i in range(int(input("How many numbers do you want to enter? "))):
        arr_numbers.append(int(input(f"Number {i + 1}: ")))

    arr_numbers.sort()

    return arr_numbers

# print(arr_numbers_sort())

# --------------------------------------------------------------------------------
# 12. Verifica si una palabra ingresada por el usuario es un palíndromo.
# def palindromo(text: str):
#     long: int = len(text)
#     half: int = long // 2

#     for i in range(0, half):
#         if text[i] != text[long - i - 1]:
#             return False

#     return True

# text: str = input("input the text: ")

# text_palindromo = palindromo(text)

# if text_palindromo:
#     print(text, "is palindromo.")
# else:
#     print(text, "not is palindromo.")

# --------------------------------------------------------------------------------
# 13. Crea un programa que genere la tabla de multiplicar de un número ingresado por el usuario
def multiplication_table():
    number: int = int(input("Enter a number to generate your multiplication table: "))
    for i in range(1, 11):
        result: int = number * i
        print(f"{number} x {i} = {result}")

# multiplication_table()

# --------------------------------------------------------------------------------
# 14. Pide el radio de un círculo al usuario y calcula su área.
def area_circunference():
    radius: int = int(input("Enter the radius of the circle: "))
    area: int = math.pi * pow(radius, 2)
    return f"The area of the circumference: {area:.6}"

# print(area_circunference())

# --------------------------------------------------------------------------------
# 15. Toma un número entero y calcula la suma de sus dígitos.
def sum_digit(num: int):
    sum: int = 0
    for i in str(num):
        sum = sum + int(i)
    return sum

print(sum_digit(565))
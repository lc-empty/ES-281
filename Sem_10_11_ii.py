# Ejercicio parte 02 -  Pilas:

#6. Utilizar una pila para invertir el orden de los caracteres de una cadena. 
class Pila:
    def __init__(self):#Inicializamos la clase Pila
        self.items = [] # Creamos una lista vacía para almacenar los elementos de la pila


    def invertir_cadena(self, cadena):# Definimos un funcion para invertir una cadena
        for caracter in cadena:# con for iteramos sobre cada caracter en la cadena
            self.items.append(caracter)# Apilamos cada caracter en la pila
        
        cad_invertida = ""# Inicializamos una cadena vacía para almacenar la cadena invertida
        while self.items:# Mientras la pila no esté vacía, se desapila un caracter y se concatena a la cadena invertida
            cad_invertida += self.items.pop()

        return cad_invertida 

# Ejemplo de uso del ejercicio 6
pila = Pila()
cadena = "mariposa"
cadena_invertida = pila.invertir_cadena(cadena)
print("Cadena original:", cadena)
print("Cadena invertida:", cadena_invertida)


#7. Implementar un programa que convierta un número decimal a su representación en sistema binario utilizando una pila. 
class Pila:
    def __init__ (self):# Inicializaciamos la clase Pila
        self.items =[]# Creamos una lista vacía para almacenar los elementos de la pila
    def convertir_binario(self, numero_decimal):  # definimos una funcion para convertir un número decimal a binario
        while numero_decimal > 0:  # Mientras el número decimal sea mayor que cero
            resto = numero_decimal % 2  # Calculamos el resto de la división entre el número decimal y 2
            self.items.append(resto)  # Apilamos el resto en la pila
            numero_decimal //= 2  # obtenemos la parte entgera del numero dividido entre 2

        binario = ""  # Inicializamos una cadena vacía para almacenar el número binario resultante
        while self.items:  # Mientras la pila no esté vacía
            binario += str(self.items.pop())  # Desapilamos un elemento de la pila y lo agregamos a la cadena binaria

        # Si la cadena binaria está vacía, significa que el número decimal era cero
        # En ese caso, devolvemos "0", de lo contrario, devolvemos la cadena binaria
        return binario if binario else "0"

# Ejemplo 
pila = Pila()  # Creamos una instancia de la clase Pila
numero_decimal = int(input("Ingrese un número decimal: "))  # Solicitamos que se ingrese un número decimal
binario = pila.convertir_binario(numero_decimal)  # Convertimos el número decimal a binario utilizando la funcion convertir_binario
print("El número binario es:", binario)  

#8. Crear un programa que evalúe una expresión matemática en notación posfija utilizando una pila
class Pila:
    def __init__(self):  # Constructor de la clase Pila
        self.items = []  # Creamos una lista vacía para almacenar los elementos de la pila

    def evaluar(self, expresion_matematica):  # Método para evaluar una expresión en notación posfija
        fichas = expresion_matematica.split()  # Dividimos la expresión matematica en fichas 
        for ficha in fichas:  # Iteramos sobre cada ficha en la expresión matematica
            if ficha.isdigit():  # Si la ficha es un dígito apilamos el dígito convertido a entero
                self.items.append(int(ficha))  
            else:# de lo contrario desapilamos el segundo operando y  el primer operando
                operando2 = self.items.pop()  
                operando1 = self.items.pop() 
                resultado = self.calcular(ficha, operando1, operando2)  # Calculamos el resultado
                self.items.append(resultado)  # Apilamos el resultado
        return self.items.pop()  # Devolvemos el resultado final

    def calcular(self, operador, operando1, operando2):  # Método para calcular una operación
        if operador == '+':
            return operando1 + operando2
        elif operador == '-':
            return operando1 - operando2
        elif operador == '*':
            return operando1 * operando2
        elif operador == '/':
            return operando1 / operando2
        else:
            raise ValueError("Operador no válido")


# Ejemplo 
pila = Pila()  # Creamos una instancia de la clase Pila
expresion = "3 1 - 5 * 8 +"  # Definimos una expresión en notación posfija
resultado = pila.evaluar(expresion)  # Evaluamos la expresión
print("Resultado de la expresión posfija:", resultado)


#9. Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una pila. 
class Pila:
    def __init__(self):
        self.items = []  # Inicializamos una lista vacía que servirá como pila

    def verificar(self, expresion):
        for caracter in expresion:  # Iteramos sobre cada caracter en la expresión
            if caracter in "({[":  # Si el caracter es un paréntesis de apertura, corchete o llave
                self.items.append(caracter)  # Lo apilamos en la pila
            elif caracter in ")}]":  # Si el caracter es un paréntesis de cierre, corchete o llave
                if not self.items:  # Si la pila está vacía
                    return False  # Indicamos que la expresión no está correctamente anidada
                cima = self.items.pop()  # Desapilamos el último elemento de la pila
                # Verificamos si el tipo de paréntesis de cierre coincide con el de apertura correspondiente
                if (cima == "(" and caracter != ")") or \
                   (cima == "{" and caracter != "}") or \
                   (cima == "[" and caracter != "]"):
                    return False  # Indicamos que la expresión no está correctamente anidada
        return len(self.items) == 0  # Si la pila está vacía al final, la expresión está correctamente anidada

# Ejemplo de uso
expresion_1 = "(3 + 4) * [5 - {2 / (1 + 3)}]"  # Expresión con paréntesis, corchetes y llaves correctamente anidados
expresion_2 = "{5 + 7) * 2"  # Expresión con error de anidación de paréntesis

pila = Pila()  # Creamos una instancia de la clase Pila

# Verificamos si las expresiones están correctamente anidadas
resultado_1 = pila.verificar(expresion_1)  # Verificamos la primera expresión
resultado_2 = pila.verificar(expresion_2)  # Verificamos la segunda expresión

print("La expresión 1 está correctamente anidada:", resultado_1)
print("La expresión 2 está correctamente anidada:", resultado_2)


#10. Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales. 
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]

def ordenar_pila_ascendente(pila):
    pila_auxiliar = Pila()  # Creamos una pila auxiliar vacía

    # Mientras la pila original no esté vacía
    while not pila.esta_vacia():
        elemento_actual = pila.desapilar()  # Desapilamos un elemento de la pila original

        # Mientras la pila auxiliar no esté vacía y el elemento actual sea menor que el elemento en el tope de la pila auxiliar
        while not pila_auxiliar.esta_vacia() and elemento_actual < pila_auxiliar.ver_tope():
            # Desapilamos un elemento de la pila auxiliar y lo apilamos de nuevo en la pila original
            pila.apilar(pila_auxiliar.desapilar())

        # Apilamos el elemento actual en la pila auxiliar
        pila_auxiliar.apilar(elemento_actual)

    # La pila auxiliar contendrá los elementos ordenados de manera ascendente
    return pila_auxiliar

# Ejemplo
pila = Pila()
pila.apilar(10)
pila.apilar(7)
pila.apilar(12)
pila.apilar(1)

pila_ordenada = ordenar_pila_ascendente(pila)

print("Pila original:", pila.items)
print("Pila ordenada:", pila_ordenada.items)


#11. Eliminar los elementos duplicados de una pila.

def eliminar_elementos_duplicados_pila(pila): # definimos la funcion iminar_elementos_duplicados_pila que recibe como parametro una pila
    pila_elementos_unicos = [] #craemos una pila que almacenara elementos unicos

    while pila:# Mientras pila no esté vacía se ejecutara el bucle
        elemento = pila.pop()
        #verificamos, Si elemento no está en la pila de elementos unicos lo agregamos, de lo contrario no 
        if elemento not in pila_elementos_unicos:
            pila_elementos_unicos.append(elemento)

    # los elementos de la pila de lementos unicos lo llevamos de vuelta a pila 
    while pila_elementos_unicos:
        pila.append(pila_elementos_unicos.pop())

# Ejemplo 
pila = [22, 2, 16, 7, 2, 1, 7]
print("Pila inicial:", pila)
eliminar_elementos_duplicados_pila(pila)
print("Pila sin elementros duplicados:", pila)

#12. Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) utilizando una pila para evaluar expresiones. 
def calculadora(expresion):
    # Divide la expresión en fichas (números y operadores)
    fichas = expresion.split()
    pila = []

    #con if iteramos las fichas
    for ficha in fichas:
        # Si la ficha es un número, lo apila en la pila
        if ficha.isdigit():
            pila.append(float(ficha))
        # Si la ficha es un operador, realiza la operación correspondiente
        else:
            # Se desapilan los dos últimos números
            numero_ultimo= pila.pop()
            numero_antepenultimo= pila.pop()
            # Realiza la operación correspondiente al operador
            if ficha == '+':
                resultado = numero_ultimo + numero_antepenultimo
            elif ficha == '-':
                resultado = numero_ultimo - numero_antepenultimo
            elif ficha== '*':
                resultado = numero_ultimo* numero_antepenultimo
            elif ficha == '/':
                # Manejo de errores, division entre cero
                if numero_antepenultimo == 0:
                    raise ValueError("No se puede dividir entre cero")
                resultado = numero_ultimo / numero_antepenultimo
            else:
                raise ValueError("Operador no válido: " + ficha)
            # Apila el resultado de la operación
            pila.append(resultado)

    # El resultado estará en la cima de la pila
    return pila[0]

# Ejemplo
expresion = "3 4 + 2 *"
resultado = calculadora(expresion)
print("Resultado:", resultado)

#13
def es_palindromo(frase):
    frase= frase.lower().replace(" ", "")## Eliminar los espacios existentes en la frase y convertir los caracteres a minúsculas
    # Creamos una pila
    pila = []
     # con for agregamos cada carácter en la pila de modo que el ultimo ingresa primero
    for caracter in frase:
        pila.append(caracter)
    # Comparamos cada carácter con los correspondientes de la palabra original
    for caracter in frase:
        if caracter != pila.pop():
            return False    #si el caracter es diferente al de la frase la funcion devuelve falso de lo contarrio verdadero
    return True
# Ejemplo 
frase = "Yo hago yoga hoy"
print("¿Es un palíndromo?", es_palindromo(frase))


#14. Implementar un sistema simple de "deshacer" utilizando dos pilas, una para las acciones y otra para los deshaceres. 
 
class SistemaDeshacer:
    # con el Método __init__ que se llama al crear una instancia de la clase se inicializa las pilas de acciones y deshaceres vacías
    def __init__(self):
        self.pila_acciones = []
        self.pila_deshacer = []

    def hacer(self, accion):
        # Realizamos la acción y agregarmos a la pila de acciones
        print("Haciendo:", accion)
        self.pila_acciones.append(accion)

    def deshacer(self):
        if self.pila_acciones:
            # Sacamos la última acción realizada de la pila de acciones y le agregamos a la pila de deshacer
            accion_deshacer = self.pila_acciones.pop()
            print("Deshaciendo:", accion_deshacer) #imprime la accion que estamos deshaciendo
            self.pila_deshacer.append(accion_deshacer)#agramos la accion a la pila de deshacer
        else:
            print("No hay acciones para deshacer")


# Ejemplo
sistema = SistemaDeshacer()
sistema.hacer("Guardar documento")
sistema.hacer("Editar texto")
sistema.deshacer()
sistema.rehacer()


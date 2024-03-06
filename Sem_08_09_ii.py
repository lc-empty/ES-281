#ejercicios parte 1
##1. validar la edad de un usuario 
    def validar_edad(edad):
        ## Con assert verificamos si el parámetro edad es de tipo entero, si no es se genera un error 
        assert isinstance(edad, int), "La edad debe ser un número entero."
        ## verificamos si la edad es un número positivo        
        assert edad > 0, " No existe edad negativa."

    try:
        edad_U = int(input("Ingresa tu edad: "))# se solicita al usuario que ingrese su edad
        validar_edad(edad_U)#validadmos la edad utilizando la funcion
        print("La edad ingresada es correcta")
    ##Si ocurren errores se manejan en los bloques except correspondientes.
    except AssertionError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Debes ingresar un número entero")

##2. Verificar el tipo de dato de una variable. 
    def verificar_tipo_dato(variable, tipo):
        ##verificamos si una variable dada es una instancia del tipo especificado.
        ##Si la variable no es del tipo esperado, se genera un error AssertionError con un mensaje que indica el tipo esperado
        assert isinstance(variable, tipo), f"La variable no es del tipo {tipo}"
    #ejemplo de uso
    numero = 5
    verificar_tipo_dato(numero, int)

    numero ="hola"
    verificar_tipo_dato(numero, int)

##3. Validar el rango de una calificación. 
    def validar_calificacion(calificacion):
        #verificamos si una calificación dada está dentro del rango de 0 a 20
        #si la calificacion se encuentra fuera del rango, ocurre un error y se imprime un mensaje
        assert 0 <= calificacion <= 20, "La calificación debe estar en el rango de 0 a 20"
    
    try:
        #solicitamos al usuario que ingrese una calificación
        calificacion = float(input("Ingresa tu calificación: "))
        #validamos utilizando la función validar_calificacion
        validar_calificacion(calificacion)
        print("La calificación es válida.")
    #Si la calificación ingresada no está en el rango válido
    #o si el usuario no ingresa un número, se manejan las excepciones AssertionError y ValueError
    except AssertionError as error:
        print(error)
    except ValueError:
        print("Error: Debes ingresar un número")

##4. Asegurar que una lista no esté vacía. 
    def asegurar_lista_no_vacia(lista): # se define la funcion asegurar_lista_no_vacia que recibe como paarmetro lista
        assert isinstance(lista, list), "El parametro debe ser una lista"# verifica si lista dada es una lista y si no está vacía
        assert len(lista) > 0, "La lista no puede estar vacía"

    #ejemplo 1: lista no vacia
    try:
        numeros= [8,3,9,10]#se crea una lista de números y se pasa a la función asegurar_lista_no_vacia.
                            #Si la lista cumple con los criterios de la función, se imprime "La lista no está vacía".
        asegurar_no_vacia(numeros)
        print("La lista no está vacía")
    except AssertionError as error:
        print(error)
    #ejemplo 2: lista vacia
    try:
        lista = []
        asegurar_lista_no_vacia(lista)
        print("La lista no está vacía")
    except AssertionError as error:
        print(error)

##5. Validar la igualdad de dos objetos. 
    def validar_igualdad_objetos(objeto1, objeto2):
        assert objeto1 == objeto2, "Los objetos no son iguales"#valiadmos si dos objetos son iguales
    #ejemplo 1
    try:
        #creamos una lista y un diccionario y se pasan a la función validar_igualdad_objetos
        conjunto1 = {"a": 1, "b": 2}
        conjunto2 = {"a": 1, "b": 3}
        validar_igualdad_objetos(conjunto1, conjunto2)
        print("Los objetos son iguales")
    except AssertionError as error:
        print(error)

    #ejemplo2
    try:
        lista1 = [1, 2, 3]
        lista2 = {"a": 1, "b": 3}
        validar_igualdad_objetos(lista1, lista2)
        print("Los objetos son iguales")
    except AssertionError as e:
        print(f"Error: {e}")


##6. Asegurar que un ciclo while se ejecuta al menos una vez. 
    def asegurar_ejecucion_ciclo_while():
        contador = 5 #inicializamos una variable contador que permitira controlar el numero de iteraciones del ciclo
        ejecucion= False #inicializamos una variable ejecucion con false
        while contador <= 5:# si contador es menor o igual 5 la variable ejecucion toma el valor de true de lo contario sigue con su valor inicial
            ejecucion = True
            contador += 1
        
        assert ejecucion, "El ciclo while no se ejecutó al menos una vez"#si ejecucion toma el valor de True es porque el ciclo while se ejecuto al menos una vez 
    try:                                                                    # si Toma falso el ciclo no se ejcuto 
        asegurar_ejecucion_ciclo_while()
        print("El ciclo while se ejecutó al menos una vez")
    except AssertionError as error:
        print(error)

##7. Asegurar que una función retorna un valor específico. 
    def retornar_valor(valor):
        resultado = 10
        return resultado

    try:
        valor_esperado = 10
        resultado_funcion = retornar_valor(valor_esperado)
        #con la aserción verificamos si el valor devuelto por la función es igual al valor esperado 
        assert resultado_funcion == valor_esperado, f"El valor retornado ({resultado_funcion}) no coincide con el valor esperado ({valor_esperado})."
        print("La función retornó el valor esperado.")
    except AssertionError as error:
        print(error)
##8. Validar el estado de una variable después de una operación. 
    def division(a, b):# Definimos la función division que toma dos parámetros, a y b, y realiza la división de a entre b.
                        #Antes de realizar la división se verifica si b es diferente de cero.
        assert b != 0, "{b} debe ser diferente de cero"#si b es cero se generará un error AssertionError con el mensaje "{b} debe ser diferente de cero"
        return a/b

    # Probamos la función con algunos valores
    try:
        resultado = division(5, 3)
        print("Resultado de la operación:", resultado)
        assert isinstance(resultado,int), "El resultado de la operación no es entero"
    except AssertionError as error:
        print(error)
##9. Asegurar que un módulo se ha importado correctamente. 
try:
    import modulo_ejemplo #importamos un módulo llamado modulo_ejemplo
except ImportError:
    print("Error: No se pudo importar el módulo")
else:
    # Verificamos si un atributo o función específica del módulo está presente
    assert hasattr(modulo_ejemplo, 'funcion_ejemplo'), "La función 'funcion_ejemplo' no está definida en el módulo"
    print("El módulo se ha importado correctamente")
    #Si la función no está definida en el módulo, se generará un error de aserción.
    #De lo contrario, se imprimirá un mensaje indicando que el módulo se ha importado correctamente

# Ejercicios parte 2

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.inicio = None

# _____
    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.inicio
        self.inicio = nuevo_nodo


    def insertar_final(self, dato):
        return


    def eliminar_nodo(self, dato):
        return
# sdfsdfsd

    def mostrar(self):
        actual = self.inicio
        while actual:
            if actual.siguiente:
                print(actual.dato, end=" -> ")
            else:
                print(actual.dato)
            actual = actual.siguiente


    # 10. Desarrollar el código de buscar nodo en la lista enlazada simple.
    def buscar(self, dato):
        actual = self.inicio
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False


    # Suma de Nodos
    # 11. Implementa una función que sume todos los nodos de una lista enlazada simple.
    def suma_todos_nodos(self):
        suma = 0
        actual = self.inicio
        while actual:
            suma += actual.dato
            actual = actual.siguiente
        return suma


    # Longitud de la Lista
    # 12. Crea una función que devuelva la longitud de una lista enlazada simple.
    def longitud(self):
        contador = 0
        actual = self.inicio
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador


    # Concatenar Listas
    # 13. Implementa una función que concatene dos listas enlazadas simples.
    def concatenar(self, otra_lista):
        actual = self.inicio
        if actual is None:
            self.inicio = otra_lista.inicio
            return
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = otra_lista.inicio


    # Eliminar Duplicados
    # 14. Crea una función que elimine los nodos duplicados de una lista enlazada simple.
    def eliminar_duplicados(self):
        if self.inicio is None:
            return
        valores_vistos = set()
        actual = self.inicio
        valores_vistos.add(actual.dato)
        while actual.siguiente:
            if actual.siguiente.dato in valores_vistos:
                actual.siguiente = actual.siguiente.siguiente
            else:
                valores_vistos.add(actual.siguiente.dato)
                actual = actual.siguiente


    # Invertir Lista
    # 15. Implementa una función que invierta el orden de una lista enlazada simple
    def invertir_orden(self):
        anterior = None
        actual = self.inicio
        siguiente = None
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.inicio = anterior


# actual = lista.inicio
# while actual:
#     print(actual.dato, end=" -> ")
#     actual = actual.siguiente


# Creamos una lista enlazada
lista = ListaEnlazadaSimple()

# Insertamos algunos nodos al inicio de la lista
lista.insertar_inicio(3)
lista.insertar_inicio(2)
lista.insertar_inicio(1)
lista.insertar_inicio(1)

# Mostramos la lista
print("Lista original:")
lista.mostrar()

# Buscamos un valor en la lista
valor_buscado = 2
if lista.buscar(valor_buscado):
    print(f"El valor {valor_buscado} está en la lista.")
else:
    print(f"El valor {valor_buscado} no está en la lista.")

# Sumamos todos los nodos de la lista
suma_total = lista.suma_todos_nodos()
print("La suma de todos los nodos es:", suma_total)

# Obtenemos la longitud de la lista
longitud_lista = lista.longitud()
print("La longitud de la lista es:", longitud_lista)

# Creamos otra lista
otra_lista = ListaEnlazadaSimple()
otra_lista.insertar_inicio(4)
otra_lista.insertar_inicio(5)

# Concatenamos las dos listas
lista.concatenar(otra_lista)

# Mostramos la lista concatenada
print("Lista concatenada:")
lista.mostrar()

# Eliminamos los nodos duplicados
lista.eliminar_duplicados()

# Mostramos la lista sin duplicados
print("Lista sin duplicados:")
lista.mostrar()

# Invertimos el orden de la lista
lista.invertir_orden()

# Mostramos la lista invertida
print("Lista invertida:")
lista.mostrar()

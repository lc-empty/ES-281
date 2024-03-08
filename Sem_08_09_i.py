# Ejercicios parte 1
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



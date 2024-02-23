#6
class Pila:
    def _init_ (self):
        self.items =[]
    def invertirCadena(self, cadena):
        for caracter in cadena:
            self.items.append(caracter)
            invertirCadena = ""
            while self.items:
                invertirCadena += self.items.pop()
                return invertirCadena
#7
class Pila:
    def _init_ (self):
        self.items =[]
    def convertir_binario(self, numero_decimal):
        while numero_decimal > 0:
            resto = numero_decimal % 2
            self.items.append(resto)
            numero_decimal//= 2
        binario = ""
        while self.items:
            binario += str(self.items.pop())

        return binario if binario else "0"


#8
class Pila:
    def _init_ (self):
        self.items =[]
    def evaluar(self, expresión):
        ficha = expresión.split()
        for ficha in ficha:
            if ficha.isdigit():
                self.items.append(int(token))
            else:
                operando2 = self.items.pop()
                operando1 = self.items.pop()
                resultado = self.calculate(ficha, operando1, operando2)
                self.items.append(resultado)
        return self.items.pop()

    def calcular(self, operador, operando1, operando2):
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

#8
class Pila:
    def __init__(self):
        self.items = []

    def verificar(self, expresion):
        for caracter in expresion:
            if caracter in "({[":
                self.items.append(caracter)
            elif caracter in ")}]":
                if not self.items:
                    return False  
                cima = self.items.pop()
                if (cima == "(" and caracter != ")") or \
                   (cima == "{" and caracter != "}") or \
                   (cima == "[" and caracter != "]"):
                    return False  
        return len(self.items) == 0  
#9
class pila:
    def __init__(self):
        self.items = []

    def esta_vacio(self):
        return len(self.items) == 0

    def agregar(self, item):
        self.items.append(item)

    def quitar(self):
        if not self.esta_vacio():
            return self.items.pop()

    def ultimo_elemento(self):
        if not self.esta_vacio():
            return self.items[-1]

    def tamaño(self):
        return len(self.items)


    def ordenar_pila(stack):
        pila_ordenada = Stack()

        while not stack.esta_vacio():
            temp = stack.pop()

            while not pila_ordenada.esta_vacio() and pila_ordenada.ultimo_elemento() > temp:
                stack.agregar(pila_ordenada.pop())

            sorted.agregar(temp)

        while not pila_ordenada.esta_vacio():
            stack.agregar(pila_ordenada.quitar())

#10
class pila:
    def __init__(self):
        self.items = []

    def esta_vacio(self):
        return len(self.items) == 0

    def agregar(self, item):
        self.items.append(item)

    def quitar(self):
        if not self.esta_vacio():
            return self.items.pop()

    def ultimo_elemento(self):
        if not self.esta_vacio():
            return self.items[-1]

    def tamaño(self):
        return len(self.items)

    def quitar_duplicados(pila):
        seen = set()
        temp_stack = pila()

        while not pila.esta_vacio():
            item =pila.quitar()
            if item not in seen:
                temp_stack.agregar(item)
                seen.add(item)

        while not temp_stack.esta_vacio():
            pila.agregar(temp_stack.quitar())

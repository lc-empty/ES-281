
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDobleEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.inicio:
            self.inicio = self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.inicio
            self.inicio.anterior = nuevo_nodo
            self.inicio = nuevo_nodo

    def agregar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.fin:
            self.inicio = self.fin = nuevo_nodo
        else:
            self.fin.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.fin
            self.fin = nuevo_nodo

    def mostrar_estado(self):
        actual = self.inicio
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")

# Crear las cuentas bancarias
cuenta1 = ListaDobleEnlazada()
cuenta2 = ListaDobleEnlazada()

# Operación transaccional: Transferencia de dinero de cuenta1 a cuenta2
cuenta1.agregar_inicio(1000)
cuenta1.agregar_inicio(500)
cuenta2.agregar_inicio(200)

print("Estado inicial de la cuenta 1:")
cuenta1.mostrar_estado()
print("Estado inicial de la cuenta 2:")
cuenta2.mostrar_estado()

# Operación transaccional: Retiro de dinero de cuenta1
cuenta1.agregar_inicio(-300)

# Operación transaccional: Depósito en cuenta2
cuenta2.agregar_inicio(100)

# Mostrar el estado de las cuentas después de las operaciones
print("Estado de la cuenta 1 después de la transacción:")
cuenta1.mostrar_estado()
print("Estado de la cuenta 2 después de la transacción:")
cuenta2.mostrar_estado()

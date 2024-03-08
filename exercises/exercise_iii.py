class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDobleEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def agregar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.fin is None:
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.fin
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo

    def obtener_primero(self):
        if self.inicio:
            return self.inicio.dato
        return None

    def obtener_ultimo(self):
        if self.fin:
            return self.fin.dato
        return None

    def mostrar_datos(self):
        actual = self.inicio
        i = 1
        while actual:
            print(f"{i} -> {actual.dato}")
            actual = actual.siguiente
            i +=1

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.historial = ListaDobleEnlazada()
        self.historial.agregar_final(saldo_inicial)

    def mostrar_saldo_inicial(self):
        return self.historial.obtener_primero()

    def mostrar_saldo_actual(self):
        return self.historial.obtener_ultimo()

    def mostrar_historial(self):
        print("Historial de transacciones:")
        self.historial.mostrar_datos()


class SistemaGestionBancario:
    def transaccion(self, cuenta_origen, cuenta_destino, monto):
        saldo_origen = cuenta_origen.historial.obtener_ultimo()
        saldo_destino = cuenta_destino.historial.obtener_ultimo()
        
        if saldo_origen >= monto:
            cuenta_origen.historial.agregar_final(saldo_origen - monto)
            cuenta_destino.historial.agregar_final(saldo_destino + monto)
            return True
        else:
            return False




# Creamos las cuentas bancarias
cuenta_1 = CuentaBancaria(1000)
cuenta_2 = CuentaBancaria(500)

# Creamos una instancia del sistema de gestión bancario
sistema_bancario = SistemaGestionBancario()

# Realizamos una transacción
if sistema_bancario.transaccion(cuenta_1, cuenta_2, 200):
    print("Transferencia exitosa.")
else:
    print("Fondos insuficientes.")

# Mostramos el saldo inicial y el saldo actual de ambas cuentas
print("Saldo inicial cuenta_1:", cuenta_1.mostrar_saldo_inicial())
print("Saldo actual cuenta_1:", cuenta_1.mostrar_saldo_actual())

print("Saldo inicial cuenta_2:", cuenta_2.mostrar_saldo_inicial())
print("Saldo actual cuenta_2:", cuenta_2.mostrar_saldo_actual())

# Historial de Transferencias
cuenta_2.mostrar_historial()

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None

    def enColar(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo

    def desColar(self):
        if not self.esta_vacia():
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is None:
                self.cola = None
            return dato
        else:
            return None

class Llamada:
    def __init__(self, duracion, prioridad):
        self.duracion = duracion
        self.prioridad = prioridad

class SistemaGestionLlamadas:
    def __init__(self):
        self.llamadas_en_espera = Cola()

    def agregar_llamada(self, duracion, prioridad):
        llamada = Llamada(duracion, prioridad)
        self.llamadas_en_espera.enColar(llamada)

    def obtener_prioridad(self, llamada):
        return llamada.prioridad 

    def atender_llamadas(self):
        if self.llamadas_en_espera.esta_vacia():
            print("No hay llamadas en espera.")
            return

        llamadas_lista = []
        while not self.llamadas_en_espera.esta_vacia():
            llamadas_lista.append(self.llamadas_en_espera.desColar())

        llamadas_ordenadas = []
        for llamada in llamadas_lista:
            if not llamadas_ordenadas:
                llamadas_ordenadas.append(llamada)
            else:
                for i in range(len(llamadas_ordenadas)):
                    if llamada.prioridad < llamadas_ordenadas[i].prioridad:
                        llamadas_ordenadas.insert(i, llamada)
                        break
                else:
                    llamadas_ordenadas.append(llamada)
        
        print("Atendiendo llamadas en orden de prioridad y tiempo de duración:")
        for llamada in llamadas_ordenadas:
            print(f"Llamada - Duración: {llamada.duracion} minutos, Prioridad: {llamada.prioridad}")


# Ejemplo de uso
sistema_llamadas = SistemaGestionLlamadas()
sistema_llamadas.agregar_llamada(5, 1)
sistema_llamadas.agregar_llamada(10, 2)
sistema_llamadas.agregar_llamada(7, 1)
sistema_llamadas.agregar_llamada(3, 3)

sistema_llamadas.atender_llamadas()


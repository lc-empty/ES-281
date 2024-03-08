class Llamada:
    def __init__(self, duracion, prioridad):
        self.duracion = duracion
        self.prioridad = prioridad

class SistemaGestionLlamadas:
    def __init__(self):
        self.llamadas_espera = []

    def agregar_llamada(self, llamada):
        self.llamadas_espera.append(llamada)

    def atender_llamada(self):
        if self.llamadas_espera:
            # Ordenar las llamadas por prioridad y duración
            self.llamadas_espera.sort(key=lambda x: (x.prioridad, -x.duracion))
            llamada_atendida = self.llamadas_espera.pop(0)
            return llamada_atendida
        else:
            return None

    def mostrar_llamadas_espera(self):
        if self.llamadas_espera:
            print("Llamadas en espera:")
            for llamada in self.llamadas_espera:
                print(f"Duración: {llamada.duracion}, Prioridad: {llamada.prioridad}")
        else:
            print("No hay llamadas en espera")

# Crear el sistema de gestión de llamadas
sistema_llamadas = SistemaGestionLlamadas()

# Agregar algunas llamadas de ejemplo
sistema_llamadas.agregar_llamada(Llamada(10, 2))
sistema_llamadas.agregar_llamada(Llamada(5, 1))
sistema_llamadas.agregar_llamada(Llamada(15, 3))

# Atender las llamadas en orden de prioridad y duración
llamada_atendida = sistema_llamadas.atender_llamada()
if llamada_atendida:
    print("Llamada atendida - Duración:", llamada_atendida.duracion)
else:
    print("No hay llamadas en espera")

# Mostrar el estado actual de las llamadas en espera
sistema_llamadas.mostrar_llamadas_espera()


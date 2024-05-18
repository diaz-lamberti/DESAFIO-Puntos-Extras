import random

# Definir clase Dado, con atributos como valor y cara actual
class Dado():
    def __init__(self):
        self.valor = random.randint(1, 6)

dado1 = Dado()
dado2 = Dado()
dado3 = Dado()
dado4 = Dado()
dado5 = Dado()
dado6 = Dado()

# Definir clase Jugador con atributos como nombre, puntaje total y puntaje por ronda
class Jugador():
    def __init__(self):
        self.nombre = input("Ingresa tu nombre: ")

    def __str__(self):
        return str(self.nombre)

jugador1 = Jugador()
jugador2 = Jugador()
jugadores = [jugador1, jugador2]

# Definir quien tiene el primer turno
def definirTurno(jugadores):
    primer_turno = random.choice(jugadores)
    print(f"El primer turno sera de {primer_turno}")

definirTurno(jugadores)

# Definir clase marcador, llevando la cuenta del puntaje de cada jugador y las combinaciones válidas.

# Simular el lanzamiento de cinco dados utilizando un generador de numeros aleatorios

# Proporcionar una interfaz para mostrar las tiradas de dados, las opciones disponibles y el puntaje actual

# Implementar las reglas de puntuación para las diferentes combinaciones posibles

# Gestionar las rondas y turnos del juego, permitiendo a cada jugador realizar sus tiradas y tomar decisiones estrategicas

# Determinar el ganador al ﬁnal de las tres rondas, mostrando el puntaje ﬁnal de cada jugador.

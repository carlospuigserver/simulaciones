import random
import time
import threading

class Ruleta:
    def __init__(self):
        self.numero = None
        self.jugadores= []
        self.banca=50000

    def jugar(self):
        self.numero = random.randint(0,36)
        if self.numero == 0:
            for jugador in self.jugadores:
                jugador.saldo=0
            self.banca += sum(jugador.apuesta for jugador in self.jugadores)
            return
        for jugador in self.jugadores:
            jugador.jugar()

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

class Jugador(threading.Thread):
    def __init__(self,ruleta, nombre):
        super().__init__()
        self.ruleta = ruleta
        self.nombre=nombre
        self.saldo=1000
        self.apuesta=10
    def jugar(self):
        pass


class NumeroJugador(Jugador):
    def __init__(self,ruleta,nombre):
        super().__init__(ruleta,nombre)
        self.numero=random.randint(1,36)

    def jugar(self):
        if self.ruleta.numero == self.numero:
            self.saldo += self.apuesta *36
            self.ruleta.banca -= self.apuesta*36
        else:
            self.saldo -= self.apuesta
            self.ruleta.banca += self.apuesta

class ParidadJugador(Jugador):
    def __init__(self,ruleta,nombre):
        super().__init__(ruleta,nombre)
        self.paridad=random.choice([True],[False])

    def jugar(self):
        if self.ruleta==0:
            self.saldo -= self.apuesta
            self.ruleta.banca += self.apuesta
        elif self.ruleta.numero % 2 == 0 and self.paridad:
            self.saldo += self.apuesta *2
            self.ruleta.banca -= self.apuesta *2
        elif self.ruleta.numero %2 ==1 and not self.paridad:
            self.saldo += self.apuesta *2
            self.ruleta.banca -= self.apuesta*2
        else:
            self.saldo -= self.apuesta
            self.ruleta.banca += self.apuesta

class RandomJugador(Jugador):
    def __init__(self,ruleta,nombre):
        super().__init__(ruleta,nombre)
        self.numero=random.randint(1,36)
        self.apuesta_actual=self.apuesta

    def jugar(self):
        if self.ruleta.numero == self.numero:
            self.saldo += self.apuesta_actual *36
            self.ruleta.banca -= self.apuesta_actual*36
            self.apuesta_actual=self.apuesta
        else:
            self.saldo -= self.apuesta_actual
            self.ruleta.banca += self.apuesta_actual
            self.apuesta_actual *=2

def simular():
    ruleta = Ruleta()
    jugadores = [
        NumeroJugador(ruleta, "Jugador 1"),
        NumeroJugador(ruleta, "Jugador 2"),
        NumeroJugador(ruleta, "Jugador 3"),
        NumeroJugador(ruleta, "Jugador 4"),
        ParidadJugador(ruleta, "Jugador 5"),
        ParidadJugador(ruleta, "Jugador 6"),
        RandomJugador(ruleta, "Jugador 7"),
        RandomJugador(ruleta, "Jugador 8"),
        RandomJugador(ruleta, "Jugador 9")
    ]

    for ronda in range(10):
        print(f"Ronda {ronda + 1} - Banca: {ruleta.banca}")
        for jugador in jugadores:
            jugador.apuesta = 10
            if jugador.saldo == 0:
                continue
            jugador.start()

        time.sleep(2)

        ruleta.jugar()

        for jugador in jugadores:
            jugador.join()
            print(f"{jugador.nombre} - Saldo: {jugador.saldo}")

        print(f"Banca después de la ronda {ronda + 1}: {ruleta.banca}\n")

if __name__ == "__main__":
    simular()

    
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.enlace = None

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def get_enlace(self):
        return self.enlace

    def set_enlace(self, enlace):
        self.enlace = enlace

    def __str__(self):
        return f'Nodo{{valor={self.valor}, enlace={self.enlace}}}'


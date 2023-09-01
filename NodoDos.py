class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.enlace_1 = None
        self.enlace_2 = None

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def get_enlace_1(self):
        return self.enlace_1

    def set_enlace_1(self, enlace_1):
        self.enlace_1 = enlace_1

    def get_enlace_2(self):
        return self.enlace_2

    def set_enlace_2(self, enlace_2):
        self.enlace_2 = enlace_2

    def __str__(self):
        return f'NodoDoble{{valor={str(self.valor)}}}'

from Nodo import Nodo


class ListaLigada:
    def __init__(self):
        self.cabeza = None

    def insercion(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            temporal = self.cabeza
            while temporal.enlace is not None:
                temporal = temporal.enlace
            temporal.enlace = nuevo_nodo

    def acceso(self):
        temporal = self.cabeza
        while temporal is not None:
            print(temporal.valor, end=" ")
            temporal = temporal.enlace
        print()

    def busqueda(self, valor):
        temporal = self.cabeza
        if temporal.get_valor() == valor:
            return temporal

        while True:
            if temporal.enlace is not None:
                if temporal.get_valor() != valor:
                    temporal = temporal.enlace
                else:
                    return temporal
            else:
                if temporal.enlace is None:
                    if temporal.get_valor() == valor:
                        return temporal
                break

        return None

    def eliminar(self, valor):
        if self.cabeza is None:
            return

        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.enlace

        temporal = self.cabeza
        while temporal.enlace is not None and temporal.enlace.valor != valor:
            temporal = temporal.enlace

        if temporal.enlace is not None:
            temporal.enlace = temporal.enlace.enlace

    def invertir(self):
        temp = None
        actual = self.inicio
        while actual is not None:
            temp = actual.enlace_1
            actual.enlace_1 = actual.enlace_2
            actual.enlace_2 = temp
            actual = actual.enlace_1
        temp = self.inicio
        self.inicio = self.fin
        self.fin = temp


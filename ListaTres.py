from Nodo import Nodo

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def insercion(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            nuevo_nodo.enlace = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.enlace = self.cabeza.enlace
            self.cabeza.enlace = nuevo_nodo

    def eliminar(self, valor):
        if not self.cabezaEstaVacia():
            if self.cabeza.valor == valor:
                if self.cabeza.enlace == self.cabeza:
                    self.cabeza = None
                else:
                    ultimo = self.cabeza
                    while ultimo.enlace != self.cabeza:
                        ultimo = ultimo.enlace
                    ultimo.enlace = self.cabeza.enlace
                    self.cabeza = self.cabeza.enlace
            else:
                actual = self.cabeza
                anterior = None
                while True:
                    anterior = actual
                    actual = actual.enlace
                    if actual == self.cabeza or actual.valor == valor:
                        break
                if actual != self.cabeza:
                    anterior.enlace = actual.enlace

    def acceso(self):
        if not self.cabezaEstaVacia():
            actual = self.cabeza
            while True:
                print(actual.valor, end=" ")
                actual = actual.enlace
                if actual == self.cabeza:
                    break
            print()

    def buscar(self, valor):
        if not self.cabezaEstaVacia():
            actual = self.cabeza
            while True:
                if actual.valor == valor:
                    return actual
                actual = actual.enlace
                if actual == self.cabeza:
                    break
        return None

    def cabezaEstaVacia(self):
        return self.cabeza is None

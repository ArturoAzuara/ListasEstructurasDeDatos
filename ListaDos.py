from NodoDos import NodoDoble

class ListaLigadaDoble:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def primeraInsercion(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if self.inicio is None:
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.enlace_2 = self.inicio
            self.inicio.enlace_1 = nuevo_nodo
            self.inicio = nuevo_nodo

    def ultimaInsercion(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if self.fin is None:
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.enlace_1 = self.fin
            self.fin.enlace_2 = nuevo_nodo
            self.fin = nuevo_nodo

    def eliminar(self, valor):
        actual = self.inicio
        while actual is not None:
            if actual.valor == valor:
                if actual == self.inicio:
                    self.inicio = actual.enlace_2
                    if self.inicio is not None:
                        self.inicio.enlace_1 = None
                elif actual == self.fin:
                    self.fin = actual.enlace_1
                    if self.fin is not None:
                        self.fin.enlace_2 = None
                else:
                    actual.enlace_1.enlace_2 = actual.enlace_2
                    actual.enlace_2.enlace_1 = actual.enlace_1
                return
            actual = actual.enlace_2

    def acceso(self):
        actual = self.inicio
        while actual is not None:
            print(actual.valor, end=" ")
            actual = actual.enlace_2
        print()

    def buscar(self, valor):
        actual = self.inicio
        while actual is not None:
            if actual.valor == valor:
                return actual
            actual = actual.enlace_2
        return None

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

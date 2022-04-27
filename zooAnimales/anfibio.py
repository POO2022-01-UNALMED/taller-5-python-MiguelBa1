from animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    _listado = []

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", colorPiel = "", venenoso = False):
        Animal.__init__(self, nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    def cantidadAnfibios(self):
        return len(self._listado)

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas += 1
        cls._listado.append(rana)
        return rana

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1
        cls._listado.append(salamandra)
        return salamandra

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    def movimiento(self):
        return "saltar"

    @classmethod
    def getListado(cls):
        return cls._listado

    def setListado(cls, listado):
        cls._listado = listado

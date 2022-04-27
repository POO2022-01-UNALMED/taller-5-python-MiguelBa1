from .animal import Animal

class Ave(Animal):

    halcones = 0
    aguilas = 0
    _listado = []

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", colorPlumas = ""):
        Animal.__init__(self, nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        Ave.halcones += 1
        # Ave._listado.append(halcon)
        return halcon

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        Ave.aguilas += 1
        # Ave._listado.append(aguila)
        return aguila

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas

    def movimiento(self):
        return "volar"

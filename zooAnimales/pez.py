from animal import Animal
class Pez(Animal):
    salmones = 0
    bacalaos = 0
    _listado = []

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", colorEscamas = "", cantidadAletas = 0):
        Animal.__init__(self, nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        cls.salmones += 1
        cls._listado.append(salmon)
        return salmon

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        cls.bacalaos += 1
        cls._listado.append(bacalao)
        return bacalao

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas

    def movimiento(self):
        return "nadar"

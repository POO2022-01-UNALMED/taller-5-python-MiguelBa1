
class Animal:
    _totalAnimales = 0

    def __init__ (self, nombre = "", edad = 0, habitat = "", genero = ""):
        Animal._totalAnimales += 1
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero

    def movimiento(self):
        return "desplazarse"

    def totalPorTipo(self):
        from .pez import Pez
        from .mamifero import Mamifero
        from .ave import Ave
        from .reptil import Reptil
        from .anfibio import Anfibio
        return str("Mamiferos: " + str(len(Mamifero.getListado())) +"\n" + 
				"Aves: "+str(len(Ave.getListado()))+"\n" + 
				"Reptiles: "+str(len(Reptil.getListado()))+"\n" + 
				"Peces: "+str(len(Pez.getListado()))+"\n" + 
				"Anfibios: "+str(len(Anfibio.getListado())))
    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales

    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales = totalAnimales

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona

    def __str__(self):
        return ("Mi nombre es " +
                self._nombre +
                ", tengo una edad de " +
                self._edad +
                ", habito en " +
                self._habitat +
                " y mi genero es " +
                self._genero +
                (", la zona en la que me ubico es " + self._zona + ", en el " + self._zona.getZoo() if self._zona else ""))

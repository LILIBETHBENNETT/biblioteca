from abc import ABC, abstractmethod

class Material(ABC):
    def __init__(self, codigo: str = None, autor: str = None, titulo: str = None , anio: int = None, editorial: str = None, disponible: bool = None, cantidad_disponible: int = None):
        self.codigo = codigo
        self.autor = autor
        self.titulo = titulo
        self.anio = anio
        self.editorial = editorial
        self.disponible = disponible
        self.cantidad_disponible = cantidad_disponible

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, nuevo_codigo):
        self._codigo = nuevo_codigo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, nuevo_autor):
        self._autor = nuevo_autor

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, nuevo_anio):
        self._anio = nuevo_anio

    @property
    def editorial(self):
        return self._editorial

    @editorial.setter
    def editorial(self, nuevo_editorial):
        self._editorial = nuevo_editorial

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, nuevo_estado):
        self._disponible = nuevo_estado

    @property
    def cantidad_disponible(self):
        return self._cantidad_disponible

    @cantidad_disponible.setter
    def saldo(self, nueva_cantidad):
        self._cantidad_disponible = nueva_cantidad


    @abstractmethod
    def actualizar_disponibilidad(self, disponible):
        pass



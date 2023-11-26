from Material import Material


class Revista(Material):
    _contador_revista = 0

    def __init__(self, codigo:str = None, autor:str = None, titulo:str = None, anio:int = None, editorial:str = None, disponible:bool = None, cantidad_disponible:int = None, id:int = None, tipo:str = None):
        super().__init__(codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible)
        self._id = id
        self._tipo = tipo
        Revista._contador_revista += 1

    @property
    def contador_revista(self):
        return Revista._contador_revista

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nuevo_id):
        self._id = nuevo_id

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo

    def actualizar_disponibilidad(self, disponible):
        self.disponible = disponible

    def __str__(self):
        return f'Revista(id={self.id}, codigo={self.codigo}, titulo={self.titulo}, autor={self.autor}, disponible={self.disponible}, cantidad_disponible={self.cantidad_disponible}, tipo ={self.tipo}, contador_revista={self.contador_revista})'

#KARELIN CORREA
#LILIBETH BENNETT
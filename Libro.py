from Material import Material

class Libro(Material):
    _contador_libro = 0

    def __init__(self, codigo: str = None, autor: str = None, titulo: str = None, anio: int = None, editorial: str = None, disponible: bool = None, cantidad_disponible: int = None, id: int = None, tipo_pasta: str = None):
        super().__init__(codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible)
        self.id = id
        self.tipo_pasta = tipo_pasta
        Libro._contador_libro += 1

    @property
    def contador_libro(self):
        return Libro._contador_libro

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nuevo_id):
        self._id = nuevo_id

    @property
    def tipo_pasta(self):
        return self._tipo_pasta

    @tipo_pasta.setter
    def tipo_pasta(self, nueva_tipo_pasta):
        self._tipo_pasta = nueva_tipo_pasta

    def actualizar_disponibilidad(self, disponible):
        self.disponible = disponible

    def __str__(self):
        return f"Libro(id={self.id}, codigo={self.codigo}, titulo={self.titulo}, autor={self.autor}, disponible={self.disponible}, cantidad_disponible={self.cantidad_disponible}, tipo_pasta={self.tipo_pasta}, contador_libro={self.contador_libro})"


#KARELIN CORREA
#LILIBETH BENNETT



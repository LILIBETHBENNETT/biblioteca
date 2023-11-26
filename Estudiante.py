from Persona import Persona
class Estudiante(Persona):
    _contador_estudiante = 0
    def _init_(self,cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera, id=int, nivel=int,):
        super()._init_(cedula , nombre , apellido, email, telefono, direccion , numero_libros , activo,carrera)
        self.id = id
        self.nivel = nivel
        Estudiante._contador_estudiante += 1

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    @property
    def contador_estudiante (self):
        return Estudiante._contador_estudiante

    def pedir_libro(self):
        self._contador_estudiante += 1
        return True


    def devolver_libro(self):
        if self._contador_estudiante > 0:
            self._contador_estudiante -= 1
            return True
        else:
            return False

    def _str_(self):
        return f"Estudiantes(id={self.id}, nivel={self.nivel}, numero_libros={self.numero_libros}, contador_estudiantes={self._contador_estudiante})"

#KARELIN CORREA
#LILIBETH BENNETT
class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None  
        self.nota = None  

    def display(self):
        print("Nombre:", self.nombre)
        print("Número de Registro:", self.numero_registro)
        if self.edad is not None: 
            print("Edad:", self.edad)
        if self.nota is not None: 
            print("Nota:", self.nota)

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, nota):
        self.nota = nota

alumno1 = Alumno("Bruno Palomino", "74698776")

alumno1.setAge(22)
alumno1.setNota(17)

alumno1.display()

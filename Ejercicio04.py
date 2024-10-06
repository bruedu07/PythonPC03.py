class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)

rectangulo = RECTANGULO(10, 5)

cuadrado = CUADRADO(7) 

area_rectangulo = rectangulo.calcular_area()
area_cuadrado = cuadrado.calcular_area()

print(f"El área del rectángulo es: {area_rectangulo}")
print(f"El área del cuadrado es: {area_cuadrado}")

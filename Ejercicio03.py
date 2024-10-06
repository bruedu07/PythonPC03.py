class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        pi = 3.1416 
        return pi * (self.radio ** 2)

circulo1 = CIRCULO(5)
circulo2 = CIRCULO(10) 

area_circulo1 = circulo1.calcular_area()
area_circulo2 = circulo2.calcular_area()

print(f"El área del círculo 1 con radio {circulo1.radio} es: {area_circulo1:.2f}")
print(f"El área del círculo 2 con radio {circulo2.radio} es: {area_circulo2:.2f}")

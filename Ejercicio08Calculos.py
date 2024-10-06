# Este es el script principal calculos.py
import Ejercicio08Operaciones

# Aquí llamamos las funciones desde operaciones.py

# Pedimos al usuario que ingrese dos números
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
except ValueError:
    print("Error: Tipo de dato no válido.")
else:
    print("Suma:", Ejercicio08Operaciones.suma(num1, num2))
    print("Resta:", Ejercicio08Operaciones.resta(num1, num2))
    print("Producto:", Ejercicio08Operaciones.producto(num1, num2))
    print("División:", Ejercicio08Operaciones.division(num1, num2))

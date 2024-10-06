# menu.py
from Ejercicio09Figuras import Circulo, Rectangulo, Cuadrado

def validar_numero(valor):
    try:
        numero = float(valor)
        if numero <= 0:
            raise ValueError("El número debe ser positivo.")
        return numero
    except ValueError:
        print("Error: Ingrese un número válido y positivo.")
        return None

def main():
    while True:
        print("\nMenu:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            radio = None
            while radio is None:
                radio_input = input("Ingrese el radio del círculo: ")
                radio = validar_numero(radio_input)
            circulo = Circulo(radio)
            print(f"El área del círculo es: {circulo.area():.2f}")

        elif opcion == '2':
            largo = None
            ancho = None
            while largo is None:
                largo_input = input("Ingrese el largo del rectángulo: ")
                largo = validar_numero(largo_input)
            while ancho is None:
                ancho_input = input("Ingrese el ancho del rectángulo: ")
                ancho = validar_numero(ancho_input)
            rectangulo = Rectangulo(largo, ancho)
            print(f"El área del rectángulo es: {rectangulo.area():.2f}")

        elif opcion == '3':
            lado = None
            while lado is None:
                lado_input = input("Ingrese el lado del cuadrado: ")
                lado = validar_numero(lado_input)
            cuadrado = Cuadrado(lado)
            print(f"El área del cuadrado es: {cuadrado.area():.2f}")

        elif opcion == '4':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

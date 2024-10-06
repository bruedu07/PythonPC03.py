def porc_gasalina():
    while True:
        try:
            fraction = input("Ingrese la fracción en formato X/Y: ")
            x, y = fraction.split('/')

            x = int(x)
            y = int(y)

            if y == 0:
                raise ZeroDivisionError

            if x > y:
                raise ValueError("X no puede ser mayor que Y.")

            percentage = (x / y) * 100

            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return f"{round(percentage)}%"
        
        except ValueError:
            print("Error: Debe ingresar números enteros en el formato X/Y y X debe ser menor o igual a Y.")
        except ZeroDivisionError:
            print("Error: Y no puede ser cero.")

print(porc_gasalina())

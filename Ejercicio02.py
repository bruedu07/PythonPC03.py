def separar_notas():
    while True:
        try:
            notas = input("Ingrese las notas separadas por comas: ")
            
            notas_lista = notas.split(',')
            
            notas_enteros = [int(calificacion.strip()) for calificacion in notas_lista]

            return notas_enteros
        
        except ValueError:
            print("Error: Asegúrese de ingresar solo números enteros separados por comas.")

notas = separar_notas()
print("Calificaciones:", notas)

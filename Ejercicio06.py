class Producto:
    def __init__(self, nombre, precio, marca, año):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.año = año

class Catalogo:
    def __init__(self):
        self.productos = [] 

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if len(self.productos) == 0:
            print("El catálogo está vacío.")
        else:
            print("Lista de productos en el catálogo:")
            for producto in self.productos:
                print(f"Producto: {producto.nombre}, Precio: {producto.precio}, Marca: {producto.marca}, Año: {producto.año}")

    def filtrar_por_año(self, año):
        print(f"\nProductos del año {año}:")
        for producto in self.productos:
            if producto.año == año:
                print(f"Producto: {producto.nombre}, Precio: {producto.precio}, Marca: {producto.marca}")
        print()

    def filtrar_por_marca(self, marca):
        print(f"\nProductos de la marca {marca}:")
        for producto in self.productos:
            if producto.marca == marca:
                print(f"Producto: {producto.nombre}, Precio: {producto.precio}, Año: {producto.año}")
        print()


producto1 = Producto("Batería", 150, "Toyota", 2023)
producto2 = Producto("Frenos", 120, "Mazda", 2021)
producto3 = Producto("Filtro de aire", 50, "Kia", 2023)

mi_catalogo = Catalogo()
mi_catalogo.agregar_producto(producto1)
mi_catalogo.agregar_producto(producto2)
mi_catalogo.agregar_producto(producto3)

mi_catalogo.mostrar_productos()

mi_catalogo.filtrar_por_año(2023)

mi_catalogo.filtrar_por_marca("Mazda")

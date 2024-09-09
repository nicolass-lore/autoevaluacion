class EquipoDeportivo:
    def __init__(self, nombre, fecha_creacion, precio_costo, precio_venta, cantidad_stock, descripcion):
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.precio_costo = precio_costo
        self.precio_venta = precio_venta
        self.cantidad_stock = cantidad_stock
        self.descripcion = descripcion

    def vender(self, cantidad_vendida):
        if cantidad_vendida > self.cantidad_stock:
            print("No hay suficiente stock para vender esa cantidad")
        else:
            self.cantidad_stock -= cantidad_vendida
            print(f"Se vendieron {cantidad_vendida} unidades de {self.nombre}. Cantidad en stock actual: {self.cantidad_stock}")

    def __str__(self):
        return f"Nombre: {self.nombre}\nFecha de creación: {self.fecha_creacion}\nPrecio costo: {self.precio_costo}\nPrecio venta: {self.precio_venta}\nCantidad en stock: {self.cantidad_stock}\nDescripción: {self.descripcion}"


# Crear equipos deportivos
equipo1 = EquipoDeportivo("Pelota de fútbol", "2022-02-08", 100, 150, 10, "Pelota de fútbol de alta calidad")
equipo2 = EquipoDeportivo("Raqueta de tenis", "2024-05-15", 50, 75, 5, "Raqueta de tenis para principiantes")

# Imprimir datos de los equipos
print(equipo1)
print(equipo2)

# Vender equipos
equipo1.vender(3)
equipo2.vender(2)

# Imprimir datos actualizados
print(equipo1)
print(equipo2)
class Cliente:
    
    def __init__(self, cedula, nombres, direccion, telefono, email):
        self.cedula=cedula
        self.nombres=nombres
        self.direccion=direccion
        self.telefono=telefono
        self.email=email

    def __str__(self):
        return '{};{};{};{};{}\n'.format(self.cedula, self.nombres, self.direccion, self.telefono, self.email)

class Producto:
    
    def __init__(self, codigo, nombre, detalle, precio):
        self.codigo=codigo
        self.nombre=nombre
        self.detalle=detalle
        self.precio=precio

    def __str__(self):
        return '{};{};{};{}\n'.format(self.codigo, self.nombre, self.detalle, self.precio)

class Venta:
    
    def __init__(self, codigo, cedula, fecha, subtotal, descuento, iva, total):
        self.codigo=codigo
        self.cedula=cedula
        self.fecha=fecha
        self.subtotal=subtotal
        self.descuento=descuento
        self.iva=iva
        self.total=total

    def calcularTotal():
        pass

    def __str__(self):
        return '{};{};{};{};{};{};{}\n'.format(self.codigo, self.cedula, self.fecha, self.subtotal, self.descuento, self.iva, self.total)

class DetalleVentas:

    def __init__(self, codigoProducto, cantidad, total):
        self.codigoVenta=None
        self.codigoProducto=codigoProducto
        self.cantidad=cantidad
        self.total=total

    def __str__(self):
        return '{};{};{};{}\n'.format(self.codigoVenta, self.codigoProducto, self.cantidad, self.total)

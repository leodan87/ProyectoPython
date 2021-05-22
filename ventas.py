import productos as pro #Importa la librería productos
import clientes as cli #Importa la librería clientes
from models import DetalleVentas, Venta
from datetime import date
import random
#CONSTANTES GLOBALES
IVA=12
DESCUENTO=1
RUTA_ARCHIVO1='./archivos/ventas.txt'
RUTA_ARCHIVO2='./archivos/detalleVenta.txt'

def guardarVenta(cedula, subtotal, descuento, iva, total, listaDetallesVenta):
    fecha=date.today().strftime('%d-%m-%y')
    codigo=random.randint(1,1000000) #Código de Venta
    
    #Guardo la Venta
    venta=Venta(codigo, cedula, fecha, subtotal, descuento, iva, total)

    archivoVen=open(RUTA_ARCHIVO1, 'a')
    archivoVen.write(str(venta))
    archivoVen.close()

    #Guardo los Detalles de Venta
    archivoDetVen=open(RUTA_ARCHIVO2, 'a')
    for objDetVen in listaDetallesVenta:
        objDetVen.codigoVenta=codigo #Le doy el valor del código de venta
        archivoDetVen.write(str(objDetVen))
    archivoDetVen.close()

def gestionVentas():
    while True:
        print('\nGESTIÓN DE VENTAS')
        print('1. Realizar Venta')
        print('2. Historial Ventas')
        print('3. Atrás')
        opcion=input('Opción: ')
        if opcion=='1':
            listaDetallesVenta=list() #Creo una lista de Detalles de Venta
            cedula=input('Cédula cliente: ')

            cliente=cli.validarCedulaCliente(cedula) #Retorna un objeto de tipo Cliente
            
            if cliente!=None: #Si encontró al cliente
                print('# Datos del Cliente #')
                print('> Nombres: {} \t\t > Teléfono: {}'.format(cliente.nombres, cliente.telefono))
                print('> Dirección: {} \t\t > Email: {}'.format(cliente.direccion, cliente.email))

                print('# Ingreso de Compras #')
                subtotal=0 #Subtotal de la Venta
                while True:
                    codigo=input('-> Código (0-Finalizar): ') #Validar si ese código existe en mi archivo Productos.txt
                    if codigo=='0': #Si es 0 se detiene la venta
                        break
                    producto=pro.validarCodigoProducto(codigo)
                    if producto!=None: #Cuando encuentra el producto
                        print('# Datos del Producto #')
                        print('> Nombre: {} \t > Detalle: {} \t > Precio Unitario: ${}'.format(producto.nombre, producto.detalle, producto.precio))

                        cantidad=int(input('-> Cantidad: '))
                        totalProducto=round(cantidad*float(producto.precio), 2) #Subtotal del Producto
                        
                        #Creo el objeto
                        detalleVenta=DetalleVentas(codigo, cantidad, totalProducto)
                        listaDetallesVenta.append(detalleVenta)

                        subtotal+=totalProducto
                        print('-> Total: $',totalProducto)
                        #Guardar en Detalle de Venta
                    else:
                        print('Producto no existe.')
                        continue
                #Realizar los cálculos del venta
                print('Subtotal: $',subtotal)
                descuento=subtotal*DESCUENTO/100
                print('Descuento '+str(DESCUENTO)+'%: $',descuento)
                subtotal-=descuento #Aplico el descuento antes del IVA
                iva=subtotal*IVA/100
                print('IVA '+str(IVA)+'%: $',round(iva,2))
                totalVenta=subtotal+iva
                print('Total: $', round(totalVenta,2))

                guardarVenta(cliente.cedula, subtotal, descuento, iva, totalVenta, listaDetallesVenta)

            else: #Si no lo encuentra llamo a la función de IngresarCliente
                print('-> Crear Cliente')
                cli.crearCliente()
        elif opcion=='2':
            historialVentas()
        else:
            break

def historialVentas():
    pass
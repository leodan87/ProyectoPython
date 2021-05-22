from models import Producto

RUTA_ARCHIVO='./archivos/productos.txt'

def crearProducto():
    codigo=input('Código: ')
    nombre=input('Nombre: ')
    detalle=input('Detalle: ')
    precio=float(input('Precio: '))

    producto=Producto(codigo, nombre, detalle, precio)

    archivoProd=open(RUTA_ARCHIVO, 'a')
    archivoProd.write(str(producto)) #123;Lápiz;Mongol;0.25
    archivoProd.close()

def mostrarArchivo(archivo):
    pass

def gestionProductos():
    while True:
        print('\nGESTIÓN DE PRODUCTOS')
        print('1. Ingresar Producto')
        print('2. Mostrar Productos')
        print('3. Atrás')
        opcion=input('Opción: ')
        if opcion=='1':
            crearProducto()
            print('¡Guardado correctamente!')
        elif opcion=='2':
            archivoProd=open(RUTA_ARCHIVO, 'r')
            #Presentar los productos bien
            print('Código\tNombre\t\tDetalle\t\tPrecio')
            for linea in archivoProd.readlines():
                atributos=linea.split(';')
                print('{}\t{}\t\t{}\t\t{}'.format(atributos[0], atributos[1], atributos[2], atributos[3]))
            archivoProd.close()
        else:
            break

def validarCodigoProducto(codigo):
    #Si encuentra que devuelva la línea
    #Si no encuentra que devuelva un null (None)
    producto=None #Valor inicial
    archivoProd=open(RUTA_ARCHIVO, 'r')
    for linea in archivoProd.readlines():
        atributos=linea.split(';')
        if codigo==atributos[0]: #Si encuentra el código en el archivo
            producto=Producto(atributos[0], atributos[1], atributos[2], atributos[3])            
            break
    archivoProd.close()

    return producto
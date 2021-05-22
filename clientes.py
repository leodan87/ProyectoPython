from models import Cliente

RUTA_ARCHIVO='./archivos/clientes.txt'

def crearCliente():
    cedula=input('Cédula: ')
    nombres=input('Nombres Completo: ')
    direccion=input('Dirección: ')
    telefono=input('Teléfono: ')
    email=input('Correo electrónico: ')

    #Creo el objeto de la clase Cliente
    cliente=Cliente(cedula, nombres, direccion, telefono, email)

    archivoCli=open(RUTA_ARCHIVO, 'a')
    archivoCli.write(str(cliente))
    archivoCli.close()

def gestionClientes():
    while True:
        print('\nGESTIÓN DE CLIENTES')
        print('1. Ingresar Cliente')
        print('2. Mostrar Clientes ')
        print('3. Atrás')
        opcion=input('Opción: ')
        if opcion=='1':
            crearCliente()
            print('¡Guardado correctamente!')
        elif opcion=='2':
            archivoCli=open(RUTA_ARCHIVO, 'r')
            #Presentar los productos bien
            print('Cédula\tNombres\t\tDirección\t\tTeléfono\tEmail')
            for linea in archivoCli.readlines():
                atributos=linea.split(';')
                print('{}\t{}\t{}\t{}\t{}'.format(atributos[0], atributos[1], atributos[2], atributos[3], atributos[4]))
            archivoCli.close()
        else:
            break

def validarCedulaCliente(cedula):
    cliente=None
    archivoCliente=open(RUTA_ARCHIVO, 'r')
    for linea in archivoCliente.readlines():
        atributos=linea.split(';')
        if cedula==atributos[0]: #Si encuentro el cliente
            cliente=Cliente(atributos[0], atributos[1], atributos[2], atributos[3], atributos[4])
            break
    archivoCliente.close()
    return cliente
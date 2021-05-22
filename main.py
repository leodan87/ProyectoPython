import productos as pro
import clientes as cli
import ventas as ven

while True:
    print('\t##> PAPELERÍA DON LEO <##')
    print('MENÚ PRINCIPAL')
    print('1. Gestión Productos')
    print('2. Gestión Clientes')
    print('3. Gestión Ventas')
    print('0. Salir')
    opcion = input('Opción: ')

    if opcion=='1':
        pro.gestionProductos()
    elif opcion=='2':
        cli.gestionClientes()
    elif opcion=='3':
        ven.gestionVentas()
    else:
        print('Saliendo del sistema.. Hasta pronto.')
        break
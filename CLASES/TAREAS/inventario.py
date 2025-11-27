#gestor de inventarios


inventarios = []

def mostrar_menu():
    
    print('\n === GESTION DE INVENTARIOS ===')
    print('1. agregar producto')
    print('2. mostrar inventario')
    print('3. buscar producto')
    print('4. eliminar producto')
    print('5. salir')
    
while True: 
    mostrar_menu()
    opcion = input('selecciona una opcion')
if opcion == '1':
        producto = input('nombre del producto:')
        invetanrios.append(producto)
        print(f'{producto} agregado al inventario')
elif opcion == '2':
    print('\n=== INVENTARIO ===')
    for i, producto in enumerate(inventarios,1):
        print(f'{i}. {producto}') 
    else: print('inventario; vacio')
elif opcion == '3':
    if inventarios: buscar = input('producto a buscar:')
    if buscar in inventario: posicion = inventario.index(buscar) + 1 
    print(f'{buscar} encontrado en posicion{posicion}')
else: print(f'{buscar} no encontrado')

elif opcion == '4':
if inventario: print('producto disponible:')
for i, producto in enumerate(inventario, 1):
    print(f'{i}. {producto}')
    try: indice = int(input('numero de producto a eliminar:')) - 1
    producto_eliminado = inventario.pop(indice)
print(f'{producto_eliminado} eliminado del inventario') 
except:
print('numero invalido')
else: print('inventario vacio')
elif opcion =='5':
    print('hasta luego') break
    else: print('opcion invalida')
estudiantes = []

cantidad = int(input('cuantos estudiantes desea registrar'))

for _ in range(cantidad):
    print('\n === registro de estudiantes ===')
    nombre = input('nombre del estudiante')
    
    n1 = float(input('nota 1:'))
    n2 = float(input('nota 2:'))
    n3 = float(input('nota 3:'))
    
    promedio = (n1 + n2 + n3) /3
    
    
    estudiantes.append({
    'nombre':  nombre,
    'notas':  [n1, n2, n3],
    'promedio':  promedio
    })
    
    
#clasificacion

aprobados = []
desaprobados = []

for est in estudiantes:
    if est['promedio'] >= 13:
        aprobados.append(est)
    else:
        desaprobados.append(est)
        
# --------- reporte final --------------
print('\n' + '='*40)
print('reporte final')
print('='*40)

print('\n aprobados (primedio >=13):')

if aprobados:
    for est in aprobados:
        print(f'{est['nombre']} - promedio : {est['promedio']:.2f}')
else:
    print('ninguno')
    
print('\n fin de reporte.')
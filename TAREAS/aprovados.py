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
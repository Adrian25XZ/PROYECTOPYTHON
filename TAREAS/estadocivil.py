nombre = input('ingresa tu nombre:')
edad = int(input('ingresa tu edad'))
estado_civil = input('estado civil(casado/soltero):').lower()
print(f'=== analisis para {nombre.upper()} ===')
#validacion de edad

if edad < 0:
    print('edad invalida')
elif edad < 18:
    print('menor a 18')
    print('no puede volar')
elif edad >= 18 and edad < 65:
    print('puede volar')
    print('en edad laboral activa')
else:
    print('adulto mayor')
    print('puede volar')
    print('elegible para jubilacion')
    
    
#validacion de estado civil

if estado_civil == 'soltero':
    print('estado: soltero/a')

elif estado_civil == 'casado':
    print('estado: casado/a')

else:
    print('estado civil no reconocido')
    

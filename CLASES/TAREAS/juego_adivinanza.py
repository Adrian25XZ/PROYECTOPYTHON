import random

numero_secreto = random.randint(1,100)
intentos = 0
adivinado = False

print('juego de adivinanza')
print('he pensado un numero del 1 al 100')
print('trata de adivinarlo')

while not adivinado:
    intento = int(input('\n ingresa tu numero'))
    intentos += 1
    if intento < numero_secreto:
        print('muy bajo intentelo con un numero mayor')
    elif intento > numero_secreto:
        print('muy alto intente con un numero menor')
    else:
        print(f'felicidades adivinaste el numero secreto {numero_secreto}')
        print(f'lo lograste en {intentos} intentos')
        adivinado = True
        print('gracias por jugar')
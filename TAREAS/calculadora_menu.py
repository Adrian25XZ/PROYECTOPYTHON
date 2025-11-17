print('=== CALCULADORA PYTHON ===')

print('1.suma')
print('2.resta')
print('3.multiplicacion')
print('4.division')

opcion = int(input('seleccione una opcion (1-4):'))
num1 = float(input('primer numero:'))
num2 = float(input('segundo numero'))


if opcion == 1:
    resultado = num1 + num2
    print(f'{num1} + {num2} = {resultado}')
    
elif opcion == 2:
    resultado = num1 - num2
    print(f'{num1} - {num2} = {resultado}')
    
elif opcion == 3:
    resultado = num1 * num2
    print(f'{num1} * {num2} = {resultado}')
    
elif opcion == 4:
    if num2 != 0:
        resultado = num1 / num2
        print(f'{num1} / {num2} = {resultado}')
    else:
        print(f'error: no se puede dividir entre cero')
else:
    print('opcion invalida')
    
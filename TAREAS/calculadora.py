#calculadora basica

print('=== CALCULADORA BASICA ===')

#solicitar numeros al usuario

num1 = float(input('ingrese el primer numero:'))
num2 = float(input('ingrese el segundo numero'))

#realizar la operacion suma = num1 + num2 restar = num1 - num2 multiplicar = num1 * num2 dividir = num1 / num2
#mostrar resultados

suma = num1 + num2
resta = num1 - num2
multiplicar = num1 * num2
dividir = num1 / num2


print(f'\n === RESULTADOS ===')
print(f'{num1} + {num2} = {suma}')
print(f'{num1} - {num2} = {resta}')
print(f'{num1} * {num2} = {multiplicar}')
print(f'{num1} / {num2} = {dividir}')

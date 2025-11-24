numero = int(input('que tabla de multiplicar quieres?'))
print(f'\n === tabla del {numero} ===')

for i in range(1,11):
    resultado = numero * i
    print(f'{numero} x {i:2} = {resultado:3}')
    print('\n' + '=' * 25)
    print('tabla completada')
print('=== CONTADOR DE PARES E IMPARES ===')

limite = int(input('ingrese el numero limite'))
pares = 0
impares = 0

print('f\n analizando numeros del 1 al {limite}:')
for numero in range(1,limite +1):
    if numero % 2 == 0:
        print(f'el {numero} es par')
        pares +=1
    else:
        print(f'{numero} es impar')
        impares += 1
print(f'=== RESUMEN ===')
print(f'numero de pares encontrados: {pares}')
print(f'numero de inpares encontrados: {impares}')
print(f'total de numeros analizados{pares + impares }')
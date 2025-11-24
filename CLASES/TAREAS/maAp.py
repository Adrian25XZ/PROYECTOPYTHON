from functools import reduce
import math


#map: aplica funcion a cada elemento

numeros = [1, 2, 3, 4, 5]
cuadros = list(map(lambda x: x**2, numeros))
potencia = list(map(lambda x: pow(x,3), numeros))
raiz = list(map(lambda x: math.sqrt(x), numeros))
print(f"esta lista numeros: {numeros}")
print(f"esta es la lista cuadros {cuadros}")
print(potencia)
print(f"la raiz cuadrada del numero {numeros} es {raiz}")

#filter: filtra elementos segun condicion

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros, pares)

#reduce: reduce lista a un solo valor

suma_total = reduce(lambda x, y: x + y, numeros)

print(suma_total)

#comprension de listas - estilos funcional
cuadrados = [x**2 for x in range (10)]
pares = [x for x in range (20) if x % 2 ==0]

print()
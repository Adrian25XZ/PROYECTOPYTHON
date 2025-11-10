Funciones en Python
===================

¿Qué es una función?
--------------------

Una *función* es un bloque de código reutilizable que realiza una tarea específica.

Imagina que escribes el mismo código muchas veces. Una función te permite escribirlo una sola vez 
y usarlo cuantas veces necesites.

Crear una función
-----------------

.. code-block:: python

   def saludar():
       print("¡Hola, bienvenido a Python!")

   saludar()  # Ejecuta la función

Funciones con parámetros
-------------------------

Los *parámetros* son valores que pasa a la función:

.. code-block:: python

   def saludar(nombre):
       print(f"¡Hola, {nombre}!")

   saludar("Juan")
   saludar("María")

Funciones con retorno
---------------------

Una función puede *devolver* un valor:

.. code-block:: python

   def sumar(a, b):
       resultado = a + b
       return resultado

   suma = sumar(5, 3)
   print(suma)  # 8

Múltiples parámetros
---------------------

.. code-block:: python

   def calcular_promedio(nota1, nota2, nota3):
       promedio = (nota1 + nota2 + nota3) / 3
       return promedio

   promedio = calcular_promedio(8, 9, 7)
   print(promedio)  # 8.0

Ejercicios
----------

1. Crea una función que reciba un número y devuelva su doble
2. Crea una función que reciba dos números y devuelva el mayor
3. Crea una función que reciba tu nombre y edad, y imprima un mensaje
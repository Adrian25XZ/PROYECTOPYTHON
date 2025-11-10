Control de Flujo
================

¿Qué es el control de flujo?
----------------------------

El *control de flujo* permite que tu programa tome decisiones y repita acciones.

Hay dos estructuras principales: *if/else* y *bucles*.

Condicionales (if/else)
-----------------------

La estructura *if/else* ejecuta código según una condición:

.. code-block:: python

   edad = 18

   if edad >= 18:
       print("Eres mayor de edad")
   else:
       print("Eres menor de edad")

Múltiples condiciones (elif)
-----------------------------

.. code-block:: python

   calificacion = 85

   if calificacion >= 90:
       print("Excelente")
   elif calificacion >= 80:
       print("Muy bien")
   elif calificacion >= 70:
       print("Bien")
   else:
       print("Necesitas estudiar más")

Operadores de comparación
--------------------------

.. code-block:: python

   ==  # igual
   !=  # no igual
   >   # mayor que
   <   # menor que
   >=  # mayor o igual
   <=  # menor o igual

Bucle for
---------

Repite código una cantidad definida de veces:

.. code-block:: python

   for i in range(5):
       print(i)  # Imprime 0, 1, 2, 3, 4

Recorrer una lista con for:

.. code-block:: python

   numeros = [1, 2, 3, 4, 5]
   for numero in numeros:
       print(numero)

Bucle while
-----------

Repite código mientras se cumpla una condición:

.. code-block:: python

   contador = 0
   while contador < 5:
       print(contador)
       contador = contador + 1

Ejercicios
----------

1. Crea un programa que pida la edad y diga si es mayor de edad
2. Crea un bucle que imprima los números del 1 al 10
3. Crea un bucle que imprima la tabla de multiplicar del 5
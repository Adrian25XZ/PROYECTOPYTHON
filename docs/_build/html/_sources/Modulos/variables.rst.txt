Variables en Python
===================

¿Qué es una variable?
---------------------

Una *variable* es un contenedor que almacena un valor en la memoria de tu computadora.

Piensa en una variable como una caja con una etiqueta:
- La etiqueta es el *nombre de la variable*
- El contenido es el *valor*

Crear variables
---------------

.. code-block:: python

   nombre = "Juan"
   edad = 20
   altura = 1.75
   es_estudiante = True

   print(nombre)
   print(edad)

Tipos de datos básicos
-----------------------

*String (texto):*

.. code-block:: python

   pais = "Argentina"
   mensaje = "Hola, mundo"

*Integer (números enteros):*

.. code-block:: python

   numero = 42
   negativo = -10

*Float (números decimales):*

.. code-block:: python

   pi = 3.14159
   temperatura = 25.5

*Boolean (verdadero/falso):*

.. code-block:: python

   verdadero = True
   falso = False

Operaciones con variables
--------------------------

.. code-block:: python

   # Suma
   a = 10
   b = 5
   suma = a + b
   print(suma)  # 15

   # Concatenación de strings
   nombre = "Juan"
   apellido = "Pérez"
   nombre_completo = nombre + " " + apellido
   print(nombre_completo)  # Juan Pérez

Ejercicios
----------

1. Crea una variable con tu nombre y otra con tu edad
2. Crea dos números y suma los resultados
3. Crea una variable con tu ciudad y otra con tu país, luego concatenálas
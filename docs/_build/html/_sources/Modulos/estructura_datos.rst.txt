Estructuras de Datos
====================

¿Qué es una estructura de datos?
--------------------------------

Una *estructura de datos* es una forma de organizar múltiples valores en una sola variable.

Python tiene varias estructuras principales: *listas, tuplas y diccionarios*.

Listas
------

Una *lista* es una colección ordenada de elementos que puede modificarse:

.. code-block:: python

   frutas = ["manzana", "banana", "naranja"]
   print(frutas[0])  # manzana
   print(frutas[1])  # banana

Agregar elementos:

.. code-block:: python

   frutas = ["manzana", "banana"]
   frutas.append("naranja")
   print(frutas)  # ['manzana', 'banana', 'naranja']

Recorrer una lista:

.. code-block:: python

   frutas = ["manzana", "banana", "naranja"]
   for fruta in frutas:
       print(fruta)

Tuplas
------

Una *tupla* es similar a una lista, pero NO se puede modificar:

.. code-block:: python

   colores = ("rojo", "verde", "azul")
   print(colores[0])  # rojo
   print(colores[1])  # verde

Diccionarios
------------

Un *diccionario* almacena pares de clave-valor:

.. code-block:: python

   persona = {
       "nombre": "Juan",
       "edad": 20,
       "ciudad": "Buenos Aires"
   }

   print(persona["nombre"])  # Juan
   print(persona["edad"])    # 20

Agregar elementos:

.. code-block:: python

   persona = {"nombre": "Juan"}
   persona["edad"] = 20
   persona["ciudad"] = "Buenos Aires"
   print(persona)

Recorrer un diccionario:

.. code-block:: python

   persona = {"nombre": "Juan", "edad": 20, "ciudad": "Buenos Aires"}
   
   for clave, valor in persona.items():
       print(f"{clave}: {valor}")

Ejercicios
----------

1. Crea una lista con 5 números y imprime el primero y el último
2. Crea un diccionario con tus datos personales (nombre, edad, ciudad)
3. Crea una lista de estudiantes y agrega 2 más
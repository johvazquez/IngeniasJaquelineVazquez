# -*- coding: utf-8 -*-
"""Notebook 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NGGJyM8BKDZKwcKEwsOeQe7C11-srOHx

# Programa Ingenias+ Data Science

Como dijimos en clases anteriores, Python tiene implementadas muchas librerias para poder trabajar con datos. En la clase de hoy trabajaremos con una de ellas: `Numpy`.

Antes de comenzar, vamos a hablar un poco de esta libreria o modulo.

**Numpy** es una librería optimizada para realizar cálculos numéricos con vectores y matrices. A diferencia de otros lenguajes de programación, Python no posee en su estructura central la figura de matrices. Eso quiere decir que para poder trabajar con esta estructura de datos deberiamos trabajar con listas de listas. NumPy introduce el concepto de arrays o matrices.

Al ser de código abierto, `numpy` posee una documentación muy amplia que es **SIEMPRE RECOMENDABLE** consultar.

- [Documentacion NumPy](https://devdocs.io/numpy/)

## Clase 4: Introduccion a NumPy

# Ejercicios

1. Crear un arreglo de ceros de longitud 12
2. Crear un arreglo de longitud 10 con ceros en todas sus posiciones y un 10 en la posición número 5
3. Crear un arreglo que tenga los números del 10 al 49
4. Crear una arreglo 2d de shape (3, 3) que tenga los números del 0 al 8
5. Crear un arreglo de números aleatorios de longitud 100 y obtener su media y varianza
6. Calcular la media de un arreglo usando np.sum
7. Calcular la varianza de un arreglo usando np.sum y np.mean
8. Crear un array de números aleatorios usando np.random.randn.
"""

import numpy as np

"""1) Crear un arreglo de ceros de longitud 12"""

arreglo_ceros = np.zeros(12)
print(arreglo_ceros)

"""2) Crear un arreglo de longitud 10 con ceros en todas sus posiciones y un 10 en la posición número 5"""

arreglo = np.zeros(10)
arreglo[4] = 10  # La posición número 5 tiene índice 4
print(arreglo)

"""3) Crear un arreglo que tenga los números del 10 al 49"""

arreglo = np.arange(10, 50) #numpy.arange() de NumPy es una función que permite generar una secuencia de números especificando un valor inicial, un valor final y un paso (opcional)
print(arreglo)

"""4) Crear una arreglo 2d de shape (3, 3) que tenga los números del 0 al 8"""

# Primero creo un arreglo 1D con los números del 0 al 8
arreglo_1d = np.arange(9)
# Luego usando Reshape para convertirlo en un arreglo 2D de forma (3, 3)
arreglo_2d = arreglo_1d.reshape((3, 3))

print(arreglo_2d)

"""5) Crear un arreglo de números aleatorios de longitud 100 y obtener su media y varianza"""

# Creo un arreglo de 100 números aleatorios entre 0 y 1
arreglo_aleatorio = np.random.rand(100)

# Calculo la media y la varianza del arreglo
media = np.mean(arreglo_aleatorio)
varianza = np.var(arreglo_aleatorio)

print("Arreglo de números aleatorios:")
print(arreglo_aleatorio)
print("\nMedia:", media)
print("Varianza:", varianza)

"""6) Calcular la media de un arreglo usando np.sum"""

# Creo un arreglo
arreglo = np.array([1, 2, 3, 4, 5])
# Calculo la media utilizando np.sum y len
media = np.sum(arreglo) / len(arreglo) #np.sum(arreglo)suma todos los elementos del arreglo, y len(arreglo) devuelve la cantidad de elementos en el arreglo

print("Arreglo:", arreglo)
print("Media:", media)

"""7) Calcular la varianza de un arreglo usando np.sum y np.mean"""

# Calculo las diferencias entre cada elemento y la media
diferencias = arreglo - media
# Calcular el cuadrado de las diferencias
cuadrados_diferencias = diferencias**2
# Calcular la varianza utilizando np.sum y np.mean
varianza = np.sum(cuadrados_diferencias) / len(arreglo)
print("Arreglo:", arreglo)
print("Varianza:", varianza)

"""8) Crear un array de números aleatorios usando np.random.randn."""

arreglo_aleatorio = np.random.randn(10)
print(arreglo_aleatorio)
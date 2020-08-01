# -*- coding: utf-8 -*-
"""
Decorador @vectorize para generar una versión compilada de la función "add_matrix_numba" en tiempo de ejecución,
a fin de que pueda usarse para procesar matrices de datos en paralelo en la GPU.

Requisitos:
Python 3.7.6
Conda 4.8.2

Install:

$> conda install numba, cudatoolkit

Información:
Python Compiler : MSC v.1916 64 bit (AMD64)
LLVM version : 8.0.0
numba: 0.48.0
"""
# from MachineInfo import MachineInfo
from numba import vectorize, float32
import numpy as np
import time


@vectorize(['float32(float32, float32)'], target='cpu')
def add_matrix_numba(x, y):
    return x+y


def add_matrix(x, y):
    return x+y


if __name__ == "__main__":
    n = 1000
    x = np.ones(n, dtype=np.float32)
    y = np.ones(n, dtype=np.float32)
    time_1 = int(round(time.time() * 1000))
    print("Suma de matrices (sin numba): ")
    S1 = add_matrix(x, y)
    print(S1)
    time_2 = int(round(time.time() * 1000))
    print('Tiempo {} ms'.format(time_2-time_1))
    # Add arrays on GPU
    time_3 = int(round(time.time() * 1000))
    S2 = add_matrix_numba(x, y)
    print(S2)
    time_4 = int(round(time.time() * 1000))
    print('Tiempo {} ms'.format(time_4-time_3))

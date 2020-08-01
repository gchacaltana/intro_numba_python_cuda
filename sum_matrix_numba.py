# -*- coding: utf-8 -*-
"""
Decorador @vectorize para generar una versión compilada de la función “Add” en tiempo de ejecución,
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
import numpy as np
from numba import vectorize


@vectorize(['float32(float32, float32)'], target='cuda')
def Add(a, b):
    return a + b


if __name__ == "__main__":
    # Inicializando Arrays
    N = 100
    A = np.ones(N, dtype=np.float32)
    print("A")
    print(A)
    B = np.ones(A.shape, dtype=A.dtype)
    print("B")
    print(B)
    C = np.empty_like(A, dtype=A.dtype)
    print("C")
    print(C)
    print(np.sum(C))
    # Add arrays on GPU
    D = Add(A, B)
    print(D)
# This is an optimized version of cython1.pyx
# import numpy
from libc.math cimport log

cdef int factorial (int n):
    if n==1:
        return 1
    return n * factorial(n-1)

print(log(10)/log(2))
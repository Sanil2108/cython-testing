import pyximport
pyximport.install()

from cython1 import factorial

print(factorial(10))
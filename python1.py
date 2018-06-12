import pyximport
pyximport.install()

import cython1

print(cython1.factorial(10))
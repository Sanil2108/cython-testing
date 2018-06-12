from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Cython10',
  ext_modules = cythonize("cython1.pyx"),
)
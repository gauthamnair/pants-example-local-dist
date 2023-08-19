from setuptools import setup
from Cython.Build import cythonize

compiled = cythonize("src/foo/bar.pyx")

setup(
    ext_modules=compiled
)

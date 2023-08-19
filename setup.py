from setuptools import setup
from Cython.Build import cythonize

compiled = cythonize("src/foo/bar.pyx")

setup(
    name="foo",
    version="0.0.1",
    url="https://github.com/gauthamnair/pants-exmaple-local-dist",
    author="Gautham Nair",
    author_email="gautham@example.com",
    ext_modules=compiled,
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=["tabulate"],
    packages=["foo"],
)

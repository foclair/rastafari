"""Build and install Rastafari."""

import os

from setuptools import Extension, setup

USE_CYTHON = os.environ.get("RASTAFARI_USE_CYTHON", False)

ext = "pyx" if USE_CYTHON else "c"
extensions = [
    Extension("rastafari.core", [f"src/rastafari/core.{ext}"]),
]
if USE_CYTHON:
    from Cython.Build import cythonize

    extensions = cythonize(extensions, compiler_directives={"language_level": "3"})

setup(ext_modules=extensions)

from setuptools import setup, Extension

setup(name='graph',
      version='1.0',
      ext_modules=[Extension('graph', ['graphmodule.c'])])
#!/usr/bin/env python
import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

import xdressrc

incdirs = [xdressrc.sourcedir, np.get_include()]

ext_modules = [
    Extension("cya.xdress_extra_types", ["cya/xdress_extra_types.pyx"], 
              include_dirs=incdirs, language="c++"),
    Extension("cya.hdf5", ["cya/hdf5.pyx", ], libraries=['hdf5'],
               include_dirs=incdirs, language="c"),
    ]

setup(  
  name = 'cya',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
  packages = ['cya']
)

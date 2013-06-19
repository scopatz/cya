import os

sourcedir = "/home/scopatz/Downloads/hdf5-1.8.11/src"
package = "cya"

# Don't do too much
make_extra_types = False
make_stlcontainers = False
defines = ["H5_NO_DEPRECATED_SYMBOLS", "DIR=__dirstream"]

# Find source files and search for their contents
_fs = set(os.listdir(sourcedir))
_fs -= set(['H5FDsec2.c'])
_fs = sorted(_fs)
_fs = [('*', f.rsplit('.', 1)[0], 'hdf5') for f in _fs if f.endswith('.c')]
classes = list(_fs)
functions = list(_fs)
variables = list(_fs)


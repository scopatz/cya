import os

sourcedir = "/home/scopatz/Downloads/hdf5-1.8.11/src"
package = "cya"

# Don't do too much
make_extra_types = False
make_stlcontainers = False
defines = ["H5_NO_DEPRECATED_SYMBOLS", "DIR=__dirstream"]

clear_parser_memo_period = 25

# Find source files and search for their contents
_fs = set(os.listdir(sourcedir))
_fs -= set(['H5FDsec2.c', 'H5PL.c', 'H5FDstdio.c', 'H5FDcore.c', 'H5Dbtree.c', 
            'H5trace.c', 'H5FDlog.c', 'H5system.c'])
_fs = sorted(_fs)
_fs = [('*', f.rsplit('.', 1)[0], 'hdf5') for f in _fs if f.endswith('.c')]
#_fs = [('*', 'H5PL', 'hdf5')]

classes = list(_fs)
functions = list(_fs)
variables = list(_fs)


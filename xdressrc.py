import os
import io
from glob import glob

sourcedir = "/home/scopatz/Downloads/hdf5-1.8.11/src"
package = "cya"

# Don't do too much
make_extra_types = False
make_stlcontainers = False
defines = ["H5_NO_DEPRECATED_SYMBOLS", 
           "DIR=__dirstream", ]
clear_parser_memo_period = 25

# Fake out package headers
_pkgfiles = glob(os.path.join(sourcedir, '*pkg.h'))
for _pf in _pkgfiles:
    _src = _pf.rsplit('.', 1)[0] + '.c'
    _base = os.path.split(_pf)[1][:-5]
    _code = '#include "H5public.h"\n'
    if _base in set(['H5R', 'H5FS', 'H5B2', 'H5MF', 'H5F', 'H5HF', 'H5HG']):
        _code += '#include <stdio.h>\n'
    if _base == 'H5SM':
        _code += '#include <stdlib.h>\n#include "H5FLprivate.h"\n'
    elif _base == 'H5Z':
        _code += '#include "H5Iprivate.h"\n'
    _code += '#include "{base}pkg.h"\n'.format(base=_base)
    with io.open(_src, 'wb') as _f:
        _f.write(_code)
    defines.append(_base + "_PACKAGE")

# Find source files and search for their contents
_fs = set(os.listdir(sourcedir))
_fs -= set(['H5FDsec2.c', 'H5PL.c', 'H5FDstdio.c', 'H5FDcore.c', 'H5Dbtree.c', 
            'H5trace.c', 'H5FDlog.c', 'H5system.c',])
_fs = sorted(_fs)
_fs = [('*', f.rsplit('.', 1)[0], 'hdf5') for f in _fs \
       if f.endswith('.c')]
#_fs += [('*', 'H5Ppkg', 'hdf5')]

classes = list(_fs)
functions = list(_fs)
variables = list(_fs)


from os import path

import viscid
from viscid.plot import vpyplot as vlt


f3d = viscid.load_file(path.join(viscid.sample_dir, 'sample_xdmf.3d.xdmf'))

b = viscid.interp_trilin(f3d['bz'], viscid.Sphere(p0=(0, 0, 0), r=7.0))
vlt.plot(b, lin=0, hemisphere='north')

vlt.show()
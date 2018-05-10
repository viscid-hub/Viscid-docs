from os import path

import viscid
from viscid.plot import vpyplot as vlt


f3d = viscid.load_file(path.join(viscid.sample_dir, 'sample_xdmf.3d.xdmf'))

seeds = viscid.Volume((-20, 1, -20), (30, 1, 20), n=(64, 5, 64))
b = viscid.interp_trilin(f3d['b'], seeds)
vlt.plot(viscid.magnitude(b)['y=0f'], logscale=True, earth=True)

vlt.show()
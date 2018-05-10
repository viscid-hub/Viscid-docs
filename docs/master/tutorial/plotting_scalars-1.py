from os import path

import viscid
from viscid.plot import vpyplot as vlt


f3d = viscid.load_file(path.join(viscid.sample_dir, 'sample_xdmf.3d.xdmf'))
# notice y=0.0, this is different from y=0; y=0 is the 0th index in
# y, which is this case will be y=-50.0
pPa_to_dyne_per_cm2 = 1e-11
erg_to_K = (1.380e-16)**-1
fac = (2.0 / 3.0) * erg_to_K * pPa_to_dyne_per_cm2
T = fac * f3d["pp"] / f3d["rr"]
T.name = "T"
T.pretty_name = "T (K)"
vlt.plot(T['y=0f'], logscale=True, earth=True)

vlt.show()
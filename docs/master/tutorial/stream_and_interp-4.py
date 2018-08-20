from os import path

import numpy as np
import viscid
from viscid.plot import vpyplot as vlt


viscid.readers.openggcm.GGCMFile.read_log_file = True
viscid.readers.openggcm.GGCMGrid.mhd_to_gse_on_read = 'auto'


f3d = viscid.load_file(path.join(viscid.sample_dir, 'sample_xdmf.3d.xdmf'))

# make N and L directions for LMN magnetopause boundary normal crds
p0 = (9.0, 0.0, 1.5)
plane = viscid.Plane(p0, pN=[0, -1, 0], pL=[1, 0, 0.05], len_l=[-3, 3],
                     len_m=6.0, nl=64, nm=64)
slc = "x=6j:11j, y=-1j:1j, z=-10j:10j"
b = viscid.interp_trilin(f3d['b'][slc], plane)
j = viscid.interp_trilin(f3d['j'][slc], plane)

# rotate the vector so its components are in / normal to the plane
# that we interpolated onto
xyz_to_lmn = plane.get_rotation().T
b = b.wrap(np.einsum("ij,lm...j->lm...i", xyz_to_lmn, b))
j = j.wrap(np.einsum("ij,lm...j->lm...i", xyz_to_lmn, j))

vlt.plot(viscid.magnitude(j))
vlt.streamplot(b)

vlt.show()
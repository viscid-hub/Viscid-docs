import numpy as np
import viscid
from viscid.plot import vpyplot as vlt
from matplotlib import pyplot as plt


B = viscid.make_dipole(twod=True)
obound0 = np.array([-4, -4, -4], dtype=B.data.dtype)
obound1 = np.array([4, 4, 4], dtype=B.data.dtype)
lines, topo = viscid.calc_streamlines(B,
                                      viscid.Line((0.2, 0.0, 0.0),
                                                  (1.0, 0.0, 0.0), 10),
                                      ds0=0.01, ibound=0.1, maxit=10000,
                                      obound0=obound0, obound1=obound1,
                                      method=viscid.EULER1,
                                      stream_dir=viscid.DIR_BOTH,
                                      output=viscid.OUTPUT_BOTH)
topo_colors = viscid.topology2color(topo)
vlt.plot2d_lines(lines, topo_colors, symdir='y')
plt.ylim(-0.5, 0.5)

vlt.show()
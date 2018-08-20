from os import path

import numpy as np
import viscid
from viscid.plot import vpyplot as vlt
from matplotlib import pyplot as plt


viscid.readers.openggcm.GGCMFile.read_log_file = True
viscid.readers.openggcm.GGCMGrid.mhd_to_gse_on_read = 'auto'


f3d = viscid.load_file(path.join(viscid.sample_dir, 'sample_xdmf.3d.xdmf'))
B = f3d['b']['x=-40j:15j, y=-20j:20j, z=-20j:20j']

# for this method, seeds must be a SeedGen subclass, not a field subset
seeds = viscid.Volume(xl=(-40, 0, -20), xh=(15, 0, 20), n=(64, 1, 128))

trace_opts = dict(ibound=2.5)
xpts = viscid.get_sep_pts_bisect(B, seeds, trace_opts=trace_opts)

# all done, now just make some illustration
log_bmag = np.log(viscid.magnitude(B))
lines, topo = viscid.calc_streamlines(B, seeds, **trace_opts)

vlt.plot(topo, cmap='afmhot')

vlt.plot2d_lines(lines[::79], scalars=log_bmag, symdir='y')
plt.plot(xpts[0], xpts[2], 'y*', ms=20,
             markeredgecolor='k', markeredgewidth=1.0)
plt.xlim(topo.xl[0], topo.xh[0])
plt.ylim(topo.xl[2], topo.xh[2])

# since seeds is a Field, we can use it to determine mhd|gse
vlt.plot_earth(B['y=0j'])

vlt.show()
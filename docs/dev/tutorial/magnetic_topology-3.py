from os import path

import numpy as np
import viscid
from viscid.plot import vpyplot as vlt
from matplotlib import pyplot as plt


viscid.readers.openggcm.GGCMFile.read_log_file = True
viscid.readers.openggcm.GGCMGrid.mhd_to_gse_on_read = 'auto'


f3d = viscid.load_file(path.join(viscid.sample_dir, 'sample_xdmf.3d.xdmf'))
B = f3d['b']['x=-40j:15j, y=-20j:20j, z=-20j:20j']

# Fields can be used as seeds to get one seed per grid point
seeds = B.slice_keep('y=0j')
lines, topo = viscid.calc_streamlines(B, seeds, ibound=2.5,
                                      output=viscid.OUTPUT_BOTH)
xpts_night = viscid.topology_bitor_clusters(topo['x=:0j, y=0j'])

# The dayside is done separately here because the sample data is at such
# low resolution. Super-sampling the grid with the seeds can sometimes help
# in these cases.
day_seeds = viscid.Volume((7.0, 0.0, -5.0), (12.0, 0.0, 5.0), (16, 1, 16))
_, day_topo = viscid.calc_streamlines(B, day_seeds, ibound=2.5,
                                      output=viscid.OUTPUT_TOPOLOGY)
xpts_day = viscid.topology_bitor_clusters(day_topo)

log_bmag = np.log(viscid.magnitude(B))

clim = (min(np.min(day_topo), np.min(topo)),
        max(np.max(day_topo), np.max(topo)))
vlt.plot(topo, cmap='afmhot', clim=clim)
vlt.plot(day_topo, cmap='afmhot', clim=clim, colorbar=None)

vlt.plot2d_lines(lines[::79], scalars=log_bmag, symdir='y')
plt.plot(xpts_night[0], xpts_night[1], 'y*', ms=20,
             markeredgecolor='k', markeredgewidth=1.0)
plt.plot(xpts_day[0], xpts_day[1], 'y*', ms=20,
             markeredgecolor='k', markeredgewidth=1.0)
plt.xlim(topo.xl[0], topo.xh[0])
plt.ylim(topo.xl[2], topo.xh[2])

# since seeds is a Field, we can use it to determine mhd|gse
vlt.plot_earth(seeds.slice_reduce(":"))

vlt.show()
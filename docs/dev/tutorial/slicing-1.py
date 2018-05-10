from os import path

import viscid
from viscid.plot import vpyplot as vlt


f3d = viscid.load_file(path.join(viscid.sample_dir, 'sample_xdmf.3d.xdmf'))

# snip off the first 5 and last 25 cells in x, and grab every other cell
# in z between z = -8.0 and z = 10.0 (in space, not index).
# Notice that slices by location are done by appending an 'f' to the
# slice. This means "y=0" is not the same as "y=0f".
pp = f3d["pp"]["x = 5:-25, y = 0.0f, z = -8.0f:10.0f:2"]
vlt.plot(pp, style="contourf", levels=50, plot_opts="log,earth")

vlt.show()
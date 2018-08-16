from os import path

import viscid
from viscid.plot import vpyplot as vlt
from matplotlib import pyplot as plt


f3d = viscid.load_file(path.join(viscid.sample_dir, 'sample_xdmf.3d.xdmf'))

vx = f3d["v"]["x, x = 5:-25, y = 0.0j, z = -8.0j:10.0j:2"]

# this slice is also equivalent to...
# >>> vx = f3d["vx"]["x = 5:-25", "y = 0.0j", "z = -8.0j:10.0j:2"]

plt.subplots(1, 1, figsize=(10, 5))
vlt.plot(vx, style="contourf", levels=50, plot_opts="earth")

vlt.show()
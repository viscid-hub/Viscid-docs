from os import path

import viscid
from viscid.plot import vpyplot as vlt
from matplotlib import pyplot as plt


f3d = viscid.load_file(path.join(viscid.sample_dir, 'sample_xdmf.3d.xdmf'))

fig, axes = plt.subplots(1, 2, sharex=True, sharey=True)

# plot pressure with 64 contours on a logscale
vlt.plot(f3d["pp"]["y=0.0f"], style="contourf", levels=64,
         plot_opts="log, earth", ax=axes[0])

# plot velocity in x with a colorbar symmetric about 0
# also, share axes so this plot pans/zooms with the first
vlt.plot(f3d["vx"]["y=0.0f"], style="contourf", levels=64,
         lin=0, earth=True, ax=axes[1])

plt.xlim((-20, 20))
plt.ylim((-10, 10))

vlt.auto_adjust_subplots()

vlt.show()
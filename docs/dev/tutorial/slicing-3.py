from os import path

import numpy as np
import viscid
from viscid.plot import vpyplot as vlt
from matplotlib import pyplot as plt


f2d = viscid.load_file(path.join(viscid.sample_dir, 'sample_xdmf.py_0.xdmf'))

times = np.array([grid.time for grid in f2d.iter_times(":2")])
nr_times = len(times)

_, axes = plt.subplots(nr_times, 1)

for i, grid in enumerate(f2d.iter_times(":2")):
    vlt.plot(grid["vz"]["x = -20.0j:20.0j, y = 0.0j, z = -10.0j:10.0j"],
             plot_opts="lin_0,earth", ax=axes[i])
    plt.title(grid.format_time(".01f"))

vlt.auto_adjust_subplots()
vlt.show()
from os import path

import viscid
from viscid.plot import vpyplot as vlt
from matplotlib import pyplot as plt


f3d = viscid.load_file(path.join(viscid.sample_dir, 'sample_xdmf.3d.xdmf'))

_, axes = plt.subplots(2, 1, sharex=True, sharey=True)
f3d.activate_time(0)

# notice y=0.0, this is different from y=0; y=0 is the 0th index in
# y, which is this case will be y=-50.0
vlt.plot(f3d["vz"]["x = -20.0f:20.0f, y = 0.0f, z = -10.0f:10.0f"],
         style="contourf", levels=50, plot_opts="lin_0,earth", ax=axes[0])
plt.title(f3d.get_grid().format_time("UT"))

# share axes so this plot pans/zooms with the first
f3d.activate_time(-1)
vlt.plot(f3d["vz"]["x = -20.0f:20.0f, y = 0.0f, z = -10.0f:10.0f"],
         style="contourf", levels=50, plot_opts="lin_0,earth", ax=axes[1])
plt.title(f3d.get_grid().format_time("hms"))

vlt.auto_adjust_subplots()
vlt.show()
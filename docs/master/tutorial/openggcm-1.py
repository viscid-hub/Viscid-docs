from os import path

import viscid
from viscid.plot import vpyplot as vlt
from matplotlib import pyplot as plt


viscid.readers.openggcm.GGCMFile.read_log_file = True
viscid.readers.openggcm.GGCMGrid.mhd_to_gse_on_read = 'auto'


f3d = viscid.load_file(path.join(viscid.sample_dir, 'sample_xdmf.3d.xdmf'))
pp = f3d["pp"]["x = -20.0f:20.0f, y = 0.0f, z = -10.0f:10.0f"]
vlt.plot(pp, plot_opts="log,x_-30_15", earth=True)
plt.title(pp.format_time("UT"))

vlt.show()
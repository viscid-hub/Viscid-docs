from os import path

import viscid
from viscid.plot import vpyplot as vlt
from matplotlib import pyplot as plt


f3d = viscid.load_file(path.join(viscid.sample_dir, 'sample_xdmf.3d.xdmf'))

vlt.plot(f3d['pp']['z=0j'], cbarlabel="Pressure", logscale=True, earth=True)
Q = vlt.plot2d_quiver(f3d['v']['x=::2, y=::2, z=0j'])
plt.quiverkey(Q, X=1.1, Y=1.07, U=400, label=r"400 $\frac{km}{s}$",
              labelpos='N')

plt.xlim(-20, 20)
plt.ylim(-10, 10)

vlt.show()
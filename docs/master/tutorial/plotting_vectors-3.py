from os import path

import viscid
from viscid.plot import vpyplot as vlt
from matplotlib import pyplot as plt


viscid.calculator.evaluator.enabled = True


f3d = viscid.load_file(path.join(viscid.sample_dir, 'sample_xdmf.3d.xdmf'))

vlt.plot(f3d['Pressure = pp']['z=0j'], logscale=True, earth=True)
new_grid = viscid.Volume((-20, -20, 0), (20, 20, 0), n=(16, 16, 1))
v = viscid.interp_trilin(f3d['v'], new_grid)
Q = vlt.plot2d_quiver(v['z=0j'])
plt.quiverkey(Q, X=1.1, Y=1.07, U=400, label=r"400 $\frac{km}{s}$",
              labelpos='N')


plt.xlim(-20, 20)
plt.ylim(-10, 10)

vlt.show()
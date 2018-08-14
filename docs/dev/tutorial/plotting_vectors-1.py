from os import path

import viscid
from viscid.plot import vpyplot as vlt
from matplotlib import pyplot as plt


viscid.calculator.evaluator.enabled = True


f3d = viscid.load_file(path.join(viscid.sample_dir, 'sample_xdmf.3d.xdmf'))

vlt.plot(f3d['Pressure = pp']['z=0j'], logscale=True, earth=True)

v = f3d['v']
speed = viscid.magnitude(v)
lw = 4 * speed / speed.max()
slc = 'z=0j'
vlt.streamplot(v[slc], arrowsize=2, density=2, linewidth=lw[slc], color='k')

plt.xlim(-20, 20)
plt.ylim(-10, 10)

vlt.show()
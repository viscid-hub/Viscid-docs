import numpy as np
import viscid
from viscid.plot import vpyplot as vlt
import matplotlib.pyplot as plt


x = np.linspace(-1, 1, 64)
y = np.linspace(-1, 1, 32)
z = np.linspace(-1, 1, 5)

fld = viscid.empty([x, y, z], nr_comps=3, layout='interlaced',
                   name="VFld1", pretty_name="Velocity [m/s]")
X, Y, Z = fld.get_crds(shaped=True)

# set the x, y, and z vector components separately
fld['x'] = 0.0 * X + 2.0 * Y + 0.0 * Z
fld['y'] = 1.0 * X + 0.0 * Y + 0.0 * Z
fld['z'] = 0.1 * (X * Y)

plt.figure(figsize=(8, 5))
vlt.plot(fld['z']['z=0f'], cbarlabel="V$_z$ [m/s]")
vlt.streamplot(fld['z=0f'])
vlt.auto_adjust_subplots()
plt.show()
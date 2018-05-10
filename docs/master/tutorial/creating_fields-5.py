import numpy as np
import viscid
from viscid.plot import vpyplot as vlt
import matplotlib.pyplot as plt


x = np.linspace(-1, 1, 64)
y = np.linspace(-1, 1, 32)

fld1 = viscid.empty([x, y], center='cell', name="ScalarFld",
                    pretty_name="Scalar Field")

# create fld2 using the same coordinates as fld1
fld2 = viscid.empty(fld1.crds, nr_comps=3, name="VectorFld",
                    pretty_name="Vector Field")

X, Y = fld2.get_crds(shaped=True)
fld2['x'] = 0.0 * X + 1.0 * Y
fld2['y'] = 1.0 * X + 0.0 * Y
fld2['z'] = 0.1 * (X * Y)

plt.figure(figsize=(8, 5))
vlt.plot(fld2['z'], cbarlabel="V$_z$ [m/s]")
vlt.plot2d_quiver(fld2, step=4)
vlt.auto_adjust_subplots()
plt.show()
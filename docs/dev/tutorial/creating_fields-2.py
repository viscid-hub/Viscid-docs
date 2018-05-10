import numpy as np
import viscid
from viscid.plot import vpyplot as vlt
import matplotlib.pyplot as plt


# now the coordinates are rectilinear, and that's ok too
a = np.linspace(1.0, 2.0, 64)**2
b = np.linspace(1.0, 2.0, 32)**2

# create a new field, this time it's node centered
fld = viscid.empty([a, b], crd_names=('axis-a', 'axis-b'), center='node',
                   name="Oscillations", pretty_name="Oscillations $[W/m^2]$")

# fill the field with data... shaped crds are a lightweight way
# to broadcast to the field's shape
A, B = fld.get_crds(shaped=True)
fld[...] = np.sin(4 * A) + B + 0.5

plt.figure(figsize=(8, 5))
vlt.plot(fld, g='#7C1607')
vlt.auto_adjust_subplots()
plt.show()
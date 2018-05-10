import numpy as np
import viscid
from viscid.plot import vpyplot as vlt
import matplotlib.pyplot as plt


# Make some coordinate arrays. These happen to have uniform grid spacing.
# In most cases, Viscid will notice that and make a uniform coordinates.
# Interpolation / streamline calculation is faster on uniform fields than
# nonuniform (rectilinear) fields.
x = np.linspace(-1, 1, 64)
y = np.linspace(-1, 1, 32)

# create a new field
fld = viscid.empty([x, y], center='cell', name="MyField",
                   pretty_name="My Field [Units]")

# fill the field with data... shaped crds are a lightweight way
# to broadcast to the field's shape
X, Y = fld.get_crds(shaped=True)
fld[...] = X**2 + Y**3 + 2.0 * X * Y - 0.5 * X

plt.figure(figsize=(8, 5))
vlt.plot(fld)
vlt.auto_adjust_subplots()
plt.show()
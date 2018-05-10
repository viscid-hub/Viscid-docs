import numpy as np
import viscid
from viscid.plot import vpyplot as vlt
import matplotlib.pyplot as plt


a = np.linspace(1.0, 2.0, 64)**2
b = np.linspace(1.0, 2.0, 32)**2

fld1 = viscid.empty([a, b], crd_names=('axis-a', 'axis-b'), center='node',
                    name="Fld1", pretty_name="Oscillations $[W/m^2]$")
A, B = fld1.get_crds(shaped=True)
fld1[...] = np.sin(4 * A) + B + 0.5

# create and fill a field like fld1
fld2 = viscid.full_like(fld1, np.nan, name='Fld2',
                        pretty_name="Fld 2 $[W/m^2]$")
fld2[...] = np.sin(8 * A) - B - 0.5

_, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 5))
vlt.plot(fld1, g='#7C1607', ax=ax0)
vlt.plot(fld2, g='#7C1607', ax=ax1)
vlt.auto_adjust_subplots()
plt.show()
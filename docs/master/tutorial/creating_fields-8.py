import numpy as np
import viscid
from viscid.plot import vpyplot as vlt
import matplotlib.pyplot as plt


x = np.linspace(-1.0, 1.0, 64).reshape(-1, 1)
y = np.linspace(-1.0, 1.0, 32).reshape(1, -1)
dat = 1.0 - np.sin(16 * x) + np.cos(8 * y)

fld = viscid.dat2field(dat, name="Waves")
plt.figure(figsize=(8, 5))
vlt.plot(fld)
vlt.auto_adjust_subplots()
plt.show()
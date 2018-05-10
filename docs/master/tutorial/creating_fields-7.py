import numpy as np
import viscid
from viscid.plot import vpyplot as vlt
import matplotlib.pyplot as plt


x = np.linspace(-1.0, 1.0, 32)
y = np.linspace(-1.0, 1.0, 64)
dat = np.sin(10 * x.reshape(-1, 1)) + np.cos(8 * y.reshape(1, -1))

fld = viscid.arrays2field([x, y], dat, name="Waves")
plt.figure(figsize=(8, 5))
vlt.plot(fld)
vlt.auto_adjust_subplots()
plt.show()
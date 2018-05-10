import numpy as np
import viscid
from viscid.plot import vpyplot as vlt
import matplotlib.pyplot as plt


grid = viscid.grid.Grid()

grid.crds = viscid.arrays2crds([np.linspace(-1, 1, 32),
                                np.linspace(-1, 1, 64)])
grid.add_field(viscid.full(grid.crds, np.nan, name='a'))
grid.add_field(viscid.full(grid.crds, np.nan, name='b'))

X, Y = grid.get_crds_cc(shaped=True)
grid['a'][...] = 1.0 + np.sin(4 * X) + np.cos(8 * Y) + 2.0 * X * Y
grid['b'][...] = np.sin(4 * X) - np.cos(8 * Y) - 2.0 * X * Y

_, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 5))
vlt.plot(grid['a'], ax=ax0)
vlt.plot(grid['b'], ax=ax1)
vlt.auto_adjust_subplots()
plt.show()
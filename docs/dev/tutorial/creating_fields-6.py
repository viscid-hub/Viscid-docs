import matplotlib.dates as mdates
import numpy as np
import viscid
from viscid.plot import vpyplot as vlt
import matplotlib.pyplot as plt


t = viscid.linspace_datetime64('2010-06-23T03:00:00.0',
                               '2010-06-23T21:00:00.0', 256)

fld = viscid.empty([t], crd_names=['t'], center='node', name="TSeries",
                   pretty_name="Shadow Length [Smoots]")

t_sec = (fld.get_crd('t') - fld.get_crd('t')[0]) / np.timedelta64(1, 's')
fld[:] = (0.02 * np.sin(t_sec / (0.15 * 3600.0)) +
          0.20 * np.sin(t_sec / (1.0 * 3600.0)) +
          0.10 * np.sin(t_sec / (10.0 * 3600.0)) +
          1.0)

plt.figure(figsize=(8, 5))

vlt.plot(fld)

dateFmt = mdates.DateFormatter('%H:%M:%S')
plt.gca().xaxis.set_major_formatter(dateFmt)
plt.gcf().autofmt_xdate()
plt.gca().grid(True)

plt.show()
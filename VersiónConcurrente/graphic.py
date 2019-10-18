import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

filename=sys.argv[1]

file_time=open(filename,"r+")



# Data for plotting
t = np.arange(14.0, 25.0, 1.0)
s1 = 

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
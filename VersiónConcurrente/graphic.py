import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys
import re

time_dict={}
filenames=sys.argv[1:]
for filename in filenames:
    time_dict[filename]=[]
    array_line=[]
    file_time=open("tiempos/"+filename,"r+")
    for line in file_time:
        array_time=line.split()
        if array_time:
            if array_time[0]=="real":
                time_dict[filename].append(((array_time[1].replace(",",".")).replace("m","s")).split("s")[1])

# Data for plotting
t = np.arange(13.0, 25.0, 1.0)
s1 = time_dict["1_core.txt"]
s2 = time_dict["2_core.txt"]


fig, ax = plt.subplots()
ax.plot(t, s1)
ax.plot(t, s2)

ax.set(xlabel='time (s)', ylabel='trees',
       title='Comparacion tiempos aplicación multihilo')
ax.grid()

fig.savefig("test.png")
plt.show()
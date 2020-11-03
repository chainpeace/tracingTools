### draw cpu utilization graph from csv file ###
### 2020.07.26 ###

from pandas import DataFrame
from pandas import read_csv
from matplotlib import pyplot
import numpy

### file configuration ###

srcdir="./csv/"
dstdir="./graph/"
name="seq"
thread=""

####

usage = read_csv(srcdir+name+thread+"_top.csv")
print(usage)

ind = list(usage['time'])
print(usage.index)

xpos = numpy.arange(len(usage.index))
usage['cpu usage(%)'].plot()

pyplot.grid()
pyplot.legend()
pyplot.title("Process Cpu Utilization")
pyplot.xlabel("time")
pyplot.ylabel("CPU usage(%)")
pyplot.xlim(usage.index[0], usage.index[-1])
pyplot.ylim(0,50)
#pyplot.xticks(xpos, ind)
pyplot.savefig(dstdir+name+thread+"_cpuuilt.png")

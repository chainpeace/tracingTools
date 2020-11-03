### draw cpu utilization graph from csv file v2 ###
### 2020.07.29 ###

from pandas import DataFrame
from pandas import read_csv
from matplotlib import pyplot
import numpy

import normalize as nz
def draw_time_graph():
    
    srcdir="./csv/"
    dstdir="./graph/"
    name1="seq"
    name2="sp"
    name3="spc"
    
    
    proclst = ["seq", "sp"]
    timelst = []

    df = read_csv(srcdir+name1+"_top.csv")
    time = list(df['time'].index)[-1]
    timelst.append(time)
    
    
    df = read_csv(srcdir+name2+"_top.csv")
    time = list(df['time'].index)[-1]
    timelst.append(time)

    
    thr = 1
    for i in range(1,11):
        thr *= 2
        thread = str(thr)
        df = read_csv(srcdir+name3+thread+"_top.csv")
        time = list(df['time'].index)[-1]
        timelst.append(time)
        proclst.append(name3+thread)

    print(timelst)
    print(proclst)

    pyplot.bar(proclst, timelst)
    pyplot.savefig("./graph/bar.png")

def draw_graphs():
### file configuration ###

    srcdir="./csv/"
    dstdir="./graph/"
    name1="seq"
    name2="sp"
    name3="spc"
    thread3="64"
####

    df1 = read_csv(srcdir+name1+"_top.csv")
    df2 = read_csv(srcdir+name2+"_top.csv")
    df3 = read_csv(srcdir+name3+thread3+"_top.csv")

    time1 = list(df1['time'].index)
    time2 = list(df2['time'].index)
    time3 = list(df3['time'].index)

    maxtime = max((time1[-1],time2[-1],time3[-1]))

    df1['cpu usage(%)'].plot(label="seq")
    df2['cpu usage(%)'].plot(label="sp")
    df3['cpu usage(%)'].plot(label="spc64")

    pyplot.grid()
    pyplot.legend()
    pyplot.title("Process Cpu Utilization")
    pyplot.xlabel("time")
    pyplot.ylabel("CPU usage(%)")
    pyplot.xlim(0, maxtime)
    pyplot.ylim(0,50)
    pyplot.savefig(dstdir+"test1_cpuuilt.png")

def draw_graphs_iter(start, end, dst):
### file configuration ###

    srcdir="./csv/"
    dstdir="./graph/"
    name1="seq"
    name2="sp"
    name3="spc"
    thread3="64"
####

    df1 = read_csv(srcdir+name1+"_top.csv")
    df1['cpu usage(%)'].plot(label="seq")
    time1 = list(df1['time'].index)
    
    df2 = read_csv(srcdir+name2+"_top.csv")
    df2['cpu usage(%)'].plot(label="sp")
    time2 = list(df2['time'].index)
    
    #thr = 1
    #maxtime = 0
   
    src = srcdir+name3
    maxtime = draw_iter(start, end ,src)
   
    """
    for i in range(1,11):
        
        thr *= 2
        thread = str(thr)
        
        df3 = read_csv(srcdir+name3+thread+"_top.csv")
        df3['cpu usage(%)'].plot(label="spc"+thread)
        
        time3 = list(df3['time'].index)
        maxtime = max(time3[-1], maxtime) 
    """
    maxtime = max((time1[-1],time2[-1],maxtime))

    pyplot.grid()
    pyplot.legend()
    pyplot.title("Process Cpu Utilization")
    pyplot.xlabel("time (sec)")
    pyplot.ylabel("CPU usage(%)")
    pyplot.xlim(0, maxtime)
    pyplot.ylim(0,50)
    pyplot.savefig(dstdir+dst)

def draw_iter(start, end, src):
    thr = 2**start
    maxtime = 0
    for i in range(start, end+1):
        thread = str(thr)

        df = read_csv(src+thread+"_top.csv")
        df['cpu usage(%)'].plot(label="spc"+thread)

        time = list(df['time'].index)
        maxtime = max(time[-1], maxtime)

        thr *= 2

    return maxtime

def draw_normalized_graphs():

### file configuration ###

    srcdir="./csv/"
    dstdir="./graph/"
    name1="seq"
    name2="sp"
    name3="spc"
    thread3="64"
####

    df1 = read_csv(srcdir+name1+"_top.csv")
    df2 = read_csv(srcdir+name2+"_top.csv")
    df3 = read_csv(srcdir+name3+thread3+"_top.csv")

    time1 = list(df1['time'].index)
    time2 = list(df2['time'].index)
    time3 = list(df3['time'].index)
    
    n_time1 = nz.normalize_100(time1)
    n_time2 = nz.normalize_100(time2)
    n_time3 = nz.normalize_100(time3)

    pyplot.plot(n_time1, df1['cpu usage(%)'], label="seq")
    pyplot.plot(n_time2, df2['cpu usage(%)'], label="sp")
    pyplot.plot(n_time3, df3['cpu usage(%)'], label="spc64")
    
    pyplot.legend()
    pyplot.grid()
    pyplot.title("Process Cpu Utilization")
    pyplot.xlabel("time")
    pyplot.ylabel("CPU usage(%)")
    pyplot.xlim(0, 100)
    pyplot.ylim(0,50)
    pyplot.tick_params(
            axis='x',
            which='both',
            labelbottom=False)
   
    pyplot.savefig(dstdir+"test3_cpuuilt.png")

if __name__ == "__main__":
    
    draw_time_graph()
    """
    draw_graphs_iter(1, 2, "test9_cpuuilt.png" )
    pyplot.clf()
    draw_graphs_iter(3, 4, "test10_cpuuilt.png" )
    pyplot.clf()
    draw_graphs_iter(5, 6, "test11_cpuuilt.png" )
    pyplot.clf()
    draw_graphs_iter(7, 8, "test12_cpuuilt.png" )
    pyplot.clf()
    draw_graphs_iter(9, 10, "test13_cpuuilt.png" )
    """
    #draw_normalized_graphs()

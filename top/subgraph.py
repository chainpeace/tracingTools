### draw cpu util subgraphs ###
### 2020.07.29 ###


from pandas import DataFrame
from pandas import read_csv
from matplotlib import pyplot
import numpy

def draw(subplot, df):
    subplot.grid()
    subplot.set_xlabel("time")
    subplot.set_ylabel("cpu usage")
    subplot.set_xlim(0, df.index[-1])
    subplot.set_ylim(0,50)

    newticks = subplot.get_xticks()
    newticks[-1] = df.index[-1]
    subplot.set_xticks(newticks)


def draw_subgraphs():
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

    pyplot.figure(1) # figure identifier
    sub = pyplot.subplot(311) # subplot rownum, colnum, plot id
    df1['cpu usage(%)'].plot()
    draw(sub, df1)
    pyplot.title("SEQ")

    sub = pyplot.subplot(312)
    df2['cpu usage(%)'].plot()
    draw(sub, df2)
    pyplot.title("SP")
    
    sub = pyplot.subplot(313)
    df3['cpu usage(%)'].plot()
    draw(sub, df3)
    pyplot.title("SPC64")

    pyplot.figure(1).tight_layout()

    pyplot.savefig(dstdir+"test2_cpuutil.png")

if __name__ == "__main__":
    draw_subgraphs()


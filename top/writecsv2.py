### modify top log to csv file ###
### 2020.07.29 ###
### 2020.07.30 modified ###

import csv, sys
import getargu as ga
from parse import compile
from listdir import flist

def writecsv(thread=2):
    name = "seq"
    src = "../newnewlog"
    thread = ""

    #outf = open("csv/"+name+str(thread)+"_iter.csv", 'w')
    outf = open("csv/"+name+"_iter.csv", 'w')
    wr = csv.writer(outf)

    for i in range(1,8):
        utils, times = readlog(name, thread, src, i)
        utils.insert(0, "util"+str(i))
        times.insert(0, "time"+str(i))
        wr.writerow(times)
        wr.writerow(utils)
    outf.close()


def readlog(name, thr, src, iteration):

    i = str(iteration)
    thread = str(thr)

    inf=open(src+"/"+name+thread+"_"+i+"_top.log", 'r')

    #wr = csv.writer(outf)

    pattern1 = compile("top - {time} up {}")
    pattern2 = compile("{:>d} {} {:.1l}{cpu:^f}{}")

    eof = False
    timeline = None
    utils=[]
    times=[]

    while not eof:
        
        if not timeline:
            line = inf.readline()
            if not line: break;

            timeline = pattern1.parse(line)
        
        while timeline:
            time = timeline['time']
            
            line = inf.readline()
            if not line:
                eof = True
                break
            
            timeline = pattern1.parse(line)
            utilline = pattern2.parse(line)
            
            if utilline: break
        
        if eof: break
        
        util = 0

        while utilline:
            util += utilline['cpu']
            
            line = inf.readline()
            if not line: 
                eof = True
                break
            
            timeline = pattern1.parse(line)
            utilline = pattern2.parse(line)

            if timeline: break

        #wr.writerow([time,util])
        times.append(time)
        utils.append(util)

    inf.close()
    return utils, times
    
if __name__ == "__main__":
    
    #lst = (2,4,8,16,32,64,128,256,512,1024)
    #for i in lst:
    #    writecsv(i)
    
    writecsv()

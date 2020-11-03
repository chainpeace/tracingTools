### modify top log to csv file ###
### 2020.07.29 ###
### 2020.07.30 modified ###

import csv, sys
import getargu as ga
from parse import compile
from listdir import flist

def writecsv_all(path):
    files = flist(path)
    pattern = compile("{name}.log")
    print(files)

    for f in files:
        do = pattern.parse(f)
        if do:
            print(pattern.parse(f)['name'])
            writecsv2(pattern.parse(f)['name'], path, "./newcsv")
            print("done") 
        if not do:
            print(f)

def writecsv2(name, src, dst):
    
    inf=open(src+"/"+name+".log", 'r')
    outf=open(dst+"/"+name+".csv", 'w', newline='')

    wr = csv.writer(outf)
    wr.writerow(["time","cpu usage(%)"])

    pattern1 = compile("top - {time} up {}")
    pattern2 = compile("{:>d} {} {:.1l}{cpu:^f}{}")

    eof = False
    timeline = None

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

        wr.writerow([time,util])

    inf.close()
    outf.close()

def writecsv(thr=64):
    
## config file path ##
    name="spc"
    thread=str(thr)
    srcdir="./log/"
    dstdir="./csv/"
####
    

    src = None
    dst = None

    src, dst = ga.getdir()
    print(src, dst)
    
    if src:
        srcname = src[1]
    else:
        srcname = srcdir+name+thread+"_top.log"

    if dst:
        dstname = dst[1]
    else:
        dstname = dstdir+name+thread+"_top.csv"

    print(srcname)


    inf=open(srcname, 'r')
    outf=open(dstname, 'w', newline='')

    wr = csv.writer(outf)
    wr.writerow(["time","cpu usage(%)"])

    pattern1 = compile("top - {time} up {}")
    pattern2 = compile("{:>d} {} {:.1l}{cpu:^f}{}")

    eof = False
    timeline = None

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

        wr.writerow([time,util])

    inf.close()
    outf.close()

if __name__ == "__main__":
    writecsv_all("/home/inhwi/newlog")
    
    """
    lst = (2,4,8,16,32,128,256,512,1024)
    for i in lst:
        writecsv(i)
    """
    #writecsv()

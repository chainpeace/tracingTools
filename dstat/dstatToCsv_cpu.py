### modify dstat cpu log(per core) to csv file ###
### 2021.02.04 ###

import csv
from parse import compile

def unit_change(unit_before, unit_after, data) :
    if unit_after != "m" and unit_after != "M" :
        print("not implemented unit change\n")
        exit(-1)

    if unit_before == "g" or unit_before == "G" :
        data = data * 1024
        return data

    if unit_before =="k" or unit_before == "K" :
        data = data / 1024
        return data

    return data

# make dstat cpu pattern
# core: num of core
# pattern: pattern string
def makeCPUPattern(pattern, core):
    core = int(core)
    if core < 1:
        return None

    if core == 1:
        return None
    else:
        #per core
        #for example, "{usr1:g}{sys1:g}{idl1:g}{wai1:g}{stl1:g}"
        for i in range(0, core):
            c = str(i)
            pattern+="{usr"+c+":>g}{sys"+c+":>g}{idl"+c+":>g}{wai"+c+":>g}{}:"
        #total cpu
        pattern+="{usr_t:>g}{sys_t:>g}{idl_t:>g}{wai_t:>g}"
        #print("pattern string: "+pattern)
        return pattern

def makeDiskTotalPattern(pattern):
    pattern+="{read_t:g}{read_t_unit:.1l}{write_t:g}{write_t_unit:.1l}"
    return pattern

def makeNetTotalPattern(pattern):
    pattern+="{recv_t:g}{recv_t_unit:.1l}{send_t:g}{send_t_unit:.1l}"
    return pattern

def makeOtherPattern(pattern):
    pattern+="{}"
    return pattern

def writeCPUTitle(writer,core):
    core = int(core)
    if core > 1:
        title = []
        #write title1
        for c in range(0, core):
            title.extend(["cpu-"+str(c), "", "", ""])
        title.extend(["cpu-total", "", "", ""])
        writer.writerow(title)
        
        title = []
        #write title2
        for c in range(0,core):
            title.extend(["usr", "sys", "wait", "sum"])
        title.extend(["usr", "sys", "wait", "sum"])
        writer.writerow(title)
        
        return
    else:
        print("error in writing title")
        return


def writecsv(ifilename, ofilename, core):
    
    inf=open(ifilename, 'r')
    outf=open(ofilename, 'w', newline='')
    unit = "m"
    unit_str = "MB"

    wr = csv.writer(outf)
    writeCPUTitle(wr, core)
    #wr.writerow([""])
    #wr.writerow(["time","used", "free", "buff", "cach"])
    
    pattern = makeCPUPattern("", int(core))
    
    #pattern = "{test1:>g}{test2:>g}"
    pattern += "{}"
    #print("pattern string:"+pattern)
    compiled = compile(pattern)
#    pattern = compile("{time}|{used:g}{used_unit:.1l}{free:>g}{free_unit:.1l}{buff:>g}{buff_unit:.1l}{cach:>g}{cach_unit:.1l}")

    # ignore header
    line = inf.readline()
    line = inf.readline()
    line = inf.readline()

    #parsing start
    line = inf.readline()
    while line:
        
        parsed = compiled.parse(line)
        if parsed is None:
            print("parsed string in None")
            print("parsing line is : ")
            print(line)
            return 
        #print("parsed string : ")
        #print(parsed)
        row = []
        for i in range(0, core):
            c = str(i)
            row.extend([parsed["usr"+c], parsed["sys"+c], parsed["wai"+c], 
                100-parsed["idl"+c]])
        row.extend([parsed["usr_t"], parsed["sys_t"], parsed["wai_t"], 
            100-parsed["idl"+c]])
        
        #print("row string: ")
        #print(row)

        wr.writerow(row)

        line = inf.readline()

    inf.close()
    outf.close()

if __name__ == "__main__":
    ipath = "/home/dcslab/ihhwang/20210129-baseline_test/" 
    opath = "/home/dcslab/ihhwang/20210129-baseline_test/output/" 
    #filename = "cpu_io_1core_wcomp_wWAL"

    core_opt =[2,4]
    comp_opt = ["w","wo"]
    wal_opt = ["w", "wo"]

    for core in core_opt :
        for comp in comp_opt :
            for wal in wal_opt :
                filename = "cpu_io_"+str(core)+"core_"+comp+"comp_"+wal+"WAL"
                ifilename = ipath + filename + ".dstat.cpu"
                ofilename = opath + filename + ".csv"
                writecsv(ifilename, ofilename, int(core))
    

### modify dstat log to csv file ###
### used "dstat -mt" command  
### 2020.11.03 ###

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


def writecsv(ifilename, ofilename):
    
    inf=open(ifilename, 'r')
    outf=open(ofilename, 'w', newline='')
    unit = "m"
    unit_str = "MB"

    wr = csv.writer(outf)
    wr.writerow(["system", "memory usage("+unit_str+")"])
    wr.writerow(["time","used", "free", "buff", "cach"])

    pattern = compile("{time}|{used:g}{used_unit:.1l}{free:>g}{free_unit:.1l}{buff:>g}{buff_unit:.1l}{cach:>g}{cach_unit:.1l}")

    # ignore header
    line = inf.readline()
    line = inf.readline()

    line = inf.readline()
    while line:
        
        parsed = pattern.parse(line)
        #print(parsed)
        
        used = unit_change(parsed["used_unit"], "M", parsed["used"])
        free = unit_change(parsed["free_unit"], "M", parsed["free"])
        buff = unit_change(parsed["buff_unit"], "M", parsed["buff"])
        cach = unit_change(parsed["cach_unit"], "M", parsed["cach"])
        
        wr.writerow([parsed["time"], used, free, buff, cach])

        line = inf.readline()

    inf.close()
    outf.close()

if __name__ == "__main__":
    ipath = 
    opath = 
    #filename = "cpu_io_1core_wcomp_wWAL"

    core_opt = [1,2]
    comp_opt = ["w", "wo"]
    wal_opt = ["w", "wo"]

    for core in core_opt :
        for comp in comp_opt :
            for wal in wal_opt :
                filename = "cpu_io_"+str(core)+"core_"+comp+"comp_"+wal+"WAL"
                ifilename = ipath + filename + ".dstat"
                ofilename = opath + filename + ".csv"

                writecsv(ifilename, ofilename)
    
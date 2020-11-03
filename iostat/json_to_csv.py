#
# Converter for iostat json format output to csv format
#
# 2020.10.12
# Inhwi Hwang
# 
from json_excel_converter import Converter, LinearizationError 
from json_excel_converter.csv import Writer
import json

def convert(filename): 
    # input file path
    ifile = filename+".json"
    ofile = filename+".csv"

    with open(ifile, "r") as io_json:
        io_python = json.load(io_json)

    #print(io_python["sysstat"]["hosts"][0]["statistics"])
    data = io_python["sysstat"]["hosts"][0]["statistics"]

    conv = Converter()
    # output file path
    conv.convert(data, Writer(file=ofile))

ipath = "/home/inhwi/201103log/json/"
opath = "/home/inhwi/201103log/csv/"
cores = [1,2]#,4,8,16]
option_compaction = ["w", "wo"]
option_WAL = ["w", "wo"]

#close = "]}]}}"


for core in cores:
    for compaction in option_compaction:
        for wal in option_WAL:
            filename = ("cpu_io_"+str(core)+"core_"+compaction+"comp_"+wal+"WAL")
            #convert(filename)
            ifile = ipath+filename+".json"
            ofile = opath+filename+".csv" 

#            with open(ifile, "a") as io_json:
#                io_json.write(close)

            with open(ifile, "r") as io_json:
                io_python = json.load(io_json)

            #print(io_python["sysstat"]["hosts"][0]["statistics"])
            data = io_python["sysstat"]["hosts"][0]["statistics"]

            conv = Converter()
            # output file path
            conv.convert(data, Writer(file=ofile))

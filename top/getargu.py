### get arguments ###
## 2020.07.30 ##

def getdir():

    import sys, getopt

    try:

        options, remainder = getopt.getopt(sys.argv[1:], 'i:o:')

    except getopt.GetoptError as e:
        print(e)
        sys.exit()
    src = None
    dst = None
    
    for opt, val in options:
        if opt == '-i':
            src = ("src", val)
        elif opt == '-o':
            dst = ("dst", val)
    return src, dst

if __name__ == "__main__":
    getdir()

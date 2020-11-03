### read file list from a directory ###
### 2020.08.01 ###

import os 

def flist(path):
    file_list = os.listdir(path)

    return file_list

if __name__ == "__main__":
    print(flist("./"))


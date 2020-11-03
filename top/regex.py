### practice regular expression ###
### 2020.08.01 ###

import re

def pattern_match(regex, strl):
    pattern = re.compile(regex)
    mat = pattern.match(strl)
    return mat

if __name__ == "__main__":
    mat = pattern_match("[\w]*[.]log", "top_32_d.log")
    print(mat.group())

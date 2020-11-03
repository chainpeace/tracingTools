
def normalize(ls):
    normalized = []
    for value in ls:
        num = (value - min(ls))/(max(ls) - min(ls))
        normalized.append(num)

    return normalized

def normalize_100(ls):
    import numpy
    normalized = numpy.array(normalize(ls)) * 100
    return normalized


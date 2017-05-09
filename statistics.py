from math import sqrt
from functools import reduce

def mean(l):
    return sum(l)/len(l)

def var(l):
    m = mean(l)
    sq = list(map(lambda x : ((x - m)*(x - m)), l))
    return reduce(lambda p, q : p + q, sq)/(len(l) - 1)

def cov(a,b):
    m1 = reduce(lambda m, n : m + n, a) / len(a)
    m2 = reduce(lambda m, n : m + n, b) / len(b)
    x  = reduce(lambda m,n : m + n, list(map(lambda x, y : (x-m1)*(y-m2), a, b)))
    return x/(len(a)-1)

def r(a,b):
    return cov(a,b)/(sqrt(var(a))*sqrt(var(b)))

def var1(l):
    m = mean(l)
    sq = list(map(lambda x : ((x - m)*(x - m)), l))
    return reduce(lambda p, q : p + q, sq)/(len(l))

def cov1(a,b):
    m1 = reduce(lambda m, n : m + n, a) / len(a)
    m2 = reduce(lambda m, n : m + n, b) / len(b)
    x  = reduce(lambda m,n : m + n, list(map(lambda x, y : (x-m1)*(y-m2), a, b)))
    return x/(len(a))

def r1(a,b):
    return cov1(a,b)/(sqrt(var1(a))*sqrt(var1(b)))

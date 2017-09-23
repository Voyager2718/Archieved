from math import sqrt
from functools import reduce

# Mean value
def Mean(l):
    return sum(l)/len(l)

# Variance
def Var(l):
    m = Mean(l)
    sq = list(map(lambda x : ((x - m)*(x - m)), l))
    return reduce(lambda p, q : p + q, sq)/(len(l) - 1)

# Covariance
def Cov(a,b):
    m1 = reduce(lambda m, n : m + n, a) / len(a)
    m2 = reduce(lambda m, n : m + n, b) / len(b)
    x  = reduce(lambda m,n : m + n, list(map(lambda x, y : (x-m1)*(y-m2), a, b)))
    return x/(len(a)-1)

# Pearson product-moment correlation coefficient
def R(a,b):
    return Cov(a,b)/(sqrt(Var(a))*sqrt(Var(b)))

# Variance with -1
def Var1(l):
    m = Mean(l)
    sq = list(map(lambda x : ((x - m)*(x - m)), l))
    return reduce(lambda p, q : p + q, sq)/(len(l))

# Covariance with -1
def Cov1(a,b):
    m1 = reduce(lambda m, n : m + n, a) / len(a)
    m2 = reduce(lambda m, n : m + n, b) / len(b)
    x  = reduce(lambda m,n : m + n, list(map(lambda x, y : (x-m1)*(y-m2), a, b)))
    return x/(len(a))

# Pearson product-moment correlation coefficient with -1
def R1(a,b):
    return Cov1(a,b)/(sqrt(Var1(a))*sqrt(Var1(b)))

# Get information from csv file
def ReadFromCSV(path, separation = ','):
    titles = []
    contents = []
    with open(path, 'r') as file:
        lines = file.readline()
        titles = lines.replace('\r','').replace('\n','').split(separation)
        lines = file.readline()
        while(lines):
            tmp_data = lines.replace('\r','').replace('\n','').split(separation)
            tmp_content = {}
            for i in range(len(titles)):
                tmp_content[titles[i]] = tmp_data[i]
            contents += [tmp_content]
            lines = file.readline()
    return contents

# Write information to csv file
def WriteToCSV(path, separation = ','):
    return

# Get information from xml file

# Write information to xml file

# 
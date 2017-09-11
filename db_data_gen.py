from random import random
from math import *
import sys

separate = 10000

a = 0
f = ''
table = ''

def getChar(num):
    ch = ''
    for i in range(num):
        ch += chr(int(random()*26)+97)
    return ch

def main():
    fp = open(f, 'w+')
    for j in range(ceil(a / separate)):
        fp.write('insert into ' + table + ' values ')
        for i in range(j * separate, min((j + 1) * separate, (a - (j + 1) * separate) + (j + 1) * separate)):
            fp.write('('+ str(i) + ',\'' + getChar(32) + '\')')
            if(i != min((j + 1) * separate - 1, (a - (j + 1) * separate) + (j + 1) * separate - 1)):
                fp.write(',\n')
            else:
                fp.write(';\n')

if __name__ == '__main__':
    try:
        a = int(sys.argv[1])
        f = sys.argv[2]
        table = sys.argv[3]
    except:
        print("Err")
    main()
